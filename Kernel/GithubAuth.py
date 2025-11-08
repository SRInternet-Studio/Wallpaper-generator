import sys
import re
import webbrowser
from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QWidget
from PySide6.QtCore import Signal
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt

class GithubInstallDialog(QDialog):
    """
    一个用于引导用户安装 GitHub App 并手动输入 installation_id 的对话框。
    使用 webbrowser 模块替代 Qt WebEngine 组件，以减小打包体积。
    """
    # 定义一个信号，当成功获取ID时发射
    installation_id_obtained = Signal(int)

    def __init__(self, install_url: str, parent=None):
        super().__init__(parent)
        self.setWindowTitle("连接到 GitHub")
        self.setMinimumSize(600, 400)
        self.setWindowIcon(QIcon(".\\NewIcon.ico"))
        self.install_url = install_url

        # 设置布局
        self.setup_ui()

        # 自动打开浏览器
        self.open_browser()

    def setup_ui(self):
        """设置用户界面"""
        layout = QVBoxLayout(self)
        layout.setSpacing(20)
        layout.setContentsMargins(30, 30, 30, 30)
        
        # 说明文字
        instruction_label = QLabel("请按照以下步骤连接 GitHub 账户：")
        instruction_label.setAlignment(Qt.AlignCenter)
        instruction_label.setStyleSheet("font-size: 16px; font-weight: bold;")
        layout.addWidget(instruction_label)
        
        # 步骤说明
        steps_label = QLabel(
            "1. 点击下方按钮打开浏览器并完成 GitHub App 安装\n" \
            "2. 安装成功后，浏览器地址栏中会显示类似以下链接：\n" \
            "   https://github.com/settings/installations/12345678\n" \
            "3. 复制地址中的数字部分（例如：12345678）并粘贴到下方输入框\n" \
            "4. 点击确认按钮完成连接"
        )
        steps_label.setAlignment(Qt.AlignLeft)
        steps_label.setWordWrap(True)
        steps_label.setStyleSheet("font-size: 14px;")
        layout.addWidget(steps_label)
        
        # 打开浏览器按钮
        self.open_browser_btn = QPushButton("打开浏览器安装 GitHub App")
        self.open_browser_btn.clicked.connect(self.open_browser)
        self.open_browser_btn.setStyleSheet("font-size: 14px; padding: 8px;")
        layout.addWidget(self.open_browser_btn)
        
        # 输入框标签
        input_label = QLabel("请输入 Installation ID：")
        input_label.setStyleSheet("font-size: 14px;")
        layout.addWidget(input_label)
        
        # Installation ID 输入框
        self.id_input = QLineEdit()
        self.id_input.setPlaceholderText("例如：12345678")
        self.id_input.setStyleSheet("font-size: 14px; padding: 8px;")
        layout.addWidget(self.id_input)
        
        # 确认按钮
        self.confirm_btn = QPushButton("确认")
        self.confirm_btn.clicked.connect(self.on_confirm)
        self.confirm_btn.setStyleSheet("font-size: 14px; padding: 8px;")
        layout.addWidget(self.confirm_btn)
        
        # 添加垂直 spacer 使内容居中
        spacer = QWidget()
        spacer.setMinimumHeight(20)
        layout.addWidget(spacer)

    def open_browser(self):
        """打开系统默认浏览器访问安装 URL"""
        try:
            # 使用系统默认浏览器打开 URL
            webbrowser.open_new_tab(self.install_url)
            QMessageBox.information(
                self, "浏览器已打开", 
                "请在浏览器中完成 GitHub App 的安装，安装成功后复制 URL 中的 Installation ID 并回到本窗口粘贴。"
            )
        except Exception as e:
            QMessageBox.critical(
                self, "浏览器打开失败", 
                f"无法自动打开浏览器，请手动访问以下链接：\n{self.install_url}\n\n错误信息：{str(e)}"
            )

    def on_confirm(self):
        """处理确认按钮点击事件"""
        # 获取用户输入的 ID
        id_text = self.id_input.text().strip()
        
        # 验证输入
        if not id_text:
            QMessageBox.warning(self, "输入错误", "请输入 Installation ID！")
            return
            
        # 检查是否为有效的数字
        if not id_text.isdigit():
            # 尝试从可能的完整 URL 中提取 ID
            match = re.search(r"github\.com/settings/installations/(\d+)", id_text)
            if match:
                id_text = match.group(1)
            else:
                QMessageBox.warning(self, "输入错误", "Installation ID 必须是数字！")
                return
                
        # 转换为整数
        installation_id = int(id_text)
        
        # 发射信号，将 ID 传递出去
        self.installation_id_obtained.emit(installation_id)
        
        # 显示成功消息并关闭窗口
        QMessageBox.information(self, "配置成功", f"已成功连接到 GitHub 账户！\nInstallation ID: {installation_id}")
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