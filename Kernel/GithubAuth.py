import sys
import re
from PySide6.QtWidgets import QApplication, QDialog, QVBoxLayout
from PySide6.QtCore import QUrl, Signal
from PySide6.QtGui import QIcon
from PySide6.QtWebEngineWidgets import QWebEngineView

class GithubInstallDialog(QDialog):
    """
    一个用于引导用户安装 GitHub App 并自动提取 installation_id 的对话框。
    """
    # 定义一个信号，当成功获取ID时发射
    installation_id_obtained = Signal(int)

    def __init__(self, install_url: str, parent=None):
        super().__init__(parent)
        self.setWindowTitle("连接到 GitHub")
        self.setMinimumSize(800, 600)
        self.setWindowIcon(QIcon(".\\NewIcon.ico"))

        # 1. 创建 QWebEngineView 实例
        self.browser = QWebEngineView()

        # 2. 连接 urlChanged 信号到我们的处理函数
        self.browser.urlChanged.connect(self.on_url_changed)

        # 3. 设置布局
        layout = QVBoxLayout(self)
        layout.addWidget(self.browser)
        self.setLayout(layout)

        # 4. 加载初始的安装 URL
        self.browser.setUrl(QUrl(install_url))

    def on_url_changed(self, url: QUrl):
        """当浏览器 URL 变化时被调用"""
        url_string = url.toString()
        print(f"URL 变更为: {url_string}")

        # 5. 使用正则表达式匹配安装成功的 URL
        # 格式: https://github.com/settings/installations/12345678
        match = re.match(r"https://github\.com/settings/installations/(\d+)", url_string)

        if match:
            # 6. 成功匹配！
            installation_id_str = match.group(1)
            installation_id = int(installation_id_str)
            
            print(f"成功捕获 Installation ID: {installation_id}")

            # 发射信号，将ID传递出去
            self.installation_id_obtained.emit(installation_id)
            
            # 可以在这里显示一个“成功”的消息，然后自动关闭
            self.browser.setHtml("<h1>配置成功！此窗口即将关闭...</h1>")
            self.close()

# if __name__ == "__main__":
#     app = QApplication(sys.argv)

#     # 你的 GitHub App 安装链接
#     # 你可以在 App 管理页面的 "Public page" 找到
#     MY_APP_INSTALL_URL = "https://github.com/apps/wallpaper-generator/installations/new"

#     def handle_id_obtained(inst_id):
#         print(f"主程序收到了 Installation ID: {inst_id}")

#     # 创建并显示对话框
#     dialog = GithubInstallDialog(MY_APP_INSTALL_URL)
#     # 将对话框的信号连接到主程序的处理函数
#     dialog.installation_id_obtained.connect(handle_id_obtained)
#     dialog.exec()

#     # sys.exit(app.exec()) # 在你的完整应用中应保留此行