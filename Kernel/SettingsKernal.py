import os, sys, json, platform
import traceback, shutil
from UI.SettingsPage_ui import Ui_Form
from UI.AboutPage_ui import Ui_Dialog
from Kernel.Logger import logger
from Kernel import MainKernal
from PySide6.QtCore import Qt, QTime, QTimer
from PySide6.QtWidgets import QWidget, QDialog, QFileDialog
from PySide6.QtGui import QColor, QIcon
from qfluentwidgets import (InfoBarPosition, InfoBar, FluentIcon, ColorDialog, themeColor, Theme, EnumSerializer, 
                            PushSettingCard, ComboBoxSettingCard, OptionsSettingCard, SwitchSettingCard, RangeSettingCard, 
                            OptionsConfigItem, OptionsValidator, BoolValidator, RangeConfigItem, RangeValidator, qconfig)

class AppSettings():
    def __init__(self):
        self.app_name = "Wallpaper Generator"

class SettingsKernal():
    def Construct_control(self, path):
        api_json_files = []
        if not os.path.isdir(path):
            os.mkdir(path)
            logger.info(f"Created {path}")
            
        for file in os.listdir(path):
            full_path = os.path.join(path, file)
            logger.debug(f"Checking {full_path}")
            if os.path.isfile(full_path) and full_path.endswith('.api.json') and not file.startswith('_'):
                api_json_files.append(full_path)
        
        return api_json_files
    
    def read_settings(self):
        path = os.path.join(MainKernal.get_config_dir(), "config.json")
        if not os.path.isfile(os.path.join(MainKernal.get_config_dir(), 'BACKIMG1.png')):
            import shutil
            shutil.copyfile(os.path.join(MainKernal.get_internal_dir(), 'BACKIMG1.png'), os.path.join(MainKernal.get_config_dir(), 'BACKIMG1.png'))
            logger.debug(f"Copied {os.path.join(MainKernal.get_internal_dir(), 'BACKIMG1.png')} to {os.path.join(MainKernal.get_config_dir(), 'BACKIMG1.png')}")
            
        if not os.path.isdir(os.path.join(MainKernal.get_config_dir(), 'Images')):
            os.mkdir(os.path.join(MainKernal.get_config_dir(), 'Images'))
            logger.info(f"Created {os.path.join(MainKernal.get_config_dir(), 'Images')}")
            
        if not os.path.isfile(path):
            return {"download_path": os.path.join(MainKernal.get_config_dir(), 'Images'), "theme_config": "Auto", 
                    "ThemeMode": "AUTO", "background_image_path": os.path.join(MainKernal.get_config_dir(), 'BACKIMG1.png'), 
                    "today_image_config": True, "ssl_verify_config": True, "trayicon_config": True, "timeout_config": 30}
        
        with open(path, "r", encoding="utf-8") as f:
            settings = json.loads(f.read())
            f.close()

        return {"download_path": settings.get("download_path", os.path.join(MainKernal.get_config_dir(), 'Images')), 
                "theme_config": settings.get("theme_config", "Auto"), 
                "ThemeMode": settings.get("ThemeMode", "AUTO"), 
                "background_image_path": settings.get("background_image_path", os.path.join(MainKernal.get_config_dir(), 'BACKIMG1.png')), 
                "today_image_config": settings.get("today_image_config", True), 
                "ssl_verify_config": settings.get("ssl_verify_config", True), 
                "trayicon_config": settings.get("trayicon_config", True), 
                "timeout_config": settings.get("timeout_config", 30)}
    
    def read_autochange_settings(self):
        os.makedirs(os.path.join(MainKernal.get_config_dir(), "acw_next"), exist_ok=True)
        path = os.path.join(MainKernal.get_config_dir(), "acw_next", "config.json")
        if not os.path.isfile(path):
            return {"enabled": False, "interval": "01:00:00", 
                    "path": os.path.join(MainKernal.get_config_dir(), 'Images'), "auto_start": False}
        
        with open(path, "r", encoding="utf-8") as f:
            settings = json.loads(f.read())
            f.close()
            
        return {"enabled": settings.get("enabled", False), 
                "interval": settings.get("interval", "01:00:00"), 
                "path": settings.get("path", os.path.join(MainKernal.get_config_dir(), 'Images')), 
                "auto_start": settings.get("auto_start", False)} # 剔除多余的设置项
    
class SettingsUI(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        
        self.parent = parent
        self.settings = SettingsKernal.read_settings(self)
        self.init_ui()
            
    def init_ui(self):
        """初始化所有设置卡"""
        self.AboutButton.clicked.connect(self.on_show_about)
        self.SaveSettings.clicked.connect(self.save_settings)
        
        self.path_card = PushSettingCard(
            text="选择文件夹",
            icon=FluentIcon.DOWNLOAD,
            title="图片保存目录",
            content=self.settings["download_path"] if os.path.isdir(self.settings["download_path"]) else os.path.join(MainKernal.get_config_dir(), 'Images'),
        )
        self.path_card.clicked.connect(self.on_choose_path)

        theme_config = OptionsConfigItem("SettingsUI", "theme_config", "Auto", OptionsValidator(["Auto", "Custom"]))
        self.theme_card = ComboBoxSettingCard(
            configItem=theme_config,
            icon=FluentIcon.PALETTE,
            title="强调色",
            content="调整应用要突出显示的颜色" if self.settings["theme_config"] == "Auto" else "调整应用要突出显示的颜色。当前已选择颜色 " + self.settings["theme_config"],
            texts=["跟随系统", "自定义"]
        )
        logger.debug(f"theme_config: {self.theme_card.optionToText}")
        qconfig.load(os.path.join(MainKernal.get_config_dir(), 'config/config.json'), theme_config)
        self.theme_card.setValue("Auto" if self.settings["theme_config"] == "Auto" else "Custom")
        theme_config.valueChanged.connect(lambda option: self.on_change_color(option))
        
        themeMode = OptionsConfigItem(
        "QFluentWidgets", "ThemeMode", Theme.LIGHT, OptionsValidator(Theme), EnumSerializer(Theme), restart=True)
        self.dark_mode_card = OptionsSettingCard(
            themeMode,
            FluentIcon.BRUSH,
            "应用主题",
            "调整你的应用外观",
            texts=["浅色", "深色", "跟随系统设置"]
        )
        qconfig.load(os.path.join(MainKernal.get_config_dir(), 'config/config.json'), themeMode)
        self.dark_mode_card.setValue(getattr(Theme, self.settings["ThemeMode"].upper(), Theme.AUTO))
        themeMode.valueChanged.connect(lambda option: self.settings.update({'ThemeMode': option.value}))
        
        self.backrgound_card = PushSettingCard(
            text="选择背景图片",
            icon=FluentIcon.BACKGROUND_FILL,
            title="默认背景图片",
            content=self.settings["background_image_path"] if os.path.isfile(self.settings["background_image_path"]) else os.path.join(MainKernal.get_config_dir(), 'BACKIMG1.png'),
        )
        self.backrgound_card.clicked.connect(self.on_choose_background)
        
        timeout_config = RangeConfigItem("SettingsUI", "timeout_config", 30, RangeValidator(15, 180))
        self.timeout_card = RangeSettingCard(
            configItem=timeout_config,
            icon=FluentIcon.ROTATE,
            title="超时时间",
            content="生成图片所需要的最长时间，超过这个时间即为失败。单位为秒"
        )
        self.timeout_card.setValue(self.settings["timeout_config"])
        timeout_config.valueChanged.connect(lambda time: self.settings.update({'timeout_config': time}))
        
        ssl_verify_config = OptionsConfigItem("SettingsUI", "ssl_verify_config", True, BoolValidator())
        self.ssl_verify_card = SwitchSettingCard(
            icon=FluentIcon.VPN,
            title="启用SSL验证",
            content="启用后，会验证下载的图片是否为安全的HTTPS图片",
            configItem=ssl_verify_config
        )
        self.ssl_verify_card.setValue(self.settings["ssl_verify_config"])
        ssl_verify_config.valueChanged.connect(lambda option: self.settings.update({'ssl_verify_config': option}))
        
        today_image_config = OptionsConfigItem("SettingsUI", "today_image_config", True, BoolValidator())
        self.today_image_card = SwitchSettingCard(
            icon=FluentIcon.TRANSPARENT,
            title="启用每日一图",
            content="每天都会更新背景图片，视觉体验更好。暂不支持自动清理每日一图",
            configItem=today_image_config
        )
        self.today_image_card.setValue(self.settings["today_image_config"])
        today_image_config.valueChanged.connect(lambda option: self.settings.update({'today_image_config': option}))

        trayicon_config = OptionsConfigItem("SettingsUI", "trayicon_config", True, BoolValidator())
        self.trayicon_card = SwitchSettingCard(
            icon=FluentIcon.ZOOM,
            title="最小化到托盘",
            content="关闭窗口后不立即退出，而是在托盘图标中继续运行",
            configItem=trayicon_config
        )
        self.trayicon_card.setValue(self.settings["trayicon_config"])
        trayicon_config.valueChanged.connect(lambda option: self.settings.update({'trayicon_config': option}))
        
        settings_cards = [self.path_card, self.theme_card, self.dark_mode_card, self.backrgound_card, self.timeout_card, self.ssl_verify_card, self.today_image_card, self.trayicon_card]
        for card in settings_cards:
            self.verticalLayout_5.addWidget(card)
            
        self.verticalLayout_5.addItem(self.cardSpacer)
        self.verticalLayout_5.addItem(self.verticalSpacer_23)
        # QApplication.processEvents()
        
    def on_choose_color(self):
        def __onColorChanged(color: QColor):
            if color: 
                self.theme_card.setContent("调整应用要突出显示的颜色。当前已选择颜色 " + color.name())
                self.settings.update({'theme_config': color.name()})
            
        w = ColorDialog(themeColor(), "选择强调色", self.window())
        w.colorChanged.connect(__onColorChanged)
        w.exec()
        
    def on_show_about(self):
        dialog = QDialog()
        dialog.setWindowIcon(QIcon(".\\NewIcon.ico"))
        dialog.setFixedSize(dialog.size())
        ui = Ui_Dialog()
        ui.setupUi(dialog)
        dialog.exec()
        
    def on_change_color(self, option):
        if option == "Custom":
            self.on_choose_color() 
        else:
            self.theme_card.setContent("调整应用要突出显示的颜色")
            self.settings.update({'theme_config': option})
        
    def on_choose_path(self):
        new_path = QFileDialog.getExistingDirectory(
        self, '生成的图片将会保存在：', self.settings["download_path"] if os.path.isdir(self.settings["download_path"]) else os.path.join(MainKernal.get_config_dir(), 'Images'))
        if new_path:
            self.settings.update({'download_path': new_path})
            self.path_card.setContent(new_path)
            
    def on_choose_background(self):
        new_path = QFileDialog.getOpenFileName(
        self, '选择背景图片', self.settings["background_image_path"] if os.path.isfile(self.settings["background_image_path"]) else os.path.join(MainKernal.get_config_dir(), 'BACKIMG1.png'),
        "Image files (*.jpg *.png *.jpeg)")[0]
        if new_path:
            try:
                if not os.path.samefile(new_path, os.path.join(MainKernal.get_config_dir(), "BACKIMG1.png")): shutil.copy(new_path, os.path.join(MainKernal.get_config_dir(), "BACKIMG1.png"))
                self.settings.update({'background_image_path': new_path})
                self.backrgound_card.setContent(new_path)
            except Exception as e:
                logger.error(f"默认背景图片更新失败：{e}")
                logger.debug(traceback.format_exc())
                InfoBar.error(title='更新失败', content=f"默认背景图更新失败：{e}", orient=Qt.Horizontal,
                        isClosable=True,
                        position=InfoBarPosition.BOTTOM_RIGHT,
                        duration=4000, 
                        parent=self.window())
            
    def save_settings(self):
        self.SaveSettings.setEnabled(False)
        try:
            with open(os.path.join(MainKernal.get_config_dir(), "config.json"), "w", encoding="utf-8") as f:
                f.write(json.dumps(self.settings, indent=4))
                f.close()
                
            InfoBar.success(title='保存成功', content=f"设置已保存，将会立即生效", orient=Qt.Horizontal,
                    isClosable=True,
                    position=InfoBarPosition.BOTTOM_RIGHT,
                    duration=4000, 
                    parent=self.window())
            
            self.parent.settings_updated.emit()
        except Exception as e:
            logger.error(f"保存设置失败：{e}")
            logger.debug(traceback.format_exc())
            InfoBar.error(title='保存失败', content=f"保存设置失败：{e}", orient=Qt.Horizontal,
                    isClosable=True,
                    position=InfoBarPosition.BOTTOM_RIGHT,
                    duration=4000, 
                    parent=self.window())
        finally:
            QTimer.singleShot(100, lambda: self.SaveSettings.setEnabled(True))