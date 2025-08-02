# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'WelcomePage.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

from qfluentwidgets import (DisplayLabel, OpacityAniStackedWidget, PushButton, TitleLabel)
import V4Resources_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1070, 650)
        Form.setStyleSheet(u"border-image: url(:/PNG/PNG/oyama-mahiro-ai~1.png);")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.OpacityAniStackedWidget = OpacityAniStackedWidget(Form)
        self.OpacityAniStackedWidget.setObjectName(u"OpacityAniStackedWidget")
        self.OpacityAniStackedWidget.setStyleSheet(u"border-image: transparent;\n"
"background: transparent;")
        self.Welcome_Page = QWidget()
        self.Welcome_Page.setObjectName(u"Welcome_Page")
        self.verticalLayout_2 = QVBoxLayout(self.Welcome_Page)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.TitleLabel = TitleLabel(self.Welcome_Page)
        self.TitleLabel.setObjectName(u"TitleLabel")
        font = QFont()
        font.setFamilies([u"HarmonyOS Sans SC"])
        font.setPointSize(18)
        font.setBold(True)
        self.TitleLabel.setFont(font)
        self.TitleLabel.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
        self.TitleLabel.setProperty("lightColor", QColor(245, 245, 245))
        self.TitleLabel.setProperty("darkColor", QColor(0, 0, 0))

        self.gridLayout.addWidget(self.TitleLabel, 1, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 100, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_3, 0, 0, 1, 1)

        self.DisplayLabel = DisplayLabel(self.Welcome_Page)
        self.DisplayLabel.setObjectName(u"DisplayLabel")
        self.DisplayLabel.setMaximumSize(QSize(16777215, 30))
        font1 = QFont()
        font1.setFamilies([u"HarmonyOS Sans SC"])
        font1.setPointSize(51)
        font1.setBold(False)
        self.DisplayLabel.setFont(font1)
        self.DisplayLabel.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
        self.DisplayLabel.setProperty("lightColor", QColor(245, 245, 245))
        self.DisplayLabel.setProperty("darkColor", QColor(0, 0, 0))

        self.gridLayout.addWidget(self.DisplayLabel, 2, 0, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)

        self.verticalSpacer_10 = QSpacerItem(20, 100, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_10)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.ToACG = PushButton(self.Welcome_Page)
        self.ToACG.setObjectName(u"ToACG")
        self.ToACG.setMinimumSize(QSize(200, 0))
        self.ToACG.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout_3.addWidget(self.ToACG)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.ToAI = PushButton(self.Welcome_Page)
        self.ToAI.setObjectName(u"ToAI")
        self.ToAI.setMinimumSize(QSize(200, 0))
        self.ToAI.setMaximumSize(QSize(200, 16777215))
        self.ToAI.setProperty("hasIcon", False)

        self.horizontalLayout_3.addWidget(self.ToAI)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.verticalSpacer_2 = QSpacerItem(20, 151, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.OpacityAniStackedWidget.addWidget(self.Welcome_Page)

        self.verticalLayout.addWidget(self.OpacityAniStackedWidget)


        self.retranslateUi(Form)

        self.OpacityAniStackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.TitleLabel.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:51pt;\">\u6b22\u8fce Welcome</span></p></body></html>", None))
        self.DisplayLabel.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:18pt;\">\u58c1\u7eb8\u751f\u6210\u5668 \u53ef\u4ee5\u5feb\u901f\u5730\u5e2e\u4f60\u751f\u6210\u4e00\u5f20\u7cbe\u7f8e\u4e8c\u6b21\u5143\u58c1\u7eb8\u3002</span></p></body></html>", None))
        self.ToACG.setText(QCoreApplication.translate("Form", u"\u6253\u5f00 \u56fe\u7247\u6e90\u5e02\u573a", None))
        self.ToAI.setText(QCoreApplication.translate("Form", u"\u5236\u4f5c\u6e10\u53d8\u8272\u58c1\u7eb8", None))
    # retranslateUi

