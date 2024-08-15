import sys, os
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QSplashScreen, QWidget
from 壁纸生成器V4 import Ui_Form  # 这里是转换后的 Python 文件

class MainWindow(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)  # 初始化 UI 界面

    def resizeEvent(self, event):
        print("set background")
        super().resizeEvent(event)
        self.update_background()

    def get_executable_path(self):
        if getattr(sys, 'frozen', False):
            # 如果应用是打包成可执行文件，返回打包后的路径
            return sys._MEIPASS
        else:
            # 如果应用是在开发环境中运行，返回当前脚本的路径
            return os.path.dirname(os.path.abspath(__file__))

def main():
    os.chdir(os.path.dirname(os.path.realpath(sys.argv[0])))
    app = QApplication(sys.argv)

    # 创建一个启动屏幕
    splash_pix = QPixmap(".\\NewIcon.ico")  # 替换为你的图标路径
    splash = QSplashScreen(splash_pix)
    splash.setWindowTitle("Welcome to Wallpaper_Generator V4...")
    splash.show()
    
    main_window = MainWindow()
    main_window.setWindowTitle("壁纸生成器 4")
    splash.finish(main_window)
    main_window.show()
    print("Window should be visible now.")

    # 启动 Qt 的事件循环
    # loop = asyncio.get_event_loop()
    # if loop.is_running():
    #     print("Event loop is already running.")
    # else:
    #     asyncio.set_event_loop(loop)
        
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
