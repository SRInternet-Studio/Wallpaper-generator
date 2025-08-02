# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'emum.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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

from qfluentwidgets import (ComboBox, StrongBodyLabel)
import V4Resources_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(387, 63)
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

        self.Option = ComboBox(Form)
        self.Option.setObjectName(u"Option")
        self.Option.setStyleSheet(u"ComboBox {\n"
"    border: 1px solid rgba(0, 0, 0, 0.073);\n"
"    border-radius: 5px;\n"
"    border-bottom: 1px solid rgba(0, 0, 0, 0.183);\n"
"    padding: 5px 31px 6px 11px;\n"
"    /* font: 14px 'Segoe UI', 'Microsoft YaHei', 'PingFang SC'; */\n"
"    color: black;\n"
"    background-color: rgba(255, 255, 255, 0.7);\n"
"    text-align: left;\n"
"}\n"
"\n"
"ComboBox:hover {\n"
"    background-color: rgba(249, 249, 249, 0.5);\n"
"}\n"
"\n"
"ComboBox:pressed {\n"
"    background-color: rgba(249, 249, 249, 0.3);\n"
"    border-bottom: 1px solid rgba(0, 0, 0, 0.073);\n"
"    color: rgba(0, 0, 0, 0.63);\n"
"}\n"
"\n"
"ComboBox:disabled {\n"
"    color: rgba(0, 0, 0, 0.36);\n"
"    background: rgba(249, 249, 249, 0.3);\n"
"    border: 1px solid rgba(0, 0, 0, 0.06);\n"
"    border-bottom: 1px solid rgba(0, 0, 0, 0.06);\n"
"}\n"
"")
        self.Option.setFlat(False)

        self.horizontalLayout.addWidget(self.Option)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(Form)

        self.Option.setDefault(True)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.Title.setText(QCoreApplication.translate("Form", u"\u751f\u6210\u6765\u6e90\uff1a", None))
        self.Option.setText(QCoreApplication.translate("Form", u"1", None))
    # retranslateUi

