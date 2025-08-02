from PySide6.QtWidgets import QLabel, QScrollArea, QVBoxLayout, QWidget, QApplication, QSizePolicy
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
from qfluentwidgets import PixmapLabel

class APixmapLabel(PixmapLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAlignment(Qt.AlignCenter)  # 图片居中显示
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)  # 允许自由缩放
        self.setMinimumSize(1, 1)  # 避免初始尺寸为0

    def setPixmap(self, pixmap):
        self.original_pixmap = pixmap
        self.updateScaledPixmap()

    def updateScaledPixmap(self):
        if hasattr(self, 'original_pixmap') and not self.original_pixmap.isNull():
            # 计算缩放后的尺寸（宽度填满，高度按比例）
            scaled_pixmap = self.original_pixmap.scaled(
                self.width(),  # 目标宽度
                self.height(),  # 目标高度（仅用于计算比例）
                Qt.AspectRatioMode.KeepAspectRatio,  # 保持宽高比
                Qt.TransformationMode.SmoothTransformation  # 平滑缩放
            )
            super().setPixmap(scaled_pixmap)

    def resizeEvent(self, event):
        self.updateScaledPixmap()
        super().resizeEvent(event)