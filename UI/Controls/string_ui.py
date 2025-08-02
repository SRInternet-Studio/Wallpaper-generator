# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'string.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt, Signal, QEvent)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QSizePolicy, QVBoxLayout, QWidget)

from qfluentwidgets import (StrongBodyLabel, TextEdit)
import V4Resources_rc

class ClickableLabel(StrongBodyLabel):
    clicked = Signal()
    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.clicked.emit()
            
        super().mousePressEvent(event)

    # def event(self, event):
    #     if event.type() == QEvent.MouseButtonPress:
    #         self.clicked.emit()
    #         return True
        
    #     return super().event(event)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(387, 150)
        Form.setStyleSheet(u"border-image: url(:/PNG/PNG/oyama-mahiro-ai~1.png);")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Title = ClickableLabel(Form)
        self.Title.setObjectName(u"Title")
        font = QFont()
        font.setFamilies([u"HarmonyOS Sans SC"])
        font.setPointSize(16)
        font.setBold(False)
        self.Title.setFont(font)

        self.verticalLayout.addWidget(self.Title)

        self.TextEdit = TextEdit(Form)
        self.TextEdit.setObjectName(u"TextEdit")

        self.verticalLayout.addWidget(self.TextEdit)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.Title.setText(QCoreApplication.translate("Form", u"\u6807\u7b7e\uff1a", None))
    # retranslateUi

