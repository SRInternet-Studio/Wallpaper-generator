from PySide6.QtCore import QThread, Signal
from PySide6.QtGui import QPixmap

class ImageLoader(QThread):
    loaded = Signal(QPixmap)

    def __init__(self, path):
        super().__init__()
        self.path = path

    def run(self):
        pixmap = QPixmap(self.path)
        self.loaded.emit(pixmap)