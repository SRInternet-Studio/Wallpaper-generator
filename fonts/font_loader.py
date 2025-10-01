# font_loader.py
from PySide6.QtGui import QFontDatabase, QGuiApplication
from PySide6.QtCore import QByteArray
from Kernel.Logger import logger
from Kernel.MainKernal import get_internal_dir
import os

def load_fonts():
    path = os.path.join(get_internal_dir(), "fonts")
    if not os.path.exists(path):
        logger.error(f"Fonts directory not found: {path}")
    else:
        QGuiApplication.processEvents()
        logger.info(f"Loading fonts from: {path}")
        for file in os.listdir(path):
            if file.lower().endswith(('.ttf', '.otf')):
                try:
                    with open(os.path.join(path, file), "rb") as f:
                        font_data = QByteArray(f.read())
                    QFontDatabase.addApplicationFontFromData(font_data)
                    logger.debug(f"Font loaded: {file}")
                except Exception as e:
                    logger.error(f"Failed to load font: {file}, {e}")
                
