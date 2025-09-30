from Kernel.Logger import logger
import asyncio
import subprocess, portalocker
import sys, random, base64, traceback, gc
import platform, json, webbrowser
from PySide6.QtCore import (QCoreApplication, QSize, Qt, Signal, QTimer)
from PySide6.QtGui import (QBrush, QColor, QIcon, QPainter, 
    QPalette, QPixmap, QImage, QImageReader, QImageIOHandler)
from PySide6.QtWidgets import (QApplication, 
    QWidget, QMessageBox, QDialog, QVBoxLayout)
from fonts.font_loader import load_fonts
from qasync import QEventLoop
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from qfluentwidgets import (SplashScreen, FluentIcon, Flyout, FlyoutViewBase, InfoBar, InfoBarPosition, 
                            InfoBarIcon, setTheme, setThemeColor, isDarkTheme, Theme, Action, ToolTipFilter, themeColor, 
                            FluentTranslator, HorizontalFlipView, CommandBarView, FlyoutAnimationType, PrimaryPushSettingCard)
from qfluentwidgets import MessageBox as OriginalMessageBox

app = QApplication(sys.argv)
load_fonts()

from APICORE import APICORE
from UI import MainWindowTemplate_ui, PageTemplate_ui, WelcomePageNext_ui
from UI.Controls import *
from acw_next import AutoChageWallpaper
from Kernel import MainKernal, SettingsKernal, APIKernal, MarketKernal, TrayIconKernal
from Kernel.OsKernal import os

from Exception_Handler import setup_global_exception_handler
handler = setup_global_exception_handler(
    log_file=os.path.join(MainKernal.get_config_dir(), "errors.log"), 
    console_output=True,
    exit_on_error=False, 
    custom_handler=lambda exc_type, exc_value, traceback: MainKernal.show_dialog(
        "发生异常", 
        f"由于发生未定义的 {exc_type.__name__} 异常，已将详细错误信息记录到程序根目录的 {os.path.join(MainKernal.get_config_dir(), 'errors.log')} 日志文件中，请联系并将此文件发送给开发者。", 
        "好", 
        "取消", 
        "False", 
        isDarkTheme()
    )
)

os.makedirs(os.path.join(MainKernal.get_config_dir(), "DaliyImages"), exist_ok=True)
daliy_img_path = os.path.join(MainKernal.get_config_dir(), "DaliyImages", f"{datetime.now().strftime('%Y-%m-%d')}.jpg")
# 继承 QApplication
class Application(QApplication):
    def notify(self, receiver, event):
        try:
            return super().notify(receiver, event)
        except Exception as e:
            print(f"Unhandled exception: {e}")
            QMessageBox.critical(None, "Error", f"An unhandled exception occurred: {e}")
            return True 
        
# 继承 Flyout
class FlowTip(Flyout):
    def __init__(self, view: FlyoutViewBase, parent=None, isDeleteOnClose=True):
        super().__init__(view, parent, isDeleteOnClose)
        self.view.setStyleSheet("background: transparent;\n"
"border: none;")

class MessageBox(OriginalMessageBox):
    def __init__(self, title, content, parent=None):
        w = OriginalMessageBox(title, content, parent)
        # if isDarkTheme():
        #     w.setStyleSheet("background-color: rgb(30, 30, 30);\n") # 对于无法深色的主题，使用深色背景
        self.r = w.exec()
        
class WelcomePage(QWidget, WelcomePageNext_ui.Ui_Form):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.main_window: QWidget = parent  # 保存MainWindow引用
        self.setupUi(self)
        self.IconWidget.setIcon(FluentIcon.MARKET)
        self.IconWidget_2.setIcon(FluentIcon.SPEED_OFF)
        self.IconWidget_3.setIcon(FluentIcon.CODE)
        self.TodayQuote.installEventFilter(ToolTipFilter(self.TodayQuote))
        self.PrimaryPushButton.clicked.connect(self.on_autowallpaper_clicked)
        self.PushButton_2.clicked.connect(self.on_gradient_clicked)
        self.PushButton.clicked.connect(lambda: webbrowser.open_new_tab("https://github.com/SRInternet-Studio/Wallpaper-generator/issues"))
        self.SubtitleLabel_7.clicked.connect(lambda: webbrowser.open_new_tab("https://github.com/SRInternet-Studio/Wallpaper-generator/releases"))
        self.loaded = False
        
    def showEvent(self, event): # 等界面完全加载完成后调用后端
        super().showEvent(event)
        if not self.loaded:
            self.loaded = True
            QTimer.singleShot(0, lambda: (
                asyncio.create_task(self.start_kernal(), name="start_kernal")
                if not check_task_exist("start_kernal")
                else None
            ))
            
    def on_image_clicked(self, file_name):
        target = self.ToadyCard
        self.CommandBar = CommandBarView(self)
        self.CommandBar.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        action = Action(FluentIcon.SYNC, "刷新今日图片", self)
        action.triggered.connect(lambda: asyncio.create_task(self.update_today_image(True), name="update_today_image"))
        self.CommandBar.addAction(action=action)
        
        action = Action(FluentIcon.COPY, "复制", self)
        action.triggered.connect(lambda: MainKernal.copyToClipboard(self.window(), QImage(os.path.realpath(file_name)))
                                 if os.path.isfile(os.path.realpath(file_name)) else 
                                 InfoBar.error(title='复制失败', content='图片已被移动或删除', orient=Qt.Horizontal, isClosable=True, 
                                                 position=InfoBarPosition.BOTTOM_RIGHT, duration=4000, parent=self
                                                ))
        self.CommandBar.addAction(action=action)
        
        action = Action(FluentIcon.IMAGE_EXPORT, "设为壁纸", self)
        action.triggered.connect(lambda: SetBackground(self, os.path.realpath(file_name), self.ToadyCard))
        self.CommandBar.addAction(action=action)

        action = Action(FluentIcon.FOLDER, "在资源管理器中打开", self)
        action.triggered.connect(lambda: subprocess.run(
            ['explorer', '/select,', os.path.realpath(file_name)] if platform.system() == "Windows" 
            else ['xdg-open', os.path.dirname(os.path.realpath(file_name))] if platform.system() == "Linux"
            else ['open', '-R', os.path.realpath(file_name)]
        ))
        self.CommandBar.addAction(action=action)
        
        action = Action(FluentIcon.EXPRESSIVE_INPUT_ENTRY, "喜欢我们", self)
        action.triggered.connect(lambda: webbrowser.open_new_tab("https://afdian.com/a/srinternet/"))
        self.CommandBar.addAction(action=action)

        self.CommandBar.resizeToSuitableWidth()
        Flyout.make(self.CommandBar, target, self,
                    FlyoutAnimationType.DROP_DOWN)
        
    def on_autowallpaper_clicked(self):
        if platform.system() != "Windows":
            MessageBox("环境问题", "自动更换壁纸 目前仅适用于 Windows 系统，请更换系统后重试。", self.window())
            return
        
        if hasattr(self.main_window, 'auto_wallpaper_window'):
            dialog: QDialog = self.main_window.auto_wallpaper_window
            dialog.setGeometry(self.window().geometry())
            dialog.setPalette(self.main_window.palette())

            self.window().hide()
            dialog.show()
            dialog.activateWindow()
            
            def on_finished():
                self.window().setGeometry(dialog.geometry())
                self.window().show()
                dialog.hide()
                
            dialog.finished.connect(on_finished)
            
    def on_gradient_clicked(self):
        if platform.system() != "Windows":
            MessageBox("环境问题", "制作渐变壁纸 目前仅适用于 Windows 系统，请更换系统后重试。", self.window())
            return
        
        if not MainKernal.is_process_running("Wallpaper_Gradient.exe"):
            os.startfile(os.path.join(MainKernal.get_internal_dir(), "gradient", "Wallpaper_Gradient.exe"))
        else:
            Flyout.create(
                icon=InfoBarIcon.SUCCESS,
                title=f'制作窗口已经打开',
                content="请勿重复运行 o(*￣▽￣*)ブ",
                target=self.PushButton_2,
                parent=self,
                isClosable=True,

            )
                
    async def start_kernal(self):
        self.ApplicationTitle.setText(QCoreApplication.translate("Form", 
                u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:700;\">\u58c1\u7eb8\u751f\u6210\u5668 5 NEXT</span></p><p><span style=\" font-size:18pt; font-weight:700;\">for " + platform.system() + "</span></p></body></html>", None))
        connection = await MainKernal.check_network()
        if connection:
            if float(f"{connection:.2f}") > 80:
                self.SubtitleLabel_4.setText(f"高达\n{connection:.2f} ms")
            else:
                self.SubtitleLabel_4.setText(f"低至\n{connection:.2f} ms")

            logger.info(f"网络连接成功，延迟：{connection:.2f}ms")
        else:
            self.ApplicationTitle.setText(QCoreApplication.translate("Form", 
                u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:700;\">\u58c1\u7eb8\u751f\u6210\u5668 5 NEXT（已离线）</span></p><p><span style=\" font-size:18pt; font-weight:700;\">for " + platform.system() + "</span></p></body></html>", None))
            self.SubtitleLabel_4.setText("无法连接\n请检查您的网络")
            self.SubtitleLabel_6.setText("无法连接\n请检查您的网络")
            
        if self.main_window.settings["today_image_config"]:
            await self.update_today_quote()
            await self.update_today_image()
            
        await self.update_fortune_text()
        logger.info("界面加载完成")
        
    async def update_fortune_text(self):
        logger.info("正在获取今日运势……")
        todayFortune = await MainKernal.TodayFortune()
        self.SubtitleLabel_2.setText(todayFortune)
        
    def update_apis_text(self, apis):
        """更新API数据统计文本"""
        # total_apis = sum(len(v) for v in apis.values())
        self.SubtitleLabel_6.setText(f"现已收录\n{apis['//summary']} 个接口")
        
    async def update_today_quote(self):
        logger.info("正在获取今日一言……")
        todayQuote = await MainKernal.Hitokota()
        self.TodayQuote.setText(todayQuote)

    async def update_today_image(self, force_update=False):
        global daily_img_path
        logger.info("正在获取今日图片……")
        file_name = daliy_img_path
        if not os.path.exists(os.path.dirname(file_name)):
            try:
                os.makedirs(os.path.dirname(file_name))
            except Exception as e:
                logger.error(f"创建每日一图文件夹失败：{str(e)}")
                logger.debug(traceback.format_exc())
                self.main_window.trayIcon.show_notification("无法更新今日图片", str(e))
                return
            
        if os.path.exists(file_name) and not force_update:
            processed_path = os.path.normpath(file_name).replace('\\', '/')
            # self.PixmapLabel.setStyleSheet(f"image: url('{processed_path}');")
            if hasattr(self, 'main_window') and self.main_window:
                self.main_window.background_changed.emit(file_name)
                
            if self.ToadyCard.receivers("clicked()") < 1:
                self.ToadyCard.setCursor(Qt.CursorShape.PointingHandCursor)
                self.ToadyCard.clicked.disconnect()
                self.ToadyCard.clicked.connect(lambda: self.on_image_clicked(file_name))
            logger.debug(f"今日图片已成功获取")
            return
        
        try:
            # "https://bing.biturl.top/?resolution=UHD&format=json&index=0&mkt=zh-CN"
            if force_update:
                InfoBar.info(title='今日图片', content=f"正在刷新，请坐和放宽……", orient=Qt.Horizontal,
                    isClosable=True,
                    position=InfoBarPosition.BOTTOM_RIGHT,
                    duration=6000, 
                    parent=self.window()
                )
                
            url = await MainKernal._requests_api("https://t.alcy.cc/pc?json", "")
            logger.debug(f"今日图片地址：{url}")
            await MainKernal.download_images(
                url.strip(), 
                file_name
            )

            if os.path.exists(file_name):
                processed_path = os.path.normpath(file_name).replace('\\', '/')
                self.PixmapLabel.setStyleSheet(f"image: url('{processed_path}');")
                if hasattr(self, 'main_window') and self.main_window:
                    self.main_window.background_changed.emit(file_name)
                    
                if not force_update and self.ToadyCard.receivers("clicked()") < 1:
                    self.ToadyCard.setCursor(Qt.CursorShape.PointingHandCursor)
                    self.ToadyCard.clicked.disconnect()
                    self.ToadyCard.clicked.connect(lambda: self.on_image_clicked(file_name))
                InfoBar.success(title='今日图片', content=f"已成功刷新", orient=Qt.Horizontal,
                    isClosable=True,
                    position=InfoBarPosition.BOTTOM_RIGHT,
                    duration=3000, 
                    parent=self.window()
                )
        except:
            logger.error("获取今日图片失败")
            logger.debug(traceback.format_exc())
            InfoBar.error(title='今日图片', content=f"刷新失败，请检查网络连接", orient=Qt.Horizontal,
                    isClosable=True,
                    position=InfoBarPosition.BOTTOM_RIGHT,
                    duration=3000, 
                    parent=self.window()
                )

class PageTemplate(QWidget, PageTemplate_ui.Ui_Form): 
    def __init__(self, parent=None, config: APICORE=None):
        super().__init__(parent=parent)
        if not config:
            raise ValueError("config cannot be None")
        self.setupUi(self)
        self.parent = parent
        
        self.SmoothScrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.Images_Area.setAspectRatioMode(Qt.AspectRatioMode.KeepAspectRatio)
        self.Images_Area.setItemAlignment(
            Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignVCenter)
        self.Images_Area.setBorderRadius(5)
        self.Images_Area.setSpacing(5)
        #self.Images_Area.setFixedSize(self.Images_Area.size())
        
        self.Images_Indicator.setPageNumber(self.Images_Area.count())
        self.Images_Indicator.setSortingEnabled(True)
        self.Images_Switcher.setMaximum(self.Images_Area.count())
        self.Images_Area.currentIndexChanged.connect(self.on_page_switch)
        self.Images_Switcher.valueChanged.connect(self.on_page_switch)
        self.Images_Indicator.currentIndexChanged.connect(self.on_page_switch)
        self._syncing = False
        self._generated = []
        self._other_responses = []

        self.SubtitleLabel.setText(config.friendly_name())
        self.ProgressLine.setVisible(False)
        self.controls_row = 3

        # test
        # self.Images_Area.addImages([".\\BACKIMG1.png"])
        
        # 添加API参数选择控件
        control_classes = { # (Ui_Class, row_span, col_span)
            "integer": (integer, 1, 3),  
            "boolean": (boolean, 1, 3),
            "enum": (emum, 1, 3),
            "string": (string, 1, 3),
        }

        
        for param in config.parameters():
            name = str(param.get('type')).lower()
            if name in control_classes:
                if not bool(param.get('enable', True)):
                    continue
                
                ui_class, row_span, col_span = control_classes[name]
                widget = QWidget()
                ui = ui_class()
                ui.setupUi(widget)
                
                # 保存控件实例到 self，使用唯一标识符确保控件名称唯一
                param_identifier = param.get('name') or f"param_{config.parameters().index(param)}"
                setattr(self, f"{param_identifier}_{name}_widget", widget)
                setattr(self, f"{param_identifier}_{name}_ui", ui)

                match name:
                    case "integer": # 关联 integer 参数控件组的 Slider 和 Selector 的数值
                        ui = getattr(self, f"{param_identifier}_{name}_ui")
                        ui.NumberSlider.valueChanged.connect(lambda: ui.NumberSelector.setValue(ui.NumberSlider.value()))
                        ui.NumberSelector.valueChanged.connect(lambda: ui.NumberSlider.setValue(ui.NumberSelector.value()))
                        ui.Title.setText(f"{param.get('friendly_name')}")
                        ui.NumberSlider.setMinimum(param.get('min_value'))
                        ui.NumberSlider.setMaximum(param.get('max_value'))
                        ui.NumberSlider.setValue(param.get('value'))
                        ui.NumberSelector.setMinimum(param.get('min_value'))
                        ui.NumberSelector.setMaximum(param.get('max_value'))
                        ui.NumberSelector.setValue(param.get('value'))
                    case "boolean":
                        ui = getattr(self, f"{param_identifier}_{name}_ui")
                        ui.CheckBox.setText(param.get('friendly_name'))
                        ui.CheckBox.setChecked(bool(param.get('value')))
                    case "enum":
                        ui = getattr(self, f"{param_identifier}_{name}_ui")
                        ui.Title.setText(f"{param.get('friendly_name')}")
                        opts = param.get('friendly_value')
                        if opts != None:
                            if len(opts) == len(param.get('value')):
                                ui.Option.addItems(opts)
                                ui.Option.setCurrentIndex(0)
                            else:
                                logger.warning(f"参数 {param.get('name')} 的选项名称 (value) 与选项友好名称 (friendly_value) 数量不匹配 ({len(param.get('value'))} != {len(opts)}) ，请检查配置是否正确")
                                ui.Option.addItems(param.get('value'))
                                ui.Option.setCurrentIndex(0)
                        else:
                            ui.Option.addItems(param.get('value'))
                            ui.Option.setCurrentIndex(0)
                    case "string":
                        ui = getattr(self, f"{param_identifier}_{name}_ui")
                        ui.Title.setText(f"{param.get('friendly_name')}")
                        ui.TextEdit.setText(param.get('value'))

                self.verticalLayout_2.addWidget(widget)
                self.controls_row += 1
            elif name == "list":
                ui_class, row_span, col_span = control_classes["string"]
                widget = QWidget()
                ui = ui_class()
                ui.setupUi(widget)
                
                ui.Title.setText(f"{param.get('friendly_name')} （用 {str(param.get('split_str', '|'))} 分隔）")
                ui.Title.clicked.connect(lambda s=str(param.get('split_str', '|')): MainKernal.copyToClipboard(self.window(), s))
                ui.Title.setCursor(Qt.CursorShape.PointingHandCursor)
                ui.TextEdit.setText(str(param.get('split_str', '|')).join(param.get('value') if isinstance(param.get('value'), list) else list(param.get('value'))))
                
                param_identifier = param.get('name') or f"param_{config.parameters().index(param)}"
                setattr(self, f"{param_identifier}_list_widget", widget)
                setattr(self, f"{param_identifier}_list_ui", ui)

                self.verticalLayout_2.addWidget(widget)
                self.controls_row += 1
            else:
                print(f"Warning: {name} is not a valid control type.")

        fixed_controls = [
            (self.verticalSpacer_7, 1, 1),
            (self.verticalSpacer_8, 1, 1),
            (self.StartButton, 1, 3),
            (self.verticalSpacer_21, 1, 1),
            (self.PushButton, 1, 1),
            (self.verticalSpacer_22, 1, 1),
            (self.ProgressLine, 1, 3),
            (self.verticalSpacer_9, 1, 1),
        ]

        for control, row_span, col_span in fixed_controls:
            if isinstance(control, QWidget):
                self.verticalLayout_2.addWidget(control)
            else:
                self.verticalLayout_2.addItem(control)
            self.controls_row += 1

        self.PushButton.clicked.connect(lambda: self.on_push_button_clicked(config))
        self.StartButton.clicked.connect(lambda: self.on_start_button_clicked(config))
        self.Images_Area.clicked.connect(self.on_image_clicked)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.Images_Area.setItemSize(self.Images_Area.size())
        logger.debug("窗口大小改变")

    def showEvent(self, event): 
        super().showEvent(event)
        self.Images_Area.setItemSize(self.Images_Area.size())

    def build_payload(self, config: APICORE, friendly_name: bool=False):
        """构建API请求的payload参数
        
        Args:
            config (APICORE): API配置
            friendly_name (bool, optional): 是不是给用户看的请求参数 (默认 False)"""
            
        payload = {}
        for param in config.parameters():
            param_type = str(param.get('type')).lower()
            param_name = param.get('name', None)
            if not param_name:
                param_name = None
            if friendly_name:
                _param_name = param.get('friendly_name', str(param_name))
            
            if not bool(param.get('enable', True)) and not friendly_name:
                payload[param_name] = param.get('value')
                
            elif hasattr(self, f"{param_name or f'param_{config.parameters().index(param)}'}_{param_type}_ui"):
                ui = getattr(self, f"{param_name or f'param_{config.parameters().index(param)}'}_{param_type}_ui")
                
                match param_type:
                    case "integer":
                        value = ui.NumberSelector.value()
                    case "boolean":
                        checkbox_value = ui.CheckBox.isChecked()
                        if friendly_name:
                            value = "是" if checkbox_value else "否"
                        else:
                            value = str(checkbox_value).lower()
                    case "string":
                        value = ui.TextEdit.toPlainText()
                    case "enum":
                        v: list = param.get('value') if not friendly_name else param.get('friendly_value')
                        logger.debug(f"{v} 在第 {ui.Option.currentIndex()} 的索引")
                        value = v[ui.Option.currentIndex()]
                    case "list":
                        split_str = param.get('split_str', '|')
                        text = ui.TextEdit.toPlainText()
                        value = text.split(split_str) if text else []
                        if friendly_name: value = "，".join(value)
                    case _:
                        value = None
                
                if value is not None:
                    if value or bool(param.get('required', False)):
                        payload[param_name if not friendly_name else _param_name] = value
                        
            else:
                logger.exception(f"构建参数时出错：未找到控件 {param_type} 无法读取值，可能会造成请求失败")
        
        return payload
    
    def on_push_button_clicked(self, cfg: APICORE):
        auto_config = {}
        split_str = {}
        for param in cfg.parameters():
            for key, value in param.items():
                if key == "split_str" and value:
                    split_str[key] = str(value)
                    break
        
        logger.debug(f"请求参数为列表的分隔符映射: {split_str}")
        payload = self.build_payload(cfg)
        payload_friendly = self.build_payload(cfg, True)
        logger.debug(f"构建的请求参数: {payload}")
        url = APIKernal.construct_api(cfg.link(), payload, split_str) if cfg.func().upper() in ["GET", "HEAD"] else cfg.link()
        auto_config = {"friendly_name": cfg.friendly_name(), 
            "intro": "Auto Change Wallpaper Config",  # 用于校验
            "icon": cfg.icon(),
            "link": url,
            "func": cfg.func(), 
            "APICORE_version": "1.0",
            "parameters": [{
                "name": "payload", 
                "value": payload, 
            }],
            "response": {
                "image": cfg.response().image()
            }
        }
        
        friendly_params = [
            {"friendly_name": k, "value": v}
            for k, v in payload_friendly.items()
        ]
        logger.debug(f"友好请求参数: {friendly_params}")
        auto_config["parameters"] = [
            auto_config["parameters"][0],
            *friendly_params 
        ]
        
        try:
            if not os.path.exists(os.path.join(MainKernal.get_config_dir(), "EnterPoint", "acw_config")):
                os.makedirs(os.path.join(MainKernal.get_config_dir(), "EnterPoint", "acw_config"))
                
            with open(os.path.join(MainKernal.get_config_dir(), "EnterPoint", "acw_config", "_AutoConfig.api.json"), "w", encoding="utf-8") as f:
                json.dump(auto_config, f, indent=2, ensure_ascii=False)
                
        except Exception as e:
            logger.error(f"保存配置文件失败: {str(e)}")
            logger.debug(traceback.format_exc())
            Flyout.create(
                icon=InfoBarIcon.SUCCESS,
                title="保存配置文件失败",
                content=f"无法写入文件，请检查权限或文件路径是否正确。",
                target=self.StartButton,
                parent=self,
                isClosable=True,
            )
            return
            
        self.parent.auto_wallpaper_updated.emit()
        Flyout.create(
                icon=InfoBarIcon.SUCCESS,
                title=cfg.friendly_name(),
                content=f"已成功设为自动更换壁纸的配置文件 (～￣▽￣)～",
                target=self.StartButton,
                parent=self,
                isClosable=True,
            )

    def on_start_button_clicked(self, cfg: APICORE):
        try:
            self.StartButton.setEnabled(False)
            self.ProgressLine.setVisible(True)
            Flyout.create(
                icon=InfoBarIcon.INFORMATION,
                title=cfg.friendly_name(),
                content=f"开始生成啦，请耐心等待( •̀ ω •́ )✧",
                target=self.StartButton,
                parent=self,
                isClosable=True,
            )
            
            # 构建请求参数
            QApplication.processEvents()
            payload = self.build_payload(cfg)
            logger.debug(f"构建的请求参数: {payload}")
            logger.info(f"开始: {cfg.friendly_name()} 模式生成...")
            
            # 创建异步任务
            asyncio.create_task(self.on_api_start(cfg, payload))
            
        except ValueError as e:
            logger.error(f"参数验证失败: {str(e)}")
            logger.debug(traceback.format_exc())
            self.ProgressLine.setVisible(False)
            MessageBox("参数错误", f"参数验证失败: {str(e)}", self.window())
            self.StartButton.setEnabled(True)
            self.StartButton.setText(QCoreApplication.translate("MainWindow", u"生成", None))
            
        except Exception as e:
            logger.error(f"生成过程中发生错误: {str(e)}")
            logger.debug(traceback.format_exc())
            self.ProgressLine.setVisible(False)
            MessageBox("错误", f"生成过程中发生错误: {str(e)}", self.window())
            self.StartButton.setEnabled(True)
            self.StartButton.setText(QCoreApplication.translate("MainWindow", u"生成", None))
    
    async def on_api_start(self, cfg: APICORE, payload: dict):
        try:
            self._generated = []
            self._other_responses = []
            split_str = {}
            if not os.path.isdir(self.parent.settings["download_path"]):
                raise FileNotFoundError("设置的图片保存位置无法被使用，请前往设置进行更换")
            
            for param in cfg.parameters():
                for key, value in param.items():
                    if key == "split_str" and value:
                        split_str[key] = str(value)
                        break
            
            gc.collect()
            logger.debug(f"请求参数为列表的分隔符映射: {split_str}")
            binary_phrase = (str(cfg.response().image().get('content_type', "URL")).upper() == "BINARY")
            r, t, c = await APIKernal.request_api(
                cfg.link(),
                "",
                cfg.func(), 
                payload=payload,
                timeout=int(self.parent.settings["timeout_config"]),
                split_str=split_str, 
                raw=binary_phrase, 
                ssl_verify=self.parent.settings["ssl_verify_config"],
            )
            
            # 逻辑最复杂的部分，解析响应
            result, response = None, []
            if binary_phrase: # 二进制
                if not cfg.response().image().get('is_base64', False): # 不是base64编码的单/多图片
                    response = await MainKernal.phrase_binary_images(r, t, c)
                    # logger.debug(f"二进制图片提取格式化: {response}")
                else: # base64编码的单/多图片
                    path = str(cfg.response().image().get('path', ''))
                    if not path:
                        raise ValueError("API 配置文件中返回结果中缺少图片路径")
                        
                    if isinstance(r, str): # 纯文本的 base64 图片
                        response = MainKernal.adaptive_base64_extractor(str(r))
                    elif isinstance(r, list):
                        response = MainKernal.adaptive_base64_extractor("\n".join(r))
                    elif not cfg.response().image().get('is_list', True): # 不在列表里的 base64 图片
                        response = MainKernal.adaptive_base64_extractor(APIKernal.parse_response(r, path))
                    else:
                        response = APIKernal.parse_response(r, path)
                        response[:] = [base64.b64decode(str(item)).decode('utf-8') for item in response]
                        
                self.StartButton.setText(QCoreApplication.translate("MainWindow", f"生成 (预计生成 {len(response)} 张)", None))
                result = await MainKernal.download_images_binary(
                    response, 
                    self.parent.settings["download_path"],
                )
                    
            else: # URL
                logger.info(f"结果返回: {str(r)} {type(r)}")
                path = str(cfg.response().image().get('path', ''))
                if not path:
                    raise ValueError("API 配置文件中返回结果中缺少图片路径")
                
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
                        
                self.StartButton.setText(QCoreApplication.translate("MainWindow", f"生成 (预计生成 {len(response)} 张)", None))
                result = await MainKernal.download_images(
                    response,
                    self.parent.settings["download_path"],
                    retries=1,
                    timeout=int(self.parent.settings["timeout_config"])
                )

            # 其他响应
            if len(cfg.response().others()) > 0:
                for other in cfg.response().others():
                    name = other.get('friendly_name', '')
                    data = other.get('data', [])
                    if not name or not data or len(data) == 0:
                        continue

                    field = {name: {}}
                    for d in data:
                        if not bool(d.get('one-to-one-mapping', True)):
                            field[name].update({f"{d['friendly_name']}-no-one-to-one-mapping": APIKernal.parse_response(r, d['path'])})
                        else:
                            content = APIKernal.parse_response(r, d['path'])
                            if isinstance(content, list) and len(content) == len(response):
                                # result中所有False值都代表图片下载失败，需要从content中删除
                                false_indices = []
                                for idx, url in enumerate(response):
                                    if url in result and result[url] is False:
                                        false_indices.append(idx)
                                
                                for idx in sorted(false_indices, reverse=True):
                                    if idx < len(content):
                                        del content[idx]
                                        
                            field[name].update({d['friendly_name']: content})

                    self._other_responses.append(field)

            logger.debug(f"其他响应: {self._other_responses}")
            
            # 在主线程中完成操作
            QTimer.singleShot(0, lambda: self.on_api_complete(
                True,
                f"{cfg.friendly_name()} 生成成功",
                result if result else {},
                response, 
                cfg
            ))
            
        except Exception as e:
            # progress_timer.stop()
            logger.error(f"API请求失败: {str(e)}")
            logger.debug(traceback.format_exc())
            
            try:
                error_str = str(e)
            except Exception:
                error_str = repr(e)
            QTimer.singleShot(0, lambda: self.on_api_complete(
                False, 
                error_str,  
                {}, 
                [], 
                cfg
            ))
    
    def on_api_complete(self, success, message, response: dict, links: list, cfg: APICORE):
        logger.debug(f"API请求完成，成功: {success}, 信息: {message}, 结果: {response}")
        for k, v in response.items():
            if v is not False:
                if v == True:
                    self._generated.append(k)
                else:
                    self._generated.append(v)
                
        gc.collect()
        if success and len(self._generated) > 0:
            logger.info(message)
            self.Images_Area.clear()
            for path in self._generated:
                reader = QImageReader(path)
                if reader.size().width() > 4096 or reader.size().height() > 4096:
                    reader.setScaledSize(reader.size().scaled(2048, 2048, Qt.AspectRatioMode.KeepAspectRatio))
                
                image = reader.read()
                if image.isNull():
                    self.Images_Area.addImage(path)
                    continue
                
                self.Images_Area.addImage(image)
                
            self.Images_Area.setCursor(Qt.CursorShape.PointingHandCursor)
            self.Images_Indicator.setPageNumber(self.Images_Area.count())
            self.Images_Switcher.setMaximum(self.Images_Area.count())
            self.Images_Switcher.setValue(self.Images_Area.currentIndex() + 1)
            self.Images_Switcher.setMinimum(1)
            self.Images_Indicator.setCurrentIndex(self.Images_Area.currentIndex())
        
            Flyout.create(
                    icon=InfoBarIcon.SUCCESS,
                    title=f'已生成',
                    content=f"{len(self._generated)} 张图片生成完毕！在设置的保存路径中找到它们吧 ο(=•ω＜=)ρ⌒☆",
                    target=self.StartButton,
                    parent=self,
                    isClosable=True,
                )
        else:
            logger.error(message)
            self.Images_Area.clear()
            self.Images_Indicator.setPageNumber(0)
            self.Images_Switcher.setMaximum(0)
            self.Images_Switcher.setValue(0)
            
            Flyout.create(
                    icon=InfoBarIcon.ERROR,
                    title=f'没有图片生成',
                    content=message,
                    target=self.StartButton,
                    parent=self,
                    isClosable=True,
                )
            
        self.ProgressLine.setVisible(False)
        self.StartButton.setEnabled(True)
        self.StartButton.setText(QCoreApplication.translate("MainWindow", u"生成", None))

    def on_page_switch(self, value):
        if self._syncing:
            return
        
        self._syncing = True  # 设置同步锁
        
        try:
            sender = self.sender() # 获取触发该函数的来源
            if sender == self.Images_Indicator:
                new_index = value
            elif sender == self.Images_Area:
                new_index = value
            elif sender == self.Images_Switcher:
                new_index = value - 1
            else:
                return
                
            if sender != self.Images_Switcher:
                self.Images_Switcher.setValue(new_index + 1)
                
            if sender != self.Images_Indicator:
                self.Images_Indicator.setCurrentIndex(new_index)
                
            if sender != self.Images_Area:
                self.Images_Area.setCurrentIndex(new_index)
                
        finally:
            self._syncing = False

    def on_image_clicked(self):
        if not isinstance(self.sender(), HorizontalFlipView) or len(self._generated) == 0:
            return
    
        target: HorizontalFlipView = self.sender()
        self.CommandBar = CommandBarView(self)
        self.CommandBar.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        action = Action(FluentIcon.PHOTO, os.path.basename(
            self._generated[self.Images_Area.currentIndex()]), self)
        action.triggered.connect(lambda: os.startfile(
            self._generated[self.Images_Area.currentIndex()]))
        self.CommandBar.addAction(action=action)
        
        action = Action(FluentIcon.COPY, "复制", self)
        action.triggered.connect(lambda: MainKernal.copyToClipboard(self.window(), QImage(os.path.realpath(self._generated[self.Images_Area.currentIndex()])))
                                 if os.path.isfile(os.path.realpath(self._generated[self.Images_Area.currentIndex()])) else 
                                 InfoBar.error(title='复制失败', content='图片已被移动或删除', orient=Qt.Horizontal, isClosable=True, 
                                                 position=InfoBarPosition.BOTTOM_RIGHT, duration=4000, parent=self
                                                ))
        self.CommandBar.addAction(action=action)

        # 格式化响应数据
        if self._other_responses:
            current_index = self.Images_Area.currentIndex()
            for response in self._other_responses:
                formatted = {}
                for key, value in response.items():
                    if isinstance(value, dict):
                        formatted[key] = {}
                        for k, v in value.items():
                            if str(k).endswith("-no-one-to-one-mapping"):
                                k = k.replace("-no-one-to-one-mapping", "")
                                formatted[key][k] = ", ".join(str(item) for item in v) if isinstance(v, list) else v
                                logger.debug(f"{k}: 非一对一映射")
                            elif isinstance(v, list) and len(v) > current_index and len(v) == len(self._generated):
                                formatted[key][k] = v[current_index]
                            else:
                                formatted[key][k] = ", ".join(str(item) for item in v) if isinstance(v, list) else v
                    else:
                        formatted[key] = value

                formatted_key, formatted_value = list(formatted.items())[0]
                action = Action(FluentIcon.TAG, formatted_key, self)
                action.triggered.connect(lambda _, fk=formatted_key, fv=formatted_value: self.show_background_tools(fk, fv))
                self.CommandBar.addAction(action=action)
                logger.debug(f"当前其他响应: {formatted}")

        action = Action(FluentIcon.IMAGE_EXPORT, "设为壁纸", self)
        action.triggered.connect(lambda: SetBackground(self, '"{}"'.format(self._generated[self.Images_Area.currentIndex()]), self.Images_Area))
        self.CommandBar.addAction(action=action)

        action = Action(FluentIcon.FOLDER, "在资源管理器中打开", self)
        # action.triggered.connect(lambda file_name=os.path.realpath(self._generated[self.Images_Area.currentIndex()]): subprocess.run(
        #     ['explorer', '/select,', file_name] if platform.system() == "Windows" 
        #     else ['xdg-open', os.path.dirname(file_name)] if platform.system() == "Linux"
        #     else ['open', '-R', file_name]
        # ))
        action.triggered.connect(lambda: (
            platform.system() == "Windows" and subprocess.run([
                'explorer', f'/select,{os.path.realpath(self._generated[self.Images_Area.currentIndex()])}'
            ])) or
            (platform.system() == "Darwin" and subprocess.run([
                'open', '-R', os.path.realpath(self._generated[self.Images_Area.currentIndex()])
            ])) or
            subprocess.run([
                'xdg-open', os.path.dirname(os.path.realpath(self._generated[self.Images_Area.currentIndex()]))
            ])
        )
        # action.triggered.connect(lambda: subprocess.run([
        #     'explorer',
        #     '/select,',
        #     os.path.realpath(self._generated[self.Images_Area.currentIndex()])
        # ]))
        self.CommandBar.addAction(action=action)

        self.CommandBar.resizeToSuitableWidth()
        Flyout.make(self.CommandBar, target, self,
                    FlyoutAnimationType.DROP_DOWN)
        
    def show_background_tools(self, title, content):
        if isinstance(content, dict):
            result_string = ''.join(['{}: {}\n'.format(key, value) for key, value in content.items()])
        else:
            result_string = str(content)
            
        result = MainKernal.show_dialog(title, result_string, "好", "取消", "True", isDarkTheme())
        print(result)

        if result != "T":
            pass

class MainWindow(QWidget, MainWindowTemplate_ui.Ui_Form):
    background_changed = Signal(str)  # 背景更改信号
    apis_updated = Signal(dict)  # API数据更新信号
    switch_page = Signal(str)  # 切换页面信号
    settings_updated = Signal()  # 设置更新信号
    auto_wallpaper_updated = Signal() # 自动更换壁纸更新信号
    force_wallpaper_update = Signal() # 强制更换壁纸更新信号
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.background_changed.connect(self.change_background)
        self.switch_page.connect(self.switch_page_to)
        
        global daliy_img_path
        self.setupUi(self)
        self.setWindowIcon(QIcon(".\\NewIcon.ico"))
        self.setWindowTitle("壁纸生成器 5 NEXT")
        self.settings_updated.connect(self.update_window_style)
        self.update_window_style()
        
        # 1. 创建启动页面
        self.splashScreen = SplashScreen(self.windowIcon(), self)
        self.splashScreen.setIconSize(QSize(128, 128))

        # 2. 在创建其他子页面前先显示主界面
        logger.debug(f"启动参数: {sys.argv}")
        if not (SettingsKernal.SettingsKernal.read_autochange_settings(self)["auto_start"] and "--AutoStartup" in sys.argv):
            self.show()
            
        self.widgets = {}
        self.first_page = WelcomePage(self)
        self.addSubInterface(self.first_page, "welcome", "欢迎")

        # 3. 加载API配置
        exclude_apis = self.preparSubInterface()
        cfgs = SettingsKernal.SettingsKernal.Construct_control(SettingsKernal.SettingsKernal, path=os.path.join(MainKernal.get_config_dir(), "EnterPoint"))
        for i in range(len(cfgs)):
            path = str(cfgs[i])
            try:
                cfg = APICORE(path).init()
            except Exception as e:
                logger.error(f"API配置文件 {path} 加载失败: {str(e)}")
                logger.debug(traceback.format_exc())
                InfoBar.info(title='图片源加载失败', content=f"{str(e)}", orient=Qt.Horizontal,
                    isClosable=True,
                    position=InfoBarPosition.BOTTOM_RIGHT,
                    duration=6000, 
                    parent=self
                )
                continue
            
            if not os.path.basename(cfgs[i]) in exclude_apis:
                self.addSubInterface(PageTemplate(self, cfg), f"api_{os.path.basename(cfgs[i]).split('.')[0]}", cfg.friendly_name())

        self.addSubInterface(MarketKernal.MarketUI(self), "marketplace", "图片源市场")
        self.addSubInterface(SettingsKernal.SettingsUI(self), "settings", "设置")
        self.OpacityAniStackedWidget.setCurrentIndex(0)
        self.TopMenu.setCurrentItem(self.first_page.objectName())
        self.TopMenu.currentItemChanged.connect(
            lambda k:  self.OpacityAniStackedWidget.setCurrentWidget(self.OpacityAniStackedWidget.findChild(QWidget, k)))
         
        self.trayIcon = TrayIconKernal.Tray_Form(self)
        self.trayIcon.create_tray_icon()
        self.hide_firstly = True
        self.close_to_restart = False
        self.splashScreen.finish()
        
        self.init_autowallpaper()
        self.change_background()
        QTimer.singleShot(0, self.handle_autowallpaper)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.update_background()
        
    def showEvent(self, event):
        super().showEvent(event)
        self.settings: dict = SettingsKernal.SettingsKernal.read_settings(self)
        setTheme(getattr(Theme, self.settings["ThemeMode"].upper(), Theme.AUTO))
        
    def init_autowallpaper(self):
        if (not hasattr(self, 'auto_wallpaper_window') or self.auto_wallpaper_window is None) and platform.system() == "Windows":
            self.auto_wallpaper_window = QDialog(self.window())
            self.auto_wallpaper_window.setWindowTitle("自动更换壁纸 5 NEXT")
            self.auto_wallpaper_window.setWindowFlags(self.auto_wallpaper_window.windowFlags() | Qt.Window)
            self.auto_wallpaper_ui = AutoChageWallpaper.AutoChageWallpaper(self, self.auto_wallpaper_window)
            self.auto_wallpaper_window.setWindowModality(Qt.ApplicationModal)
            self.auto_wallpaper_updated.connect(self.auto_wallpaper_ui.auto_wallpaper_updated.emit)
            self.force_wallpaper_update.connect(self.auto_wallpaper_ui.force_wallpaper_update.emit)
            
            layout = QVBoxLayout(self.auto_wallpaper_window)
            layout.addWidget(self.auto_wallpaper_ui)
            layout.setContentsMargins(0, 0, 0, 0)
            self.auto_wallpaper_window.setLayout(layout)
            
            self.auto_wallpaper_window.setAttribute(Qt.WA_DeleteOnClose, False)
            self.auto_wallpaper_ui.init_timer()
    
    def handle_autowallpaper(self):
        if SettingsKernal.SettingsKernal.read_autochange_settings(self)["auto_start"] and "--AutoStartup" in sys.argv:
            if hasattr(self, 'auto_wallpaper_window') and self.auto_wallpaper_window is not None and platform.system() == "Windows":
                logger.info("启动开机自动更换")
                self.auto_wallpaper_ui.force_wallpaper_update.emit()
                self.hide()
            
    def update_window_style(self):
        self.settings: dict = SettingsKernal.SettingsKernal.read_settings(self)
        logger.debug(f"设置主题: {self.settings['ThemeMode'].upper()}, 颜色 {self.settings['theme_config']}")
        if self.settings["theme_config"].lower() != "auto":
            setThemeColor(self.settings["theme_config"])
        else:
            if platform.system() == "Windows":
                from winsdk.windows.ui.viewmanagement import UISettings, UIColorType
                accent_color = UISettings().get_color_value(UIColorType.ACCENT)
                if not themeColor() == QColor(accent_color.r, accent_color.g, accent_color.b):
                    setThemeColor(QColor(accent_color.r, accent_color.g, accent_color.b))
            else:
                setThemeColor(app.palette().highlight().color())
                
        
        setTheme(getattr(Theme, self.settings["ThemeMode"].upper(), Theme.AUTO))    
        if hasattr(self, 'first_page'): 
            if self.settings["today_image_config"]: asyncio.create_task(self.first_page.update_today_image())
            else:
                self.change_background()
        
    def preparSubInterface(self):
        if not os.path.exists(os.path.join(MainKernal.get_config_dir(), "EnterPoint")):
            os.mkdir(os.path.join(MainKernal.get_config_dir(), "EnterPoint"))
            
        exclude_apis = []
        if os.path.isfile(os.path.join(MainKernal.get_config_dir(), "EnterPoint", "exclude.txt")):
            with open(os.path.join(MainKernal.get_config_dir(), "EnterPoint", "exclude.txt"), "r", encoding="utf-8") as f:
                exclude_apis = [line.strip() for line in f.readlines()]
        logger.debug(f"排除的API: {exclude_apis}")
        return exclude_apis

    def addSubInterface(self, widget: QWidget, objectName: str, text, insert_index: int=-1):
        widget.setObjectName(objectName)
        self.widgets[objectName] = widget # if objectName.startswith("api_"): 
        if insert_index > -1:
            self.OpacityAniStackedWidget.insertWidget(insert_index, widget)
            self.TopMenu.insertItem(insert_index, routeKey=objectName, text=text)
        else:
            self.OpacityAniStackedWidget.addWidget(widget)
            self.TopMenu.addItem(routeKey=objectName, text=text)
            
        if isinstance(widget, WelcomePage):
            self.apis_updated.connect(widget.update_apis_text)
    
    def switch_page_to(self, page_name: str):
        match page_name:
            case "welcome":
                self.TopMenu.setCurrentItem(self.first_page.objectName())
                self.OpacityAniStackedWidget.setCurrentWidget(self.first_page)
            case "marketplace":
                self.TopMenu.setCurrentItem(self.widgets[page_name].objectName())
                self.OpacityAniStackedWidget.setCurrentWidget(self.widgets[page_name])
            case "settings":
                self.TopMenu.setCurrentItem(self.widgets[page_name].objectName())
                self.OpacityAniStackedWidget.setCurrentWidget(self.widgets[page_name])
            case _:
                logger.warning(f"未知页面: {page_name}")
                
        self.window().show()
        self.window().activateWindow()
        self.window().raise_()

    def _finalize(self):
        try:
            for timer in getattr(self, '_timers', []):
                timer.stop()
                
            loop = asyncio.get_event_loop()
            for task in asyncio.all_tasks(loop):
                if not task.done():
                    task.cancel()
                    
            if loop.is_running():
                loop.stop()
            
            for i in range(self.OpacityAniStackedWidget.count()):
                widget = self.OpacityAniStackedWidget.widget(i)
                if hasattr(widget, 'cleanup'):
                    widget.cleanup()
                    
            if hasattr(self, '_thread_pool'):
                self._thread_pool.shutdown(wait=False)
                
            return True
        except Exception as e:
            logger.error(f"Finalization error: {str(e)}")
            return False

    def on_close(self):
        self.hide_firstly = False
        if self._finalize():
            QTimer.singleShot(0, lambda: (
                QApplication.processEvents(),
                QApplication.quit()
            ))
        else:
            # Force quit if cleanup failed
            QApplication.quit()
            
    def closeEvent(self, event):
        if not self.close_to_restart:
            if self.settings["trayicon_config"]:
                event.ignore()
                self.window().hide()
                if self.hide_firstly:
                    self.hide_firstly = False
                    self.trayIcon.show_notification("壁纸生成器", "已隐藏到托盘，右键托盘可显示")
            else:
                self.on_close()
        else:
            super().closeEvent(event)

    def change_background(self, image_path=None):
        # 加载原始图片
        if image_path and os.path.exists(image_path):
            image_path = os.path.normpath(image_path).replace('\\', '/')
            self.first_page.PixmapLabel.setStyleSheet(f"image: url('{image_path}');")
            self.original_pixmap = QPixmap(image_path)
            logger.debug(f"加载自定义背景图片: {image_path}")
        else:
            normal_path = os.path.normpath(os.path.join(MainKernal.get_config_dir(), 'BACKIMG1.png')).replace('\\', '/')
            self.first_page.PixmapLabel.setStyleSheet(f"image: url('{normal_path}');")
            self.original_pixmap = QPixmap(normal_path)
            logger.debug("使用默认背景图片")
        
        logger.debug(f"isDarkTheme: {isDarkTheme()}")
        if not isDarkTheme():
            mask_color = QColor(255, 255, 255, 200) 
        else:
            mask_color = QColor(0, 0, 0, 200)
        
        # 创建临时绘图表面
        masked_pixmap = QPixmap(self.original_pixmap.size())
        masked_pixmap.fill(Qt.transparent)
        
        # 绘制带遮罩的图片
        painter = QPainter(masked_pixmap)
        painter.drawPixmap(0, 0, self.original_pixmap)
        painter.fillRect(masked_pixmap.rect(), mask_color)  # 添加遮罩层
        painter.end()
        
        # 缩放并设置背景
        self.pixmap = masked_pixmap  # 保存带遮罩的图片
        self.update_background()
        
    def update_background(self):
        if not hasattr(self, 'pixmap') or self.pixmap.isNull():
            return
        # 获取当前窗口的尺寸
        window_width = self.MainUI.width()
        window_height = self.MainUI.height()

        # 计算图像缩放比例
        pixmap_width = self.pixmap.width()
        pixmap_height = self.pixmap.height()

        scale_x = window_width / pixmap_width
        scale_y = window_height / pixmap_height

        # 选择使图像的短边适应窗口的比例
        scale = max(scale_x, scale_y)

        # 创建缩放后的图像
        scaled_pixmap = self.pixmap.scaled(
            pixmap_width * scale,
            pixmap_height * scale,
            Qt.AspectRatioMode.IgnoreAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )

        # 更新背景图像
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(scaled_pixmap))
        self.MainUI.setPalette(palette)
        
'''===全局方法==='''
def SetBackground(self, new_wall, target) -> None:
    try:
        MainKernal.SetBackground(self, new_wall, 
            isDarkTheme(), themeColor().name(), target)
    except FileNotFoundError as e:
        logger.exception(str(e))
        MessageBox("错误", "壁纸设置工具不存在，未能找到 Set_Wallpaper.exe\n壁纸生成器 可能已经损坏，重新安装本程序可能解决此问题。", self.window())
    except NotImplementedError as e:
        logger.exception(str(e))
        MessageBox("环境问题", "设置壁纸 功能目前仅适用于 GNOME、KDE、MATE、DDE、XFCE、Cinnamon 桌面和 Windows 系统，请更换系统后重试。", self.window())
    except Exception as e:
        logger.exception(str(e))
        Flyout.create(
                icon=InfoBarIcon.ERROR,
                title=f'壁纸设置失败 o(╥﹏╥)o',
                content=f"错误代码: {str(e)}",
                target=target,
                parent=self,
                isClosable=True)
        
def check_task_exist(task_name: str) -> bool:
    for task in asyncio.all_tasks():
        if task.get_name() == task_name:
            return not task.done()
        return False
        
def check_multiple_instances(lockfile='wallpaper_generator_next.app.lock') -> None:
    lockfile_path = os.path.join(os.environ.get('TEMP', '/tmp'), lockfile)
    try:
        lock = open(lockfile_path, 'w')
        portalocker.lock(lock, portalocker.LOCK_EX | portalocker.LOCK_NB)
    except (portalocker.AlreadyLocked, IOError):
        MainKernal.show_dialog(
            "无需启动", 
            f"壁纸生成器 NEXT 已在运行中，请勿重复启动。", 
            "好", 
            "取消", 
            "False", 
            isDarkTheme()
        )
        sys.exit(0)
    
    import atexit
    def cleanup():
        portalocker.unlock(lock)
        lock.close()
        try:
            os.unlink(lockfile_path)
        except:
            pass
    
    atexit.register(cleanup)

if __name__ == '__main__':
    QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    QApplication.setAttribute(Qt.ApplicationAttribute.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.ApplicationAttribute.AA_UseHighDpiPixmaps)
    QImageReader.setAllocationLimit(512)
    
    # 设置跟随系统主题和主题色
    setTheme(Theme.AUTO)
    if sys.platform == 'win32':
        from winsdk.windows.ui.viewmanagement import UISettings, UIColorType
        accent_color = UISettings().get_color_value(UIColorType.ACCENT)
        setThemeColor(QColor(accent_color.r, accent_color.g, accent_color.b))
    else:
        setThemeColor(app.palette().highlight().color())
    
    check_multiple_instances()
    os.chdir(MainKernal.get_internal_dir())
    
    # 启动程序
    event_loop = QEventLoop(app)
    asyncio.set_event_loop(event_loop)
    
    t = FluentTranslator()
    app.installTranslator(t)

    w = MainWindow()
    # w.show() # show() 转移到 MainWindow.__init__ 中处理
    
    with event_loop:
        event_loop.run_forever()

    sys.exit(app.exec())