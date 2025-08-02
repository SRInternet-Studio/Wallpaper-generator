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
from PySide6.QtWidgets import (QApplication, QGridLayout, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

from qfluentwidgets import (CardWidget, CheckBox, LargeTitleLabel, LineEdit,
    OpacityAniStackedWidget, PrimaryPushButton, PushButton, SimpleCardWidget,
    SubtitleLabel)
import V4Resources_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1008, 650)
        Form.setStyleSheet(u"border-image: url(:/PNG/PNG/oyama-mahiro-ai~1.png);")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.OpacityAniStackedWidget = OpacityAniStackedWidget(Form)
        self.OpacityAniStackedWidget.setObjectName(u"OpacityAniStackedWidget")
        self.OpacityAniStackedWidget.setStyleSheet(u"border-image: transparent;\n"
"background: transparent;")
        self.Settings_Page = QWidget()
        self.Settings_Page.setObjectName(u"Settings_Page")
        self.gridLayout_7 = QGridLayout(self.Settings_Page)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.SimpleCardWidget_3 = SimpleCardWidget(self.Settings_Page)
        self.SimpleCardWidget_3.setObjectName(u"SimpleCardWidget_3")
        self.gridLayout_6 = QGridLayout(self.SimpleCardWidget_3)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.verticalSpacer_27 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_6.addItem(self.verticalSpacer_27, 1, 1, 1, 1)

        self.AboutButton = PushButton(self.SimpleCardWidget_3)
        self.AboutButton.setObjectName(u"AboutButton")
        self.AboutButton.setMinimumSize(QSize(140, 0))
        self.AboutButton.setMaximumSize(QSize(165, 16777215))

        self.gridLayout_6.addWidget(self.AboutButton, 18, 1, 1, 1)

        self.SavePath = LineEdit(self.SimpleCardWidget_3)
        self.SavePath.setObjectName(u"SavePath")

        self.gridLayout_6.addWidget(self.SavePath, 5, 1, 1, 3)

        self.SubtitleLabel_3 = SubtitleLabel(self.SimpleCardWidget_3)
        self.SubtitleLabel_3.setObjectName(u"SubtitleLabel_3")

        self.gridLayout_6.addWidget(self.SubtitleLabel_3, 4, 1, 1, 1)

        self.verticalSpacer_26 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.verticalSpacer_26, 18, 6, 1, 1)

        self.horizontalSpacer_12 = QSpacerItem(15, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_12, 11, 0, 1, 1)

        self.verticalSpacer_25 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_6.addItem(self.verticalSpacer_25, 20, 4, 1, 1)

        self.PrimaryPushButton = PrimaryPushButton(self.SimpleCardWidget_3)
        self.PrimaryPushButton.setObjectName(u"PrimaryPushButton")

        self.gridLayout_6.addWidget(self.PrimaryPushButton, 11, 1, 1, 1)

        self.CheckBox = CheckBox(self.SimpleCardWidget_3)
        self.CheckBox.setObjectName(u"CheckBox")

        self.gridLayout_6.addWidget(self.CheckBox, 4, 4, 1, 1)

        self.verticalSpacer_24 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_6.addItem(self.verticalSpacer_24, 7, 1, 1, 1)

        self.verticalSpacer_23 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer_23, 12, 1, 1, 1)

        self.ChoseBackgroundPath = PushButton(self.SimpleCardWidget_3)
        self.ChoseBackgroundPath.setObjectName(u"ChoseBackgroundPath")
        self.ChoseBackgroundPath.setMinimumSize(QSize(100, 0))

        self.gridLayout_6.addWidget(self.ChoseBackgroundPath, 8, 4, 1, 1)

        self.verticalSpacer_28 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_6.addItem(self.verticalSpacer_28, 10, 1, 1, 1)

        self.SaveSettings = PrimaryPushButton(self.SimpleCardWidget_3)
        self.SaveSettings.setObjectName(u"SaveSettings")
        self.SaveSettings.setMinimumSize(QSize(100, 0))

        self.gridLayout_6.addWidget(self.SaveSettings, 17, 4, 2, 1)

        self.ChosePath = PushButton(self.SimpleCardWidget_3)
        self.ChosePath.setObjectName(u"ChosePath")
        self.ChosePath.setMinimumSize(QSize(128, 0))

        self.gridLayout_6.addWidget(self.ChosePath, 5, 4, 1, 1)

        self.LargeTitleLabel = LargeTitleLabel(self.SimpleCardWidget_3)
        self.LargeTitleLabel.setObjectName(u"LargeTitleLabel")
        font = QFont()
        font.setFamilies([u"HarmonyOS Sans SC"])
        font.setPointSize(32)
        font.setBold(False)
        self.LargeTitleLabel.setFont(font)

        self.gridLayout_6.addWidget(self.LargeTitleLabel, 3, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer, 18, 2, 1, 1)

        self.SubtitleLabel_7 = SubtitleLabel(self.SimpleCardWidget_3)
        self.SubtitleLabel_7.setObjectName(u"SubtitleLabel_7")

        self.gridLayout_6.addWidget(self.SubtitleLabel_7, 8, 1, 1, 3)


        self.gridLayout_7.addWidget(self.SimpleCardWidget_3, 1, 0, 1, 1)

        self.OpacityAniStackedWidget.addWidget(self.Settings_Page)

        self.verticalLayout.addWidget(self.OpacityAniStackedWidget)


        self.retranslateUi(Form)

        self.OpacityAniStackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.AboutButton.setText(QCoreApplication.translate("Form", u"\u5173\u4e8e \u58c1\u7eb8\u751f\u6210\u5668", None))
        self.SubtitleLabel_3.setText(QCoreApplication.translate("Form", u"\u56fe\u7247\u4fdd\u5b58\u8def\u5f84\uff1a", None))
        self.PrimaryPushButton.setText(QCoreApplication.translate("Form", u"\u8bbe\u7f6e \u81ea\u52a8\u66f4\u6362\u58c1\u7eb8\u7684\u6258\u76d8\u7a0b\u5e8f", None))
        self.CheckBox.setText(QCoreApplication.translate("Form", u"\u6bcf\u6b21\u5747\u8be2\u95ee", None))
        self.ChoseBackgroundPath.setText(QCoreApplication.translate("Form", u"\u9009\u53d6 ", None))
        self.SaveSettings.setText(QCoreApplication.translate("Form", u"\u5e94\u7528", None))
        self.ChosePath.setText(QCoreApplication.translate("Form", u"\u9009\u53d6 ", None))
        self.LargeTitleLabel.setText(QCoreApplication.translate("Form", u"\u8bbe\u7f6e", None))
        self.SubtitleLabel_7.setText(QCoreApplication.translate("Form", u"\u7a0b\u5e8f\u80cc\u666f\uff1a", None))
    # retranslateUi

