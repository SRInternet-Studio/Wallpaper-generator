from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
import platform, re, os, sys
import aiohttp, aiofiles, subprocess
import inspect, mimetypes, base64, time
from PIL import Image
from io import BytesIO
from urllib.parse import urlparse, unquote
from functools import wraps
import asyncio, traceback
from typing import Optional, Union, List, Dict, Tuple, Any

import psutil
from UI import Dialog, Reloading_Dialog
from PySide6.QtWidgets import QDialog
from PySide6.QtCore import QTimer, QProcess
from qfluentwidgets import Flyout, InfoBarIcon, isDarkThemeMode

"""装饰器：限制函数只能被本模块内的其他函数调用"""
def internal_only(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # 获取调用栈信息
        caller_frame = inspect.currentframe().f_back
        caller_module = caller_frame.f_globals.get('__name__', '')
        
        # 仅允许本模块内的函数调用
        if caller_module != __name__:
            raise RuntimeError(f"{func.__name__} 是内部工具函数，禁止显式调用！")
        return func(*args, **kwargs)
    return wrapper

"""APIKernal 简化请求"""
async def _requests_api(
    api: str, 
    path: Optional[Union[str, List[str]]] = None,
    method: str = "GET",
    headers: Optional[Dict[str, str]] = {}, 
    payload: Optional[Dict[str, Any]] = {},
    timeout: int = 15
) -> Any:
    """
    简化的通用API请求函数
    
    :param api: API端点URL
    :param path: 要解析的路径（单个或多个）
    :param method: HTTP方法 (默认为GET)
    :param headers: 请求头
    :param payload: 请求负载
    :param timeout: 超时时间（秒）
    :return: 解析后的数据
    """
    a, b, c = await request_api(
        api=api,
        paths=path,
        method=method,
        headers=headers,
        payload=payload,
        timeout=timeout
    )
    return a

"""前端核心"""
async def TodayFortune() -> str:
    url = "https://v2.xxapi.cn/api/horoscope?type=aquarius&time=today"
    headers = {
        'User-Agent': 'xiaoxiaoapi/1.0.0 (https://xxapi.cn)'
    }

    try:
        data = await _requests_api(url, "data.todo", headers=headers)
        yi = data['yi']
        ji = data['ji']
        return f"{yi}\n{ji}"
    except:
        traceback.print_exc()
        # print("\n\n")
        return "无法获取今日运势"
    
async def Hitokota() -> str:
    content = ""
    try:
        content = str(await _requests_api(api="https://international.v1.hitokoto.cn/", path="hitokoto"))
    except:
        traceback.print_exc()
        print("\n\n")
        content = "请求失败。"
        
    return u"<html><head/><body><p><span style=\" font-size:12pt;\">{} </span></p><p align=\"right\"><span style=\" font-size:12pt;\">\u2014\u2014 \u4eca\u65e5\u56fe\u7247 </span></p></body></html>".format(content)
    

def show_dialog(title, content, TrueText, FalseText, Editable, dark=False):
    BatchWindow = QDialog()
    ui1 = Dialog.Ui_Form(title, content, TrueText, FalseText, Editable, dark)
    ui1.setupUi(BatchWindow)
    BatchWindow.exec()
    return ui1.IsTF()

async def check_network() -> Union[float, bool]:
    try:
        logger.debug("测试网络连接...")
        
        # 强制使用ASCII环境并设置ping目标
        env = os.environ.copy()
        env.update({
            'LC_ALL': 'C',
            'LANG': 'C',
            'LANGUAGE': 'C'
        })
        
        ping_target = 'cn.bing.com'
        timeout_sec = 5.0
        
        proc = await asyncio.create_subprocess_exec(
            'ping',
            '-n' if platform.system() == 'Windows' else '-c',
            '1',
            '-w' if platform.system() == 'Windows' else '-W',
            '1000',
            ping_target,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
            env=env
        )
        
        try:
            stdout, stderr = await asyncio.wait_for(proc.communicate(), timeout_sec)
        except asyncio.TimeoutError:
            proc.kill()
            logger.warning(f"网络连接超时 (>{timeout_sec}秒)")
            return False
        
        # 检查命令执行状态
        if proc.returncode != 0:
            logger.warning(f"网络无法连接: {proc.returncode}")
            return False
            
        # 直接处理二进制输出，强制提取数字
        output_bytes = stdout
        output_ascii = ''.join(chr(b) if b < 128 else ' ' for b in output_bytes)
        logger.debug(f"Ping输出 (原始字节): {output_bytes!r}")
        logger.debug(f"Ping输出 (ASCII处理): {output_ascii}")
        
        # 简化延迟提取 - 只查找数字+ms模式
        match = re.search(r'(\d+)\s*ms', output_ascii)
        if match:
            try:
                latency = float(match.group(1))
                logger.debug(f"网络延迟: {latency}ms")
                return latency
            except ValueError:
                logger.debug(f"未知的网络延迟: {match.group(1)}")
                return 0.0  # 网络连通但无法获取延迟
        
        return False
        
    except Exception:
        logger.exception("网络检测错误")
        return False    
    
def is_process_running(process_name):
    for proc in psutil.process_iter(['name']):
        if proc.info['name'] == process_name:
            return True
    return False
    
"""二进制解析"""
async def phrase_binary_images(response: aiohttp.ClientResponse, content, binary_data) -> List[bytes]:
    """解析二进制图片数据，支持multipart和单图"""
    images = []
    content_type = response.headers.get('Content-Type', '').lower()
    
    try:
        # 多图
        if 'multipart/' in content_type:
            images.extend(await _process_multipart(response, content))
        else:
            # 单图
            images.extend(await _process_single_image(response, binary_data))
            
        # 过滤非静态图片
        return [img for img in images if await _is_static_image(img)]
    except aiohttp.ClientConnectionError:
        logger.error("连接被服务器关闭，尝试重试...")
        raise  # 让上层调用者处理重试
    except Exception as e:
        logger.error(f"解析图片数据失败: {str(e)}")
        logger.debug(traceback.format_exc())
        return []

@internal_only
async def _process_multipart(response, content): # 多图
    parts = []
    boundary_match = re.search(r'boundary="?([^";]+)"?', response.headers.get('Content-Type', ''))
    if not boundary_match:
        return []
    
    boundary = boundary_match.group(1)
    part_boundary = f'--{boundary}'
    end_boundary = f'{part_boundary}--'
    
    raw_parts = content.split(part_boundary)[1:]
    for raw_part in raw_parts:
        if raw_part.strip() == '--' or raw_part.startswith(end_boundary): # 跳过结束标记
            continue
            
        header_body = raw_part.split('\r\n\r\n', 1) # 分割头部和主体
        if len(header_body) < 2:
            continue
            
        header, body = header_body
        body = body.rstrip('\r\n')
        content_type = re.search(r'Content-Type:\s*([^\r\n]+)', header, re.IGNORECASE)
        if content_type:
            content_type = content_type.group(1).lower()
            if 'image/' in content_type:
                binary_body = body.encode('latin1') # -> binary
                parts.append(binary_body)
    
    return parts

@internal_only
async def _process_single_image(response, binary_data): # 单图
    """处理单张图片的二进制数据"""
    content_type = response.headers.get('Content-Type', '').lower()
    if 'image/' in content_type or await _is_image_data(binary_data):
        return [binary_data]
    return []

@internal_only
async def _is_static_image(image_data):
    """动图排除"""
    try:
        img = Image.open(BytesIO(image_data))
        if img.format in ['GIF', 'WEBP', 'APNG']:
            try:
                img.seek(1)
                return False
            except EOFError:
                return True  # 单帧GIF/WEBP/APNG（静态）
        
        return img.format in ['JPEG', 'PNG', 'BMP', 'TIFF']
    
    except Exception:
        return False
    
@internal_only
async def _is_image_data(data):
    if len(data) < 12:
        return False
    
    # 魔数
    magic_numbers = {
        b'\xFF\xD8\xFF': 'JPEG',
        b'\x89PNG\r\n\x1a\n': 'PNG',
        b'GIF87a': 'GIF',
        b'GIF89a': 'GIF',
        b'BM': 'BMP',
        b'II*\x00': 'TIFF',
        b'MM\x00*': 'TIFF',
        b'\x00\x00\x01\x00': 'ICO',
    }
    
    for magic, fmt in magic_numbers.items():
        if data.startswith(magic):
            return True
    return False

"""图片下载"""
async def download_images_binary(binary_data_list: List[bytes], save_path: str, max_workers: int = 4) -> Dict[str, bool]:
    """
    下载二进制图片(支持单张和多张)
    
    :param binary_data_list: 图片二进制数据列表
    :param save_path: 保存路径 (文件或目录)
    :param max_workers: 最大并发数
    :return: 字典 {文件名: 是否成功}
    """
    logger.info(f"保存二进制图片数据: {len(binary_data_list)}张 -> {save_path}")
    
    async def _save_single(data: bytes, path: str) -> bool:
        try:      
            async with aiofiles.open(path, 'wb') as f:
                await f.write(data)
            logger.info(f"图片保存成功: {path}")
            return True
        except Exception as e:
            logger.error(f"图片保存失败: {path} - {str(e)}")
            logger.debug(traceback.format_exc())
            return False
    
    if len(binary_data_list) == 1:
        if os.path.isdir(save_path): # 如果save_path是目录，生成文件名
            filename = f"image_{datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"
            save_path = os.path.join(save_path, filename)
        completeness = await _save_single(binary_data_list[0], save_path)
        return {save_path: await _save_single(binary_data_list[0], save_path)}
    
    if not os.path.exists(save_path):
        os.makedirs(save_path)
        
    semaphore = asyncio.Semaphore(max_workers)
    results = {}
    tasks = []
    async def _save_with_semaphore(data, path):
        async with semaphore:
            return await _save_single(data, path)
        
    for i, data in enumerate(binary_data_list):
        filename = f"image_{datetime.now().strftime('%Y%m%d_%H%M%S')}_{i:03d}.jpg"
        path = os.path.join(save_path, filename)
        tasks.append(_save_with_semaphore(data, path))
    
    save_results = await asyncio.gather(*tasks, return_exceptions=True)
    for i, (data, result) in enumerate(zip(binary_data_list, save_results)):
        filename = f"image_{datetime.now().strftime('%Y%m%d_%H%M%S')}_{i:03d}.jpg"
        path = os.path.join(save_path, filename)
        if isinstance(result, Exception):
            logger.error(f"图片保存异常: {path} - {str(result)}")
            logger.debug(traceback.format_exc())
            results[path] = False
        else:
            results[path] = result
    
    return results

async def download_images(urls: Union[str, List[str]], save_path: str, max_workers: int = 4, timeout: int = 30, retries: int = 3) -> Dict[str, bool]:
    """
    下载图片(支持单张和多张)
    
    :param urls: 图片URL或URL列表
    :param save_path: 保存路径 (文件或目录)
    :param max_workers: 最大并发数
    :param timeout: 超时时间(秒)
    :param retries: 重试次数
    :return: 字典 {URL: 图片路径（保存成功）/False（保存失败）}
    """
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    logger.info(f"下载图片: {urls} -> {save_path}")
    
    async def _download_single(session: aiohttp.ClientSession, url: str, path: str) -> bool:
        for attempt in range(retries):
            try:
                logger.info(f"开始下载图片: {url} -> {path} (尝试 {attempt + 1}/{retries})")
                async with session.get(url, headers=headers, timeout=aiohttp.ClientTimeout(total=timeout)) as response:
                    response.raise_for_status()
                    total_size = int(response.headers.get('content-length', 0))
                    downloaded = 0
                    
                    async with aiofiles.open(path, 'wb') as f:
                        async for chunk in response.content.iter_chunked(8192):
                            await f.write(chunk)
                            downloaded += len(chunk)
                            if total_size > 0:
                                percent = (downloaded / total_size) * 100
                                # logger.debug(f"{os.path.basename(path)} 下载进度: {downloaded}/{total_size} bytes ({percent:.1f}%) - {url}")
                            else:
                                # logger.debug(f"{os.path.basename(path)} 已下载: {downloaded} bytes - {url}")
                                pass

                    logger.info(f"图片下载完成: {path}")
                    return True
                
            except Exception as e:
                logger.warning(f"图片下载失败 (尝试 {attempt + 1}/{retries}): {url} - {str(e)}")
                if attempt == retries - 1:
                    logger.error(f"图片下载最终失败: {url}")
                    logger.debug(traceback.format_exc())
                    return False
                await asyncio.sleep(1)
        return False
    
    def extract_filename(url, default_filename):
        origin_url = urlparse(url).path
        if not origin_url or origin_url.endswith('/'): 
            filename = default_filename
        else: 
            filename = unquote(os.path.basename(origin_url)).split('?')[0].split('#')[0]
        
        return (f"{filename}.jpg" if not "." in filename else filename).translate(str.maketrans(r'\/:*?"<>|', '_' * len(r'\/:*?"<>|')))
    
    if isinstance(urls, str):
        # 如果save_path是目录，才需要拼接文件名
        if os.path.isdir(save_path):
            # 尝试从URL获取文件名，否则使用带时间戳的默认文件名
            filename = extract_filename(urls, f"image_{datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg")
            save_path = os.path.join(save_path, filename)
        async with aiohttp.ClientSession() as session:
            completeness = await _download_single(session, urls, save_path)
            return {urls: save_path if completeness else False}
    
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    
    semaphore = asyncio.Semaphore(max_workers)
    results = {}
    
    async def _download_with_semaphore(session, url, path):
        async with semaphore:
            return await _download_single(session, url, path)
    
    async with aiohttp.ClientSession() as session:
        tasks = []
        for i, url in enumerate(urls):
            filename = extract_filename(url, f"image_{i}.jpg")
            path = os.path.join(save_path, filename)
            tasks.append(_download_with_semaphore(session, url, path))
        
        download_results = await asyncio.gather(*tasks, return_exceptions=True)
        
        for i, (url, result) in enumerate(zip(urls, download_results)):
            filename = extract_filename(url, f"image_{i}.jpg")
            path = os.path.join(save_path, filename)
            if isinstance(result, Exception):
                logger.error(f"图片下载异常: {path} - {str(result)}")
                logger.debug(traceback.format_exc())
                if os.path.exists(path):
                    os.remove(path)
                results[url] = False
            else:
                results[url] = path
    
    return results

def copyToClipboard(self, text):
    from PySide6.QtCore import Qt
    from PySide6.QtWidgets import QApplication
    from qfluentwidgets import InfoBar, InfoBarPosition
    logger.debug(f"复制到粘贴板: {text}")
    QApplication.clipboard().setText(str(text))
    InfoBar.success(title='复制成功', content=f"分隔符 {text} 已复制到粘贴板", orient=Qt.Horizontal,
                isClosable=True,   # enable close button
                position=InfoBarPosition.BOTTOM_RIGHT,
                duration=3000, 
                parent=self
            )
    
def get_internal_dir() -> str:
    if getattr(sys, 'frozen', False):
        base = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
        if base.rstrip(os.path.sep).endswith("_internal"):
            return base
        
        if hasattr(sys, '_MEIPASS'):
            # 单文件模式：_internal在_MEIxxxx下
            return os.path.join(base, '_internal')
        # 目录模式：_internal在sys._MEIPASS下
        return os.path.join(base, '_internal') if os.path.exists(os.path.join(base, '_internal')) else base
    else:
        return os.path.dirname(os.path.realpath(sys.argv[0]))

"""链接解析"""
def adaptive_link_splitter(text) -> List[str]:
    common_separators = ["\n", "\n\n", " ", "  ", "    ", ",  ", ", ", ",", ";", "|"]
    
    for sep in common_separators:
        if sep in text:
            links = text.split(sep)
            valid_links = [link.strip() for link in links if link.strip()]
            
            if len(valid_links) > 0 and sum(is_link_like(link) for link in valid_links) / len(valid_links) > 0.75:
                return valid_links
    
    return re.split(r"\s+", text)

def is_link_like(link):
    clean_link = link.strip()
    conditions = [
        clean_link.startswith(("http://", "https://", "ftp://", "www.")), 
        "." in clean_link,
        " " not in clean_link, 
        len(clean_link) >= 8 
    ]

    return sum(conditions) >= 3

"""base64解析"""
def adaptive_base64_extractor(text: str) -> Tuple[List[bytes], List[str]]:
    """
    :param text: 所有base64字符串
    :return: 解码后的二进制数据列表, 原始base64字符串列表
    """
    
    common_separators = ["\n", "\n\n", " ", "  ", "    ", ",  ", ", ", ",", ";", "|", "||", "::", ":", "\\", "/", "//"]
    for sep in common_separators:
        if sep in text:
            parts = text.split(sep)
            valid_parts = [part.strip() for part in parts if part.strip()]
            
            # 检查 Base64 比例
            base64_count = sum(is_base64_like(part) for part in valid_parts)
            if base64_count > 0 and base64_count / len(valid_parts) > 0.75:
                decoded_list = []
                encoded_list = []
                for part in valid_parts:
                    try:
                        decoded = base64.b64decode(part)
                        decoded_list.append(decoded)
                        encoded_list.append(part)
                    except:
                        pass
                return decoded_list, encoded_list
    
    base64_pattern = r'(?:[A-Za-z0-9+/]{4})*(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=)?'
    matches = re.findall(base64_pattern, text)
    valid_matches = [match for match in matches if is_base64_like(match)]
    
    decoded_list = []
    encoded_list = []
    for match in valid_matches:
        try:
            decoded = base64.b64decode(match)
            decoded_list.append(decoded)
            encoded_list.append(match)
        except:
            pass
    
    return decoded_list, encoded_list

def is_base64_like(s: str) -> bool:
    if len(s) < 4 or len(s) % 4 != 0:
        return False
    
    # 字符集检查
    valid_chars = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=")
    if not all(char in valid_chars for char in s):
        return False
    
    # 填充检查 ( = < 2 )
    if s.endswith('='):
        if s.count('=') > 2 or s[-1] != '=' or (len(s) > 1 and s[-2] == '=' and s[-1] != '='):
            return False
    
    try:
        base64.b64decode(s)
        return True
    except:
        return False
    
    
def _restart_program(self):
    try:
        BatchWindows = QDialog()
        ui1 = Reloading_Dialog.Ui_Form()
        ui1.setupUi(BatchWindows)
        BatchWindows.show()
        
        # 获取当前执行命令
        if getattr(sys, 'frozen', False):
            executable = sys.executable
            args = []
        else:
            executable = sys.executable
            args = sys.argv
        
        if sys.platform == 'win32':
            if ' ' in executable and not executable.startswith('"'):
                executable = f'"{executable}"'
        
        command = [executable] + (args if not getattr(sys, 'frozen', False) else [])
        # logger.info(f"即将重启: {' '.join(command)}")
        logger.info(f"即将重启: {executable} {args}")
        
        # if sys.platform == 'win32':
        #     subprocess.Popen(['start', '""'] + command, shell=True)
        #     os.startfile(os.path.dirname(executable), args)
        #     os.execv
        # else:
        os.execv(executable, args)
        
        QTimer.singleShot(100, self.window().close)
        
    except Exception as e:
        logger.error(f"重启失败: {str(e)}")
        logger.debug(traceback.format_exc())
        QTimer.singleShot(0, self.window().show)
        
def restart_program(self):
    new_args = []
    if getattr(sys, 'frozen', False):
        executable_path = sys.executable
        command = [executable_path] + new_args
        os.popen(f"start \"{executable_path}\"")
    else:
        python_executable = sys.executable
        script_path = os.path.abspath(__file__)
        command = [python_executable, script_path] + new_args
        # subprocess.Popen(command)
        os.popen(f"start \"{python_executable}\" \"{script_path}\"")

    QTimer.singleShot(1000, self.window().close)
    quit()
    
def SetBackground(self, new_wall: str, is_dark_theme: bool, theme_color, target=None, no_window="false"):
    if platform.system() == "Windows":
        exe = os.path.join(os.getcwd(), "set_wallpaper", "Set_Wallpaper.exe")
        if os.path.exists(exe):
            exe = os.path.abspath("set_wallpaper/Set_Wallpaper.exe")
            bg_color = '#1E1E1E' if is_dark_theme else '#FFFFFF'
            theme_mode = 'dark' if is_dark_theme else 'light'
            args = [exe, new_wall, bg_color, theme_color, theme_mode, no_window]
            
            logger.debug(f"壁纸设置命令: {subprocess.list2cmdline(args)}")
            process = subprocess.run(args)
            if process.returncode == 0:
                if target is not None:
                    Flyout.create(
                        icon=InfoBarIcon.SUCCESS,
                        title=f'壁纸已设置 o(*≧▽≦)ツ',
                        content=os.path.basename(new_wall),
                        target=target,
                        parent=self,
                        isClosable=True)
            else:
                raise Exception(process.returncode)
        else:
            raise FileNotFoundError("壁纸设置工具不存在，未能找到 Set_Wallpaper.exe 。")
    elif platform.system() == "Linux":
        try:
            new_wall = new_wall.rstrip("/").strip("\\").strip("\"")
            desktop_env = os.getenv("XDG_CURRENT_DESKTOP", "").lower()
            logger.debug(f"桌面环境: {desktop_env}, 壁纸路径: {new_wall}")
            if "gnome" in desktop_env or "ubuntu" in desktop_env:
                subprocess.run(["gsettings", "set", "org.gnome.desktop.background", "picture-uri", f"file://{new_wall}"])
            elif "mate" in desktop_env:
                subprocess.run(["gsettings", "set", "org.mate.background", "picture-filename", f"{new_wall}"])
            elif "kde" in desktop_env:
                subprocess.run(["dcop", "kdesktop", "org.kde.image", "/Picture", "setWallpaper", f"{new_wall}"])
            else:
                raise NotImplementedError("壁纸设置功能目前仅适用于 GNOME 桌面和Windows 系统。")
        except Exception as e:
            logger.error(f"壁纸设置失败: {str(e)}")
            logger.debug(traceback.format_exc())
            raise NotImplementedError("壁纸设置功能目前仅适用于 GNOME 桌面和Windows 系统。")
    else:
        logger.error(f"不适用于 {platform.system()}")
        raise NotImplementedError("壁纸设置功能目前仅适用于 GNOME 桌面和Windows 系统。")

"""TEST CODE"""
async def test_api() -> None:
    API = "https://api.lolicon.app/setu/v2?num=2"
    # 测试通配符路径
    r, _, _ = await request_api(
        api=API, 
        paths="data[*].tags", 
        method="GET"
    )
    print("通配符结果:")
    print(f"类型: {type(r)}")
    print(f"内容: {r}")
    
if __name__ == '__main__':
    from APIKernal import *
    from Logger import logger
    # asyncio.run(test_api())
    a = adaptive_link_splitter('''https://tc.alcy.cc/i/2024/04/21/6624165a9656f.webp
https://tc.alcy.cc/i/2024/04/21/6624166753e54.webp
https://tc.alcy.cc/i/2024/04/21/6624169c089a9.webp
https://tc.alcy.cc/i/2024/04/21/6624167686925.webp
https://tc.alcy.cc/i/2024/04/21/66241674c8cfe.webp
https://tc.alcy.cc/i/2024/04/21/662416457b85a.webp
https://tc.alcy.cc/i/2024/05/24/66505ff4caca8.webp
https://tc.alcy.cc/i/2024/05/24/66505ffaccd14.webp
https://tc.alcy.cc/i/2024/04/21/6624166841615.webp
https://tc.alcy.cc/i/2024/04/21/66241666764fd.webp
https://tc.alcy.cc/i/2024/04/21/6624166eb8088.webp
https://tc.alcy.cc/i/2024/05/24/66505ff463d2d.webp
https://tc.alcy.cc/i/2024/04/21/66241657062d6.webp
https://tc.alcy.cc/i/2024/04/21/6624165de22e1.webp
https://tc.alcy.cc/i/2024/04/21/662416571a459.webp
https://tc.alcy.cc/i/2024/05/24/66505ffcb5132.webp
https://tc.alcy.cc/i/2024/04/21/6624165ead099.webp
https://tc.alcy.cc/i/2024/04/21/662416501c0fb.webp
https://tc.alcy.cc/i/2024/05/24/66505ff165a43.webp
https://tc.alcy.cc/i/2024/04/21/6624165488abd.webp''')
    print(a, len(a))
else:
    from Kernel.APIKernal import *
    from Kernel.Logger import logger