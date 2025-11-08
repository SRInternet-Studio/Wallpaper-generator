# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AboutPage.ui'
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
from PySide6.QtWidgets import (QApplication, QCommandLinkButton, QDialog, QHBoxLayout,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

from qfluentwidgets import (BodyLabel, HyperlinkButton, PixmapLabel, PushButton, isDarkTheme, 
    StrongBodyLabel, SubtitleLabel)
import webbrowser
import V4Resources_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(422, 498)
        background_color = "250, 250, 250" if not isDarkTheme() else "30, 30, 30"
        Dialog.setStyleSheet(u"\n"
"#Dialog {\n"
"	background-color: rgb(" + background_color + ");\n"
"    background-repeat: no-repeat; /* \u7981\u6b62\u5e73\u94fa */\n"
"    background-position: center; /* \u56fe\u7247\u5c45\u4e2d */\n"
"    background-attachment: fixed; /* \u56fe\u7247\u56fa\u5b9a\u4e0d\u6eda\u52a8 */\n"
"    background-size: cover; /* \u62c9\u4f38\u56fe\u7247\u4ee5\u586b\u5145\u6574\u4e2a\u80cc\u666f */\n"
"}")
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.PixmapLabel = PixmapLabel(Dialog)
        self.PixmapLabel.setObjectName(u"PixmapLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(128)
        sizePolicy.setVerticalStretch(128)
        sizePolicy.setHeightForWidth(self.PixmapLabel.sizePolicy().hasHeightForWidth())
        self.PixmapLabel.setSizePolicy(sizePolicy)
        self.PixmapLabel.setMinimumSize(QSize(128, 128))
        self.PixmapLabel.setMaximumSize(QSize(16777215, 128))
        self.PixmapLabel.setStyleSheet(u"image: url(:/ICO/NewIcon.ico);")

        self.verticalLayout.addWidget(self.PixmapLabel)

        self.verticalSpacer_4 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.SubtitleLabel = SubtitleLabel(Dialog)
        self.SubtitleLabel.setObjectName(u"SubtitleLabel")
        self.SubtitleLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.SubtitleLabel)

        self.StrongBodyLabel = StrongBodyLabel(Dialog)
        self.StrongBodyLabel.setObjectName(u"StrongBodyLabel")
        self.StrongBodyLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.StrongBodyLabel)

        self.verticalSpacer_3 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.BodyLabel = BodyLabel(Dialog)
        self.BodyLabel.setObjectName(u"BodyLabel")
        self.BodyLabel.setAlignment(Qt.AlignCenter)
        self.BodyLabel.setWordWrap(True)

        self.verticalLayout.addWidget(self.BodyLabel)

        self.verticalSpacer_2 = QSpacerItem(20, 34, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.HyperlinkButton = HyperlinkButton(Dialog)
        self.HyperlinkButton.setObjectName(u"HyperlinkButton")
        self.HyperlinkButton.setCheckable(False)
        self.HyperlinkButton.setUrl(QUrl(u"https://github.com/SRInternet-Studio/Wallpaper-generator"))

        self.horizontalLayout.addWidget(self.HyperlinkButton)

        self.commandLinkButton = QCommandLinkButton(Dialog)
        self.commandLinkButton.setObjectName(u"commandLinkButton")
        self.commandLinkButton.setMaximumSize(QSize(128, 16777215))
        if isDarkTheme():   self.commandLinkButton.setStyleSheet(u"QCommandLinkButton {	\n"
"	color: rgb(250, 250, 250);\n"
"}")
        self.commandLinkButton.clicked.connect(lambda: webbrowser.open("https://afdian.com/a/srinternet/"))

        self.horizontalLayout.addWidget(self.commandLinkButton)

        self.commandLinkButton_2 = QCommandLinkButton(Dialog)
        self.commandLinkButton_2.setObjectName(u"commandLinkButton_2")
        self.commandLinkButton_2.setMaximumSize(QSize(128, 16777215))
        if isDarkTheme():   self.commandLinkButton_2.setStyleSheet(u"QCommandLinkButton {	\n"
"	color: rgb(250, 250, 250);\n"
"}")
        self.commandLinkButton_2.clicked.connect(lambda: webbrowser.open("https://github.com/SRInternet-Studio/Wallpaper-generator/blob/NEXT-PREVIEW/DISCLAIMER.md"))

        self.horizontalLayout.addWidget(self.commandLinkButton_2)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u5173\u4e8e \u58c1\u7eb8\u751f\u6210\u5668 5 NEXT", None))
        self.SubtitleLabel.setText(QCoreApplication.translate("Dialog", u"\u58c1\u7eb8\u751f\u6210\u5668 NEXT", None))
        self.StrongBodyLabel.setText(QCoreApplication.translate("Dialog", u"Wallpaper Generator NEXT", None))
        self.BodyLabel.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p>\u7248\u672c\u53f7\uff1a5.1.0.0 (Build 251108)</p><p>APICORE \u7248\u672c\uff1a1.0</p><p>Powered by IntelliMarkets, APICORE \u53ca\u5176\u751f\u6001\u4e2d\u7684\u5f00\u6e90\u9879\u76ee</p><p>Powered by Qt for Python, QFluentWidgets</p><p>SR\u601d\u9510 \u56e2\u961f \u00a9 2025 \u4fdd\u7559\u90e8\u5206\u6743\u5229</p></body></html>", None))
        self.HyperlinkButton.setText(QCoreApplication.translate("Dialog", u"Github \u4ed3\u5e93", None))
        self.commandLinkButton.setText(QCoreApplication.translate("Dialog", u"\u652f\u6301\u6211\u4eec", None))
        self.commandLinkButton_2.setText(QCoreApplication.translate("Dialog", u"\u514d\u8d23\u58f0\u660e", None))
    # retranslateUi

