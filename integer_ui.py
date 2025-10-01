# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'integer.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QSizePolicy, QVBoxLayout,
    QWidget)

from qfluentwidgets import (Slider, SpinBox, StrongBodyLabel)
import V4Resources_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(386, 94)
        Form.setStyleSheet(u"border-image: url(:/PNG/PNG/oyama-mahiro-ai~1.png);")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.Title = StrongBodyLabel(Form)
        self.Title.setObjectName(u"Title")
        font = QFont()
        font.setFamilies([u"HarmonyOS Sans SC"])
        font.setPointSize(16)
        font.setBold(False)
        self.Title.setFont(font)

        self.horizontalLayout.addWidget(self.Title)

        self.NumberSelector = SpinBox(Form)
        self.NumberSelector.setObjectName(u"NumberSelector")
        self.NumberSelector.setMinimum(1)
        self.NumberSelector.setMaximum(100)

        self.horizontalLayout.addWidget(self.NumberSelector)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.NumberSlider = Slider(Form)
        self.NumberSlider.setObjectName(u"NumberSlider")
        self.NumberSlider.setMinimumSize(QSize(200, 24))
        self.NumberSlider.setOrientation(Qt.Horizontal)

        self.verticalLayout.addWidget(self.NumberSlider)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.Title.setText(QCoreApplication.translate("Form", u"\u751f\u6210\u6570\u91cf (1~100)\uff1a", None))
    # retranslateUi

