"""
PROJECT:    APIKernal - The request, parsing and batch parsing of the API are all completed in one step.
MODULE:     APIKernal.py
FUNCTION:   APIKernal is a module that encapsulates the request, parsing and batch parsing of the API.
AUTHOR:     SRInternet
DATE:       2025-06
VERSION:    1.0.0 (see Releases Notes)

DEPENDENCIES:
  - aiohttp
  - asyncio

NOTES:
  This module is compatible with Python 3.8+
"""

import aiohttp
import asyncio
from typing import Any, Dict, List, Optional, Union, Tuple
import json
import re
from urllib.parse import quote, urlencode

try:
    from Kernel.Logger import logger
except ImportError:
    from Logger import logger

def construct_api(api: str, payload: Optional[Dict[str, Any]] = None, split_str: Optional[Dict[str, str]] = None):
    """构造请求的URL和参数
    
    :param api: API端点URL
    :param payload: 请求负载(对于POST/PUT等)
    :param split_str: 对于是列表类型的请求负载，如果是 GET 方法，则将列表中的每个值用此字符连接（缺省为 '|'）"""
    
    payload = payload or {}
    split_str = split_str or {}
    url = api.rstrip('/').rstrip('?')
    none_params = []
    other_params = {}
    
    # 分离None键和其他参数
    for key, value in payload.items():
        if key is None:
            none_params.append(str(value))
        else:
            s = split_str.get(key, '|')
                
            if isinstance(value, list):
                other_params[key] = s.join(str(v) for v in value)
            else:
                other_params[key] = value
    
    # 构建最终URL
    if none_params:
        url += '/' + '/'.join(quote(v, safe='') for v in none_params)
    if other_params:
        url += ('&' if '?' in url else '?') + urlencode(other_params, doseq=True)
    
    logger.debug(f"构建的请求URL: {url}")
    return url
                
# 请求函数
async def request_api(
    api: str,
    paths: Optional[Union[str, List[str]]] = None,
    method: str = "GET",
    headers: Optional[Dict[str, str]] = None,
    payload: Optional[Dict[str, Any]] = None,
    split_str: Optional[Dict[str, str]] = None,
    timeout: Union[int, float] = 15,
    raw: bool = False,
    ssl_verify: bool = True,
    *,
    body_type: str = "json",
    body: Any = None,
    return_status: bool = False,
    network_retries: int = 0,
    retry_delay_ms: int = 10000,
) -> Any:
    """
    异步执行API请求并解析响应数据
    
    :param api: API端点URL
    :param paths: 要解析的一个或多个路径
    :param method: HTTP方法 (GET, POST, etc.)
    :param headers: 请求头
    :param payload: 请求负载(对于POST/PUT等)
    :param split_str: 对于是列表类型的请求负载，如果是 GET 方法，则将列表中的每个值用此字符连接（缺省为 '|'）
    :param timeout: 超时时间(秒)
    :param raw: True = 返回原始数据，False = 返回按照 paths 解析后的数据
    :param ssl_verify: 是否验证SSL证书，设置为False可禁用SSL验证
    :return: 解析后的数据
    """
    headers = dict(headers or {})
    payload = payload or {}
    split_str = split_str or {}
    headers.setdefault("User-Agent", "WallpaperGenerator/6")
    request_body = payload if body is None else body
    
    try:
        # 如果禁用SSL验证，创建一个不验证SSL的ClientSession
        connector = aiohttp.TCPConnector(ssl=ssl_verify) if not ssl_verify else None
        if not ssl_verify:
            logger.warning(f"SSL 验证已被禁用，这可能会造成不安全的HTTPS连接！")
        # 使用 connect + sock_read 替代 total，避免大文件/图片下载到一半被总超时切断
        client_timeout = aiohttp.ClientTimeout(
            connect=min(10, timeout),
            sock_read=timeout
        )
        async with aiohttp.ClientSession(
            timeout=client_timeout,
            connector=connector
        ) as session:
            if method.upper() in ["GET", "HEAD"]:
                url = construct_api(api, payload, split_str)
                async with session.request(method, url, headers=headers) as response:
                    return await handle_response(response, paths, raw, return_status)
            else:
                kwargs = {}
                if body_type == "json":
                    kwargs["json"] = request_body
                elif body_type in ("form-data", "form_data", "x-www-form-urlencoded"):
                    kwargs["data"] = request_body
                    if body_type == "x-www-form-urlencoded":
                        headers.setdefault("Content-Type", "application/x-www-form-urlencoded")
                elif body_type == "raw":
                    kwargs["data"] = request_body
                else:
                    raise ValueError(f"不支持的 body_type: {body_type}")
                async with session.request(method, api, headers=headers, **kwargs) as response:
                    return await handle_response(response, paths, raw, return_status)
    except asyncio.TimeoutError:
        if network_retries > 0:
            await asyncio.sleep(max(0, retry_delay_ms) / 1000)
            return await request_api(api, paths, method, headers, payload, split_str,
                                     timeout, raw, ssl_verify, body_type=body_type, body=body,
                                     return_status=return_status, network_retries=network_retries - 1,
                                     retry_delay_ms=retry_delay_ms)
        raise RuntimeError(f"API请求超时: 超过 {timeout} 秒")
    except aiohttp.ClientError as e:
        if network_retries > 0:
            await asyncio.sleep(max(0, retry_delay_ms) / 1000)
            return await request_api(api, paths, method, headers, payload, split_str,
                                     timeout, raw, ssl_verify, body_type=body_type, body=body,
                                     return_status=return_status, network_retries=network_retries - 1,
                                     retry_delay_ms=retry_delay_ms)
        error_msg = f"API请求失败: {str(e)}"
        if hasattr(e, 'status') and e.status:
            error_msg += f" (状态码: {e.status})"
        raise RuntimeError(error_msg)

# 响应处理函数
async def handle_response(response: aiohttp.ClientResponse, paths: Optional[Union[str, List[str]]] = None, raw = False, return_status=False) -> Tuple[Any, ...]:
    """处理响应并返回解析后的数据（由 request_api 调用）"""

    # raw 模式直接读取二进制，避免 response.text() 消费响应体后 response.read() 为空
    if raw:
        binary_data = await response.read()
        content = ""
        try:
            content = binary_data.decode('utf-8')
        except UnicodeDecodeError:
            content = binary_data.decode('latin1')

        logger.debug(f"API返回状态码: {response.status} {response.reason}")
        logger.debug(f"API返回二进制大小: {len(binary_data)} bytes")
        if not response.ok and not return_status:
            error_msg = f"API返回错误: {response.status} {response.reason}"
            if content:
                error_msg += f"\n错误详情: {content[:200]}..."
            raise RuntimeError(error_msg)

        result = (response, content, binary_data)
        return (*result, response.status) if return_status else result

    try:
        content = await response.text()
    except UnicodeDecodeError:
        content = await response.text('latin1')

    logger.debug(f"API返回状态码: {response.status} {response.reason}")
    logger.debug(f"API返回内容: {content[:200]}...")
    if not response.ok and not return_status:
        error_msg = f"API返回错误: {response.status} {response.reason}"
        if content:
            error_msg += f"\n错误详情: {content[:200]}..."
        raise RuntimeError(error_msg)
    
    # 解析JSON
    try:
        data = json.loads(content)
    except json.JSONDecodeError:
        data = content
    
    if not paths:
        result = (data, None, None)
        return (*result, response.status) if return_status else result
    
    # 解析指定的路径
    result = (parse_response(data, paths), None, None)
    return (*result, response.status) if return_status else result

def parse_response(data: Any, paths: Union[str, List[str]]) -> Any:
    """
    解析响应数据
    
    :param data: 要解析的数据 (通常是dict或list)
    :param paths: 单个路径字符串或路径字符串列表
    :return: 解析结果，结果类型根据路径和数据类型决定
    """
    logger.debug(f"正在解析 paths: {paths}")
    # 核心：通过正则表达式，识别索引和切片语法
    index_pattern = re.compile(r'\[(.*?)\]')

    def resolve_path(obj: Any, parts: List[str]) -> Union[Any, List[Any]]:
        """递归解析路径：返回最自然的类型"""
        if not parts or obj is None:
            return obj
            
        current = parts[0]
        remaining = parts[1:]
        
        # 检查当前部分是否包含索引/切片语法
        match = index_pattern.search(current)
        if match:
            # 提取索引/切片表达式
            index_expr = match.group(1)
            # 获取字段名（索引前的部分）
            field = current[:match.start()].strip()
            
            # 如果字段名不为空，先访问该字段
            target_obj = obj
            if field:
                if isinstance(obj, dict) and field in obj:
                    target_obj = obj[field]
                elif isinstance(obj, (list, tuple)) and field.isdigit():
                    try:
                        target_obj = obj[int(field)]
                    except (ValueError, IndexError):
                        return None
            
            # 处理通配符 (*) 或索引/切片
            if index_expr == '*':
                # 通配符处理，展开所有元素
                if not isinstance(target_obj, (list, tuple)):
                    return None
                
                # 处理空数组，根据文档规范返回空列表
                if len(target_obj) == 0:
                    return []
                    
                results = []
                for item in target_obj:
                    result = resolve_path(item, remaining)
                    # 根据是否使用通配符决定结构
                    if '*' in current:  # 使用通配符时保持每个item的结构
                        results.append(result)
                    else:  # 非通配符情况扁平化
                        if isinstance(result, list):
                            results.extend(result)
                        else:
                            results.append(result)
                return results
            elif ':' in index_expr:
                # 切片处理
                if not isinstance(target_obj, (list, tuple)):
                    return None
                
                indices = index_expr.split(':')
                try:
                    # 支持负索引
                    start = int(indices[0]) if indices[0] else 0
                    end = int(indices[1]) if len(indices) > 1 and indices[1] else len(target_obj)
                    step = int(indices[2]) if len(indices) > 2 and indices[2] else 1
                    
                    results = []
                    for item in target_obj[start:end:step]:
                        result = resolve_path(item, remaining)
                        if isinstance(result, list):
                            results.extend(result)
                        else:
                            results.append(result)
                    return results
                except (ValueError, TypeError, IndexError):
                    return None
            else:
                # 单个索引处理
                try:
                    if not isinstance(target_obj, (list, tuple)):
                        return None
                    idx = int(index_expr)
                    return resolve_path(target_obj[idx], remaining)
                except (ValueError, TypeError, IndexError):
                    return None
                
        # 处理常规路径
        if isinstance(obj, dict) and current in obj:
            return resolve_path(obj[current], remaining)
            
        # 解析为数组索引
        if isinstance(obj, (list, tuple)) and current.isdigit():
            try:
                idx = int(current)
                return resolve_path(obj[idx], remaining)
            except (ValueError, IndexError):
                return None
            
        # 分割点路径
        if '.' in current:
            sub_paths = current.split('.')
            return resolve_path(obj, sub_paths + remaining)
            
        return None
    
    # 处理单个路径或路径列表
    if isinstance(paths, str):
        # 对于单个路径，返回最自然的类型
        path_parts = [part.strip() for part in paths.split('.') if part.strip()]
        result = resolve_path(data, path_parts)
        logger.debug(f"解析单个路径结果: {type(result).__name__}")
        return result
    else:
        # 对于多个路径，返回结果列表
        result = [resolve_path(data, [part.strip() for part in p.split('.') if part.strip()]) 
                for p in paths]
        logger.debug(f"解析多路径结果，长度: {len(result) if isinstance(result, list) else 'N/A'}")
        return result
