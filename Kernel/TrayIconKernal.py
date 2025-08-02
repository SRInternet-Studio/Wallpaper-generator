import sys, platform
from PySide6.QtWidgets import (
    QApplication, QSystemTrayIcon, QMenu, QMainWindow, QVBoxLayout, 
    QWidget, QPushButton, QLabel, QMessageBox
)
from PySide6.QtGui import QIcon, QAction, QPixmap
from PySide6.QtCore import Qt, QTimer, Slot
from qfluentwidgets import SystemTrayMenu, ToolTipFilter, ToolTipPosition, Action

class Tray_Form():
    def __init__(self, parent: QWidget=None):
        super().__init__()
        self.parent = parent
        
    def _(self) -> None:
        pass

    def create_tray_icon(self):
        self.tray_icon = QSystemTrayIcon(self.parent)
        self.tray_icon.setIcon(QIcon(".\\NewIcon.ico"))
        self.tray_icon.setToolTip("壁纸生成器 5 NEXT")
        self.tray_icon.installEventFilter(ToolTipFilter(self.tray_icon))
        tray_menu = SystemTrayMenu("壁纸生成器 5 NEXT", self.parent)
        
        # 添加菜单项
        show_action = Action("显示主窗口", self.parent)
        show_action.triggered.connect(self.parent.window().show)
        tray_menu.addAction(show_action)
        
        # notify_action = QAction("自动更换壁纸", self)
        # notify_action.triggered.connect(self.show_notification)
        # tray_menu.addAction(notify_action)
        
        if sys.platform != "darwin": 
            tray_menu.addSeparator()
        
        welcome_action = Action("欢迎", self.parent)
        welcome_action.triggered.connect(lambda: self.parent.switch_page.emit("welcome"))
        tray_menu.addAction(welcome_action)
        
        marketplace_action = Action("图片源市场", self.parent)
        marketplace_action.triggered.connect(lambda: self.parent.switch_page.emit("marketplace"))
        tray_menu.addAction(marketplace_action)
        
        settings_action = Action("设置", self.parent)
        settings_action.triggered.connect(lambda: self.parent.switch_page.emit("settings"))
        tray_menu.addAction(settings_action)
        
        if sys.platform != "darwin": 
            tray_menu.addSeparator()
            
        awc_action = Action("立即自动更换", self.parent)
        awc_action.triggered.connect(lambda: self.force_update_wallpaper())
        tray_menu.addAction(awc_action)
            
        if sys.platform != "darwin": 
            tray_menu.addSeparator()
        
        quit_action = Action("退出", self.parent)
        quit_action.triggered.connect(self.parent.on_close)
        tray_menu.addAction(quit_action)
        
        self.tray_icon.setContextMenu(tray_menu)
        self.tray_icon.activated.connect(self.on_tray_activated)
        
        self.tray_icon.show()
    
    @Slot(QSystemTrayIcon.ActivationReason)
    def on_tray_activated(self, reason):     
        if reason == QSystemTrayIcon.ActivationReason.Context:
            # 右键点击
            pass
        elif reason == QSystemTrayIcon.ActivationReason.Trigger:
            # 单击处理（左键）
            pass
        elif reason == QSystemTrayIcon.ActivationReason.DoubleClick:
            # 双击处理
            self.parent.window().show()
            self.parent.window().activateWindow()
            self.parent.window().raise_()
        elif reason == QSystemTrayIcon.ActivationReason.MiddleClick:
            # 中键点击
            pass
        
    def show_notification(self, title=None, message=None):
        if not title:
            title = "壁纸生成器"
        if not message:
            message = "消息"
            
        self.tray_icon.showMessage(
            title,
            message,
            QSystemTrayIcon.MessageIcon.Information,
            5000
        )
        
    def force_update_wallpaper(self):
        if platform.system() == "Windows":
            self.show_notification(title="已启动 自动更换壁纸", message="请耐心等待，即将更换壁纸。")
            self.parent.force_wallpaper_update.emit()
        else:
            self.show_notification(title="自动更换壁纸 失败", message="壁纸设置功能目前仅适用于 Windows 系统。")