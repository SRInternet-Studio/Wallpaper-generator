# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SettingsPage.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

from qfluentwidgets import (CardWidget, LargeTitleLabel, OpacityAniStackedWidget, PrimaryPushButton,
    PushButton, SimpleCardWidget, SmoothScrollArea, SubtitleLabel)
import V4Resources_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(986, 650)
        Form.setStyleSheet(u"border-image: url(:/PNG/PNG/oyama-mahiro-ai~1.png);")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.OpacityAniStackedWidget = OpacityAniStackedWidget(Form)
        self.OpacityAniStackedWidget.setObjectName(u"OpacityAniStackedWidget")
        self.OpacityAniStackedWidget.setStyleSheet(u"border-image: transparent;\n"
"background: transparent;")
        self.Settings_Page = QWidget()
        self.Settings_Page.setObjectName(u"Settings_Page")
        self.verticalLayout_2 = QVBoxLayout(self.Settings_Page)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.SimpleCardWidget_3 = SimpleCardWidget(self.Settings_Page)
        self.SimpleCardWidget_3.setObjectName(u"SimpleCardWidget_3")
        self.verticalLayout_3 = QVBoxLayout(self.SimpleCardWidget_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalSpacer_27 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_3.addItem(self.verticalSpacer_27)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_2 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.LargeTitleLabel = LargeTitleLabel(self.SimpleCardWidget_3)
        self.LargeTitleLabel.setObjectName(u"LargeTitleLabel")
        font = QFont()
        font.setFamilies([u"HarmonyOS Sans SC"])
        font.setPointSize(32)
        font.setBold(False)
        self.LargeTitleLabel.setFont(font)

        self.horizontalLayout.addWidget(self.LargeTitleLabel)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.SubtitleLabel_5 = SubtitleLabel(self.SimpleCardWidget_3)
        self.SubtitleLabel_5.setObjectName(u"SubtitleLabel_5")
        self.SubtitleLabel_5.setAlignment(Qt.AlignJustify|Qt.AlignTop)

        self.verticalLayout_3.addWidget(self.SubtitleLabel_5)

        self.verticalSpacer_29 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_3.addItem(self.verticalSpacer_29)

        self.SmoothScrollArea = SmoothScrollArea(self.SimpleCardWidget_3)
        self.SmoothScrollArea.setObjectName(u"SmoothScrollArea")
        self.SmoothScrollArea.setFrameShape(QFrame.NoFrame)
        self.SmoothScrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 932, 414))
        self.verticalLayout_5 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_5.setSpacing(5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(5, 0, 5, 0)
        self.cardSpacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        # self.verticalLayout_5.addItem(self.cardSpacer)

        self.verticalSpacer_23 = QSpacerItem(20, 383, QSizePolicy.Minimum, QSizePolicy.Expanding)

        # self.verticalLayout_5.addItem(self.verticalSpacer_23)

        self.SmoothScrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_3.addWidget(self.SmoothScrollArea)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer)

        self.AboutButton = PushButton(self.SimpleCardWidget_3)
        self.AboutButton.setObjectName(u"AboutButton")
        self.AboutButton.setMinimumSize(QSize(140, 0))
        self.AboutButton.setMaximumSize(QSize(165, 16777215))

        self.horizontalLayout_12.addWidget(self.AboutButton)

        self.horizontalSpacer_9 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_9)

        self.SaveSettings = PrimaryPushButton(self.SimpleCardWidget_3)
        self.SaveSettings.setObjectName(u"SaveSettings")
        self.SaveSettings.setMinimumSize(QSize(128, 0))

        self.horizontalLayout_12.addWidget(self.SaveSettings)

        self.horizontalSpacer_27 = QSpacerItem(14, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_27)


        self.verticalLayout_3.addLayout(self.horizontalLayout_12)

        self.verticalSpacer_25 = QSpacerItem(20, 15, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_3.addItem(self.verticalSpacer_25)


        self.verticalLayout_2.addWidget(self.SimpleCardWidget_3)

        self.OpacityAniStackedWidget.addWidget(self.Settings_Page)

        self.verticalLayout.addWidget(self.OpacityAniStackedWidget)


        self.retranslateUi(Form)

        self.OpacityAniStackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.LargeTitleLabel.setText(QCoreApplication.translate("Form", u"\u8bbe\u7f6e", None))
        self.SubtitleLabel_5.setText(QCoreApplication.translate("Form", u"   \u4e2a\u6027\u5316\u4f60\u7684\u58c1\u7eb8\u751f\u6210\u5668", None))
        self.AboutButton.setText(QCoreApplication.translate("Form", u"\u5173\u4e8e \u58c1\u7eb8\u751f\u6210\u5668", None))
        self.SaveSettings.setText(QCoreApplication.translate("Form", u"\u5e94\u7528", None))
    # retranslateUi

