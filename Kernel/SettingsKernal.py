import os, sys, json, platform
import traceback, shutil
from UI.SettingsPage_ui import Ui_Form
from UI.AboutPage_ui import Ui_Dialog
from Kernel.Logger import logger
from PySide6.QtCore import Qt, QTime, QTimer
from PySide6.QtWidgets import QWidget, QDialog, QFileDialog
from PySide6.QtGui import QColor, QIcon
from qfluentwidgets import (InfoBarPosition, InfoBar, FluentIcon, ColorDialog, themeColor, Theme, EnumSerializer, 
                            PushSettingCard, ComboBoxSettingCard, OptionsSettingCard, SwitchSettingCard, 
                            OptionsConfigItem, OptionsValidator, BoolValidator, qconfig, isDarkThemeMode)

class AppSettings():
    def __init__(self):
        self.app_name = "Wallpaper Generator"

class SettingsKernal():
    def Construct_control(self, path):
        api_json_files = []
        for file in os.listdir(path):
            full_path = os.path.join(path, file)
            logger.debug(f"Checking {full_path}")
            if os.path.isfile(full_path) and full_path.endswith('.api.json') and not file.startswith('_'):
                api_json_files.append(full_path)
        
        return api_json_files
    
    def read_settings(self):
        path = os.path.join(os.getcwd(), "config.json")
        if not os.path.isfile(path):
            return {"download_path": os.path.abspath('./Images'), "theme_config": "Auto", 
                    "ThemeMode": "AUTO", "background_image_path": os.path.abspath('./BACKIMG1.png'), 
                    "today_image_config": True}
        
        with open(path, "r", encoding="utf-8") as f:
            settings = json.loads(f.read())
            f.close()

        return {"download_path": settings.get("download_path", os.path.abspath('./Images')), 
                "theme_config": settings.get("theme_config", "Auto"), 
                "ThemeMode": settings.get("ThemeMode", "AUTO"), 
                "background_image_path": settings.get("background_image_path", os.path.abspath('./BACKIMG1.png')), 
                "today_image_config": settings.get("today_image_config", True)}
    
    def read_autochange_settings(self):
        path = os.path.join(os.getcwd(), "acw_next", "config.json")
        if not os.path.isfile(path):
            return {"enabled": False, "interval": "01:00:00", 
                    "path": os.path.abspath("./Images"), "auto_start": False}
        
        with open(path, "r", encoding="utf-8") as f:
            settings = json.loads(f.read())
            f.close()
            
        return {"enabled": settings.get("enabled", False), 
                "interval": settings.get("interval", "01:00:00"), 
                "path": settings.get("path", os.path.abspath("./Images")), 
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
            content=self.settings["download_path"] if os.path.isdir(self.settings["download_path"]) else os.path.abspath('./Images'),
        )
        self.path_card.clicked.connect(self.on_choose_path)

        theme_config = OptionsConfigItem("SettingsUI", "theme_config", "Auto", OptionsValidator(["Auto", "Custom"]))
        self.theme_card = ComboBoxSettingCard(
            configItem=theme_config,
            icon=FluentIcon.PALETTE,
            title="强调色" if platform.system() == "Windows" else "强调色（仅在 Windows 下可设置）",
            content="调整应用要突出显示的颜色" if self.settings["theme_config"] == "Auto" else "调整应用要突出显示的颜色。当前已选择颜色 " + self.settings["theme_config"],
            texts=["跟随系统", "自定义"]
        )
        logger.debug(f"theme_config: {self.theme_card.optionToText}")
        self.theme_card.setValue("Auto" if self.settings["theme_config"] == "Auto" else "Custom")
        theme_config.valueChanged.connect(lambda option: self.on_change_color(option))
        self.theme_card.setEnabled(platform.system() == "Windows")
        
        themeMode = OptionsConfigItem(
        "QFluentWidgets", "ThemeMode", Theme.LIGHT, OptionsValidator(Theme), EnumSerializer(Theme), restart=True)
        self.dark_mode_card = OptionsSettingCard(
            themeMode,
            FluentIcon.BRUSH,
            "应用主题",
            "调整你的应用外观",
            texts=["浅色", "深色", "跟随系统设置"]
        )
        self.dark_mode_card.setValue(getattr(Theme, self.settings["ThemeMode"].upper(), Theme.AUTO))
        themeMode.valueChanged.connect(lambda option: self.settings.update({'ThemeMode': option.value}))
        
        self.backrgound_card = PushSettingCard(
            text="选择背景图片",
            icon=FluentIcon.BACKGROUND_FILL,
            title="默认背景图片",
            content=self.settings["background_image_path"] if os.path.isfile(self.settings["background_image_path"]) else os.path.abspath('./BACKIMG1.png'),
        )
        self.backrgound_card.clicked.connect(self.on_choose_background)
        
        today_image_config = OptionsConfigItem("SettingsUI", "today_image_config", True, BoolValidator())
        self.today_image_card = SwitchSettingCard(
            icon=FluentIcon.TRANSPARENT,
            title="启用每日一图",
            content="每天都会更新背景图片，视觉体验更好。暂不支持自动清理每日一图",
            configItem=today_image_config
        )
        self.today_image_card.setValue(self.settings["today_image_config"])
        today_image_config.valueChanged.connect(lambda option: self.settings.update({'today_image_config': option}))
        
        settings_cards = [self.path_card, self.theme_card, self.dark_mode_card, self.backrgound_card, self.today_image_card]
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
        self, '生成的图片将会保存在：', self.settings["download_path"] if os.path.isdir(self.settings["download_path"]) else os.path.abspath('./Images'))
        if new_path:
            self.settings.update({'download_path': new_path})
            self.path_card.setContent(new_path)
            
    def on_choose_background(self):
        new_path = QFileDialog.getOpenFileName(
        self, '选择背景图片', self.settings["background_image_path"] if os.path.isfile(self.settings["background_image_path"]) else os.path.abspath('./BACKIMG1.png'),
        "Image files (*.jpg *.png *.jpeg)")[0]
        if new_path:
            try:
                if not os.path.samefile(new_path, os.path.join(os.getcwd(), "BACKIMG1.png")): shutil.copy(new_path, os.path.join(os.getcwd(), "BACKIMG1.png"))
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
            with open(os.path.join(os.getcwd(), "config.json"), "w", encoding="utf-8") as f:
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