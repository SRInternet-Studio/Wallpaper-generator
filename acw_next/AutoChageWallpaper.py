import ctypes
import traceback
from PySide6.QtCore import Qt, QTime, QTimer, Signal
from PySide6.QtWidgets import QWidget, QApplication, QFileDialog
from qfluentwidgets import PickerColumnFormatter, InfoBarPosition, InfoBar, isDarkTheme, themeColor
import sys, os, json, qasync, asyncio, random, base64

if __name__ == "__main__":
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UI.AutoChangingPage_ui import Ui_Form
from Kernel.SettingsKernal import SettingsKernal
from Kernel.Logger import logger
from Kernel.StartupManager import StartupManager
from Kernel import APIKernal, MainKernal
from APICORE import APICORE

class TimeFormatter(PickerColumnFormatter):
    """ Seconds formatter """
    def __init__(self, format_str):
        """:param format_str: str, 一个字符，表示时间单位，如 '时'"""
        super().__init__()
        self.format_str = format_str

    def encode(self, value):
        return str(value) + f" {self.format_str}"

    def decode(self, value: str):
        return int(value[:-1])

class AutoChageWallpaper(QWidget, Ui_Form):
    auto_wallpaper_updated = Signal()
    force_wallpaper_update = Signal()
    
    def __init__(self, parent=None, window=None):
        super().__init__(window)
        self.setupUi(self)
        self.parent = window
        self.parentWidget = parent
        
        self.settings: dict = SettingsKernal.read_autochange_settings(self)
        self.displayed = False
        self.payload = {}
        self.cfg = None
        self.last_value = self.TimeDial.value()
        self.auto_wallpaper_updated.connect(lambda: self.init_cfg(False))
        self.force_wallpaper_update.connect(lambda: self.on_time_changing(True))
                
        if getattr(sys, 'frozen', False):
            startup_args = "--AutoStartup"
        else:
            startup_args = f"'{os.path.abspath(__file__)}' --AutoStartup"
            
        self.startup_manager = StartupManager(f"'{sys.executable}'", startup_args, None if startup_args.startswith("--") else "WallpaperGenerator")
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("自动更换壁纸 5 NEXT")
        self.TimePicker.setColumnVisible(2, True)
        for i, label in enumerate(["时", "分", "秒"]):
            self.TimePicker.setColumnFormatter(i, TimeFormatter(label))
            
        self.TimeDial.valueChanged.connect(lambda value: self.on_dial_value_changed(value))
        self.TimeDial.setRange(0, 60)
        self.SaveSettings.clicked.connect(self.on_save_settings)
        self.CancelSettings.clicked.connect(self.on_close)
        self.ChosePath.clicked.connect(self.on_choose_path)
        self.AutoStartButton.setEnabled(self.settings["enabled"])
        self.init_settings()
        # self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        # self.setFixedSize(self.size())
        
    def init_settings(self):
        self.last_time = QTime.currentTime()
        self.next_time = self.add_time_to_current(self.settings["interval"])
        self.EnabilityButton.setChecked(self.settings["enabled"])
        self.TextPath.setText(self.settings["path"])
        self.AutoStartButton.setChecked(self.startup_manager.IsAddedToStartup()) # self.settings["auto_start"]
        self.TimePicker.setTime(QTime.fromString(self.settings["interval"], "hh:mm:ss"))
        
    def init_timer(self):
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.on_time_changing)
        if self.settings["enabled"]:
            self.timer.start(1000)
            self.init_cfg(False)
        else:
            self.timer.stop()
            self.CurrentStage.setText(" 下次更换：未启用。")
            
    def on_close(self):
        self.parent.close()
        
    def showEvent(self, event):
        super().showEvent(event)
        self.init_cfg()
        
    def init_cfg(self, show_error=True):
        path = os.path.join(os.getcwd(), "EnterPoint", "acw_config", "_AutoConfig.api.json")
        try:
            if os.path.isfile(path):
                cfg = APICORE(path).init()
                assert cfg.intro() == "Auto Change Wallpaper Config", "不是自动更换壁纸的配置文件占用了正确的文件名"
                
                self.description_text = ""
                self.SubtitleLabel_7.setText(f"当前配置：{cfg.friendly_name()}")
                for para in cfg.parameters():
                    if para.get("friendly_name", None):
                        self.description_text += f" {para['friendly_name']}：{para['value']}\n"
                    elif para.get("name", "") == "payload":
                        self.payload = para["value"]
                        
                self.cfg = cfg
            else:
                raise FileNotFoundError("没有自动更换壁纸的图片源配置。")
        except Exception as e:
            if show_error:
                self.description_text = "没有自动更换壁纸的图片源配置。"
                InfoBar.error(title='自动更换壁纸的配置加载失败', content=f"{str(e)}", orient=Qt.Horizontal,
                    isClosable=True,
                    position=InfoBarPosition.TOP_RIGHT,
                    duration=6000, 
                    parent=self
                )
            else:
                self.parentWidget.trayIcon.show_notification("自动更换壁纸的配置加载失败", str(e))
            logger.error(f"_AutoConfig {path} 加载失败: {str(e)}")
            logger.debug(traceback.format_exc())
                
        logger.debug(f"显示自动更换壁纸窗口，已刷新")
        self.displayed = True
        
    def closeEvent(self, event):
        super().closeEvent(event)
        self.displayed = False
        # if not __name__ == "__main__": self.window().show()
            
    def add_time_to_current(self, time_str: str) -> QTime:
        try:
            added_time = QTime.fromString(time_str, "hh:mm:ss")
            if not added_time.isValid() or (added_time.hour() == 0 and added_time.minute() < 1):
                logger.error("无效的时间格式或时间间隔小于 1 分钟，请重新修改时间")
                self.parentWidget.trayIcon.show_notification("自动更换壁纸 失败", "无效的时间格式或时间间隔小于 1 分钟，请重新修改时间")
                return self.add_time_to_current("00:05:00")
            
            current_time = self.last_time.addSecs(1) # 加 1 秒，避免立即更换
            total_secs = current_time.hour() * 3600 + current_time.minute() * 60 + current_time.second()
            added_secs = added_time.hour() * 3600 + added_time.minute() * 60 + added_time.second()
            total_secs += added_secs
    
            if total_secs >= 86400:
                total_secs %= 86400  # 86400秒=24小时，明天更换
                
            return QTime(0, 0).addSecs(total_secs)
        
        except Exception as e:
            logger.error(f"添加时间失败：{e}")
            logger.debug(traceback.format_exc())
            return self.add_time_to_current("00:05:00")
        
    def on_dial_value_changed(self, value):
        if value == self.last_value:
            return
        
        current_time = self.TimePicker.getTime()
        time_diff = value - self.last_value
        if time_diff > 0: # 增加时间
            if current_time.second() == 59:
                if current_time.minute() == 59:
                    if current_time.hour() == 23:
                        pass
                    else:
                        self.TimePicker.setTime(QTime(current_time.hour() + 1, 0, time_diff))
                else:
                    self.TimePicker.setTime(QTime(current_time.hour(), current_time.minute() + 1, time_diff))
            else:
                self.TimePicker.setTime(QTime(current_time.hour(), current_time.minute(), current_time.second() + time_diff))
        else: # 减少时间
            time_diff = abs(time_diff)
            if current_time.second() == 0:
                if current_time.minute() == 0:
                    if current_time.hour() == 0:
                        pass
                    else:
                        self.TimePicker.setTime(QTime(current_time.hour() - 1, 59, 59 - time_diff))
                else:
                    self.TimePicker.setTime(QTime(current_time.hour(), current_time.minute() - 1, 59 - time_diff))
            else:
                self.TimePicker.setTime(QTime(current_time.hour(), current_time.minute(), current_time.second() - time_diff))
            
        self.last_value = value
        
    def on_choose_path(self):
         new_path = QFileDialog.getExistingDirectory(
            self, '生成的图片将会保存在：', self.TextPath.text() if os.path.isdir(self.TextPath.text()) else self.settings["path"])
         if new_path:
             self.TextPath.setText(new_path)
        
    def on_save_settings(self):
        if __name__ == "__main__":
            return
        
        if not os.path.isdir(self.TextPath.text()):
            InfoBar.warning(title='路径无效', content=f"请重新选择图片的保存路径", orient=Qt.Horizontal,
                    isClosable=True,
                    position=InfoBarPosition.TOP_RIGHT,
                    duration=6000, 
                    parent=self)
            return
        
        user_time = self.TimePicker.getTime()
        if user_time.hour() == 0 and user_time.minute() < 1:
            InfoBar.warning(title='时间间隔过短', content=f"时间间隔不能小于 1 分钟，请重新设置", orient=Qt.Horizontal,
                    isClosable=True,
                    position=InfoBarPosition.TOP_RIGHT,
                    duration=6000, 
                    parent=self)
            return
        
        self.settings["enabled"] = self.EnabilityButton.isChecked()
        self.settings["path"] = self.TextPath.text()
        self.settings["interval"] = user_time.toString("hh:mm:ss")
        if not self.settings["enabled"]:
            self.AutoStartButton.setChecked(False)
            self.AutoStartButton.setEnabled(False)
        else:
            self.AutoStartButton.setEnabled(True)
        
        try:
            if self.AutoStartButton.isChecked(): 
                if not self.startup_manager.IsAddedToStartup():
                    self.startup_manager.AddToStartup()
            else:
                if self.startup_manager.IsAddedToStartup():
                    self.startup_manager.RemoveFromStartup()
                    
        except Exception as e:
            logger.error(f"设置开机启动失败：{e}")
            logger.debug(traceback.format_exc())
            InfoBar.error(title='开机启动设置失败', content=f"{str(e)}", orient=Qt.Horizontal,
                    isClosable=True,
                    position=InfoBarPosition.TOP_RIGHT,
                    duration=6000, 
                    parent=self)
        
        self.settings["auto_start"] = self.startup_manager.IsAddedToStartup()
        self.AutoStartButton.setChecked(self.startup_manager.IsAddedToStartup())
        with open(os.path.join(os.getcwd(), "acw_next", "config.json"), "w", encoding="utf-8") as f:
            f.write(json.dumps(self.settings, indent=4, ensure_ascii=False))
            f.close()
            
        self.init_settings()
        if not self.settings["enabled"]:
            self.timer.stop()
            self.CurrentStage.setText(" 下次更换：未启用。")
        else:
            if not self.timer.isActive():
                self.timer.start(1000)
            
        InfoBar.info(title='配置应用成功', content=f"将会立即生效", orient=Qt.Horizontal,
                    isClosable=True,
                    position=InfoBarPosition.TOP_RIGHT,
                    duration=6000, 
                    parent=self)
            
    def on_time_changing(self, force=False):
        now = QTime.currentTime()
        now_secs = now.hour() * 3600 + now.minute() * 60 + now.second() # 当日剩余时间的秒数
        seconds_left = self._count_seconds_left(now_secs)
        
        if seconds_left <= 0 or force:
            asyncio.set_event_loop(qasync.QEventLoop(self))
            asyncio.create_task(self.change_wallpaper())
            self.last_time = QTime.currentTime()
            self.next_time = self.add_time_to_current(self.settings["interval"])
            
            now_after = QTime.currentTime()
            now_after_secs = now_after.hour() * 3600 + now_after.minute() * 60 + now_after.second()
            seconds_left = self._count_seconds_left(now_after_secs)
            
        if self.settings["enabled"]:
            hours = seconds_left // 3600
            minutes = (seconds_left % 3600) // 60
            seconds = seconds_left % 60
            countdown = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
            
            # countdown = QTime(0, 0, 0).addSecs(abs(self.next_time.secsTo(QTime.currentTime()))).toString('hh:mm:ss')
            if self.displayed:
                self.CurrentStage.setText(f"{self.description_text}\n 下次更换：{countdown} 后 ({self.next_time.toString('hh:mm:ss')})")
        
    async def change_wallpaper(self):
        try:
            cfg: APICORE = self.cfg
            payload: dict = self.payload
            if not cfg:
                logger.error("没有配置的图片源")
                raise ValueError("没有配置自动更换壁纸的图片源。")
            
            binary_phrase = (str(cfg.response().image().get('content_type', "URL")).upper() == "BINARY")
            if cfg.func().upper() in ["GET", "HEAD"]:
                r, t, c = await APIKernal.request_api(
                    cfg.link(),
                    "",
                    cfg.func(),
                    timeout=random.randint(15, 30),
                    raw=binary_phrase
                )
            else:
                r, t, c = await APIKernal.request_api(
                    cfg.link(),
                    "",
                    cfg.func(), 
                    payload=payload,
                    timeout=random.randint(15, 30),
                    raw=binary_phrase
                )
            
            # 解析响应
            result, response = None, []
            if binary_phrase: # 二进制
                if not cfg.response().image().get('is_base64', False): # 不是base64编码的单/多图片
                    response = await MainKernal.phrase_binary_images(r, t, c)
                else: # base64编码的单/多图片
                    path = str(cfg.response().image().get('path', ''))
                    if not path:
                        raise ValueError("API 配置文件中返回结果中缺少图片路径。")
                        
                    if isinstance(r, str): # 纯文本的 base64 图片
                        response = MainKernal.adaptive_base64_extractor(str(r))
                    elif isinstance(r, list):
                        response = MainKernal.adaptive_base64_extractor("\n".join(r))
                    elif not cfg.response().image().get('is_list', True): # 不在列表里的 base64 图片
                        response = MainKernal.adaptive_base64_extractor(APIKernal.parse_response(r, path))
                    else:
                        response = APIKernal.parse_response(r, path)
                        response[:] = [base64.b64decode(str(item)).decode('utf-8') for item in response]
                        
                response = response[:1]
                result = await MainKernal.download_images_binary(
                    response, 
                    self.parentWidget.settings["download_path"],  # os.path.abspath(".//Images")
                )
                    
            else: # URL
                logger.info(f"结果返回: {str(r)} {type(r)}")
                path = str(cfg.response().image().get('path', ''))
                if not path:
                    raise ValueError("API 配置文件中返回结果中缺少图片路径。")
                
                if isinstance(r, str): # 纯文本的 URL
                    response = MainKernal.adaptive_link_splitter(str(r))
                    logger.debug(f"文本链接提取格式化: {response}")
                elif isinstance(r, list):
                    response = MainKernal.adaptive_link_splitter("\n".join(r))
                elif not cfg.response().image().get('is_list', True): # 不在列表里的URL
                    response = MainKernal.adaptive_link_splitter(APIKernal.parse_response(r, path))
                else:
                    response = APIKernal.parse_response(r, path)
                    
                if cfg.response().image().get('is_base64', False): # 用base64编码的URL
                    response[:] = [base64.b64decode(str(item)).decode('utf-8') for item in response]
                    
                response = response[:1]
                result = await MainKernal.download_images(
                    response,
                    self.parentWidget.settings["download_path"],  # os.path.abspath(".//Images")
                    retries=1,
                    timeout=30
                )
                
            new_wall: str = None
            for k, v in result.items():
                if v is not False:
                    if v == True:
                        new_wall = k
                    else:
                        new_wall = v
            
            if not new_wall or not os.path.isfile(new_wall):
                logger.debug(f"解析的响应: {response}")
                raise ValueError("没有壁纸成功生成。")
            
            try:
                try:
                    ctypes.windll.user32.SystemParametersInfoW(20, 0, new_wall, 3)
                except Exception as e:
                    logger.error(f"ctypes 设置壁纸失败: {e}")
                    logger.debug(traceback.format_exc())
                    MainKernal.SetBackground(self, 
                        new_wall, 
                        isDarkTheme(), themeColor().name(), no_window="true")
            except FileNotFoundError as e:
                logger.exception(str(e))
                raise
            except NotImplementedError:
                logger.exception(str(e))
                raise
            except Exception as e:
                logger.exception(str(e))
                raise Exception(f"错误代码: {str(e)}。")
            
        except Exception as e:
            logger.error(f"更换壁纸失败：{e}")
            logger.debug(traceback.format_exc())
            self.parentWidget.trayIcon.show_notification("自动更换壁纸 失败", f"{e} 请稍后再试。")
                
    def _count_seconds_left(self, now_secs: int) -> int:
        next_secs = self.next_time.hour() * 3600 + self.next_time.minute() * 60 + self.next_time.second() # 下一次更换的秒数
        
        if next_secs >= now_secs:
            seconds_left = next_secs - now_secs
        else:
            seconds_left = (86400 - now_secs) + next_secs # 明天更换
        return seconds_left
    
if __name__ == '__main__':
    app = QApplication()
    acw = AutoChageWallpaper()
    acw.show()
    sys.exit(app.exec())