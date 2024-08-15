# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'V4-AboutHnSRKr.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
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
from PySide6.QtWidgets import (QApplication, QCommandLinkButton, QDialog, QSizePolicy,
    QWidget)

from qfluentwidgets import (BodyLabel, HyperlinkButton, PixmapLabel, PushButton,
    StrongBodyLabel, SubtitleLabel)

import webbrowser as web
# import about_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog: QDialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(525, 278)
        Dialog.setStyleSheet(u"\n"
"#Dialog {\n"
"	background-color: rgb(240, 240, 240);\n"
"   \n"
"    background-repeat: no-repeat; /* \u7981\u6b62\u5e73\u94fa */\n"
"    background-position: center; /* \u56fe\u7247\u5c45\u4e2d */\n"
"    background-attachment: fixed; /* \u56fe\u7247\u56fa\u5b9a\u4e0d\u6eda\u52a8 */\n"
"    background-size: cover; /* \u62c9\u4f38\u56fe\u7247\u4ee5\u586b\u5145\u6574\u4e2a\u80cc\u666f */\n"
"}\n"
"")
        Dialog.setWindowIcon(QIcon("NewIcon.ico"))
        self.PixmapLabel = PixmapLabel(Dialog)
        self.PixmapLabel.setObjectName(u"PixmapLabel")
        self.PixmapLabel.setGeometry(QRect(20, 20, 81, 81))
        self.PixmapLabel.setStyleSheet(u"border-image: url('NewIcon.ico');")
        self.SubtitleLabel = SubtitleLabel(Dialog)
        self.SubtitleLabel.setObjectName(u"SubtitleLabel")
        self.SubtitleLabel.setGeometry(QRect(120, 20, 120, 27))
        self.StrongBodyLabel = StrongBodyLabel(Dialog)
        self.StrongBodyLabel.setObjectName(u"StrongBodyLabel")
        self.StrongBodyLabel.setGeometry(QRect(120, 50, 171, 19))
        self.BodyLabel = BodyLabel(Dialog)
        self.BodyLabel.setObjectName(u"BodyLabel")
        self.BodyLabel.setGeometry(QRect(120, 80, 411, 141))
        self.BodyLabel.setWordWrap(True)
        self.HyperlinkButton = HyperlinkButton(Dialog)
        self.HyperlinkButton.setObjectName(u"HyperlinkButton")
        self.HyperlinkButton.setGeometry(QRect(110, 230, 391, 31))
        self.HyperlinkButton.setCheckable(False)
        self.HyperlinkButton.setUrl(QUrl(u"https://github.com/SRInternet-Studio/Wallpaper-generator"))
        self.commandLinkButton = QCommandLinkButton(Dialog)
        self.commandLinkButton.setObjectName(u"commandLinkButton")
        self.commandLinkButton.setGeometry(QRect(400, 10, 111, 41))
        self.commandLinkButton.clicked.connect(self.juanzeng)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u5173\u4e8e \u58c1\u7eb8\u751f\u6210\u5668 4", None))
        self.SubtitleLabel.setText(QCoreApplication.translate("Dialog", u"\u58c1\u7eb8\u751f\u6210\u5668 4", None))
        self.StrongBodyLabel.setText(QCoreApplication.translate("Dialog", u"Wallpaper Generator V4", None))
        self.BodyLabel.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p>Bilibili：SR思锐Official</p><p>\u4f9d\u8d56\uff1aMikirol API\uff0cLolicon API\uff0cStable Diffusion API</p><p>\u7248\u6743\uff1a\u63a5\u53e3\u53ca\u5176\u8fd4\u56de\u7684\u8d44\u6e90\u7248\u6743\u5f52\u63a5\u53e3\u5236\u4f5c\u8005\u548c\u8d44\u6e90\u521b\u4f5c\u8005\u6240\u6709</p><p>\u58c1\u7eb8\u751f\u6210\u5668 Made by \u601d\u9510\u5de5\u4f5c\u5ba4\uff08SR Studio\uff09</p><p>\u5f00\u6e90\u5730\u5740\uff1a</p></body></html>", None))
        self.HyperlinkButton.setText(QCoreApplication.translate("Dialog", u"https://github.com/SRInternet-Studio/Wallpaper-generator", None))
        self.commandLinkButton.setText(QCoreApplication.translate("Dialog", u"\u652f\u6301\u6211\u4eec", None))

    def juanzeng(self):
        web.open('https://afdian.com/a/srinternet')
    # retranslateUi

