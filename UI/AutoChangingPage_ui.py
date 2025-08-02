# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AutoChangingPage.ui'
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
from PySide6.QtOpenGLWidgets import QOpenGLWidget
from PySide6.QtWidgets import (QApplication, QDial, QFrame, QHBoxLayout,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

from qfluentwidgets import (CardWidget, LargeTitleLabel, LineEdit, OpacityAniStackedWidget,
    PrimaryPushButton, PushButton, SimpleCardWidget, SmoothScrollArea,
    SubtitleLabel, SwitchButton, TimePicker)
import V4Resources_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1008, 739)
        Form.setStyleSheet(u"border-image: url(:/PNG/PNG/oyama-mahiro-ai~1.png);")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.OpacityAniStackedWidget = OpacityAniStackedWidget(Form)
        self.OpacityAniStackedWidget.setObjectName(u"OpacityAniStackedWidget")
        self.OpacityAniStackedWidget.setStyleSheet(u"border-image: transparent;\n"
"background: transparent;")
        self.Settings_Page = QWidget()
        self.Settings_Page.setObjectName(u"Settings_Page")
        self.verticalLayout_3 = QVBoxLayout(self.Settings_Page)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.SimpleCardWidget_3 = SimpleCardWidget(self.Settings_Page)
        self.SimpleCardWidget_3.setObjectName(u"SimpleCardWidget_3")
        self.verticalLayout_2 = QVBoxLayout(self.SimpleCardWidget_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer_27 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer_27)

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


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.verticalSpacer_29 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer_29)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.SubtitleLabel_6 = SubtitleLabel(self.SimpleCardWidget_3)
        self.SubtitleLabel_6.setObjectName(u"SubtitleLabel_6")
        self.SubtitleLabel_6.setAlignment(Qt.AlignJustify|Qt.AlignTop)

        self.horizontalLayout_5.addWidget(self.SubtitleLabel_6)

        self.horizontalSpacer_14 = QSpacerItem(10, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_14)

        self.EnabilityButton = SwitchButton(self.SimpleCardWidget_3)
        self.EnabilityButton.setObjectName(u"EnabilityButton")
        self.EnabilityButton.setLayoutDirection(Qt.RightToLeft)
        self.EnabilityButton.setChecked(False)

        self.horizontalLayout_5.addWidget(self.EnabilityButton)

        self.horizontalSpacer_12 = QSpacerItem(8, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_12)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.verticalSpacer_26 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer_26)

        self.SubtitleLabel_3 = SubtitleLabel(self.SimpleCardWidget_3)
        self.SubtitleLabel_3.setObjectName(u"SubtitleLabel_3")

        self.verticalLayout_2.addWidget(self.SubtitleLabel_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_3 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.TextPath = LineEdit(self.SimpleCardWidget_3)
        self.TextPath.setObjectName(u"TextPath")

        self.horizontalLayout_2.addWidget(self.TextPath)

        self.ChosePath = PushButton(self.SimpleCardWidget_3)
        self.ChosePath.setObjectName(u"ChosePath")
        self.ChosePath.setMinimumSize(QSize(128, 0))

        self.horizontalLayout_2.addWidget(self.ChosePath)

        self.horizontalSpacer_7 = QSpacerItem(8, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_7)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.verticalSpacer_24 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer_24)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.SubtitleLabel_4 = SubtitleLabel(self.SimpleCardWidget_3)
        self.SubtitleLabel_4.setObjectName(u"SubtitleLabel_4")
        self.SubtitleLabel_4.setAlignment(Qt.AlignJustify|Qt.AlignTop)

        self.horizontalLayout_4.addWidget(self.SubtitleLabel_4)

        self.horizontalSpacer_13 = QSpacerItem(10, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_13)

        self.AutoStartButton = SwitchButton(self.SimpleCardWidget_3)
        self.AutoStartButton.setObjectName(u"AutoStartButton")
        self.AutoStartButton.setLayoutDirection(Qt.RightToLeft)
        self.AutoStartButton.setChecked(False)

        self.horizontalLayout_4.addWidget(self.AutoStartButton)

        self.horizontalSpacer_11 = QSpacerItem(8, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_11)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_4 = QSpacerItem(15, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)

        self.TimeDial = QDial(self.SimpleCardWidget_3)
        self.TimeDial.setObjectName(u"TimeDial")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TimeDial.sizePolicy().hasHeightForWidth())
        self.TimeDial.setSizePolicy(sizePolicy)
        self.TimeDial.setMinimumSize(QSize(50, 50))
        self.TimeDial.setMaximumSize(QSize(50, 50))
        self.TimeDial.setValue(0)

        self.horizontalLayout_3.addWidget(self.TimeDial)

        self.horizontalSpacer_5 = QSpacerItem(10, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)

        self.SubtitleLabel = SubtitleLabel(self.SimpleCardWidget_3)
        self.SubtitleLabel.setObjectName(u"SubtitleLabel")
        self.SubtitleLabel.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_3.addWidget(self.SubtitleLabel)

        self.horizontalSpacer_8 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_8)

        self.TimePicker = TimePicker(self.SimpleCardWidget_3)
        self.TimePicker.setObjectName(u"TimePicker")

        self.horizontalLayout_3.addWidget(self.TimePicker)

        self.horizontalSpacer_9 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_9)

        self.SubtitleLabel_2 = SubtitleLabel(self.SimpleCardWidget_3)
        self.SubtitleLabel_2.setObjectName(u"SubtitleLabel_2")
        self.SubtitleLabel_2.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_3.addWidget(self.SubtitleLabel_2)

        self.horizontalSpacer_6 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_6)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.openGLWidget = QOpenGLWidget(self.SimpleCardWidget_3)
        self.openGLWidget.setObjectName(u"openGLWidget")

        self.verticalLayout_2.addWidget(self.openGLWidget)

        self.SmoothScrollArea = SmoothScrollArea(self.SimpleCardWidget_3)
        self.SmoothScrollArea.setObjectName(u"SmoothScrollArea")
        self.SmoothScrollArea.setFrameShape(QFrame.NoFrame)
        self.SmoothScrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 954, 138))
        self.verticalLayout_4 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.SubtitleLabel_7 = SubtitleLabel(self.scrollAreaWidgetContents)
        self.SubtitleLabel_7.setObjectName(u"SubtitleLabel_7")
        self.SubtitleLabel_7.setAlignment(Qt.AlignJustify|Qt.AlignTop)

        self.verticalLayout_4.addWidget(self.SubtitleLabel_7)

        self.CurrentStage = SubtitleLabel(self.scrollAreaWidgetContents)
        self.CurrentStage.setObjectName(u"CurrentStage")
        font1 = QFont()
        font1.setFamilies([u"HarmonyOS Sans SC Medium"])
        font1.setPointSize(15)
        font1.setBold(False)
        self.CurrentStage.setFont(font1)

        self.verticalLayout_4.addWidget(self.CurrentStage)

        self.verticalSpacer_28 = QSpacerItem(20, 99, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_28)

        self.SmoothScrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.SmoothScrollArea)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_16 = QSpacerItem(8, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_16)

        self.CancelSettings = PushButton(self.SimpleCardWidget_3)
        self.CancelSettings.setObjectName(u"CancelSettings")
        self.CancelSettings.setMinimumSize(QSize(128, 0))

        self.horizontalLayout_6.addWidget(self.CancelSettings)

        self.SaveSettings = PrimaryPushButton(self.SimpleCardWidget_3)
        self.SaveSettings.setObjectName(u"SaveSettings")
        self.SaveSettings.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_6.addWidget(self.SaveSettings)

        self.horizontalSpacer_15 = QSpacerItem(8, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_15)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.verticalSpacer_25 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer_25)


        self.verticalLayout_3.addWidget(self.SimpleCardWidget_3)

        self.OpacityAniStackedWidget.addWidget(self.Settings_Page)

        self.verticalLayout.addWidget(self.OpacityAniStackedWidget)


        self.retranslateUi(Form)

        self.OpacityAniStackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.LargeTitleLabel.setText(QCoreApplication.translate("Form", u"\u81ea\u52a8\u66f4\u6362\u58c1\u7eb8", None))
        self.SubtitleLabel_6.setText(QCoreApplication.translate("Form", u"   \u81ea\u52a8\u66f4\u6362\uff1a", None))
        self.EnabilityButton.setOnText(QCoreApplication.translate("Form", u"\u542f\u7528", None))
        self.EnabilityButton.setOffText(QCoreApplication.translate("Form", u"\u7981\u7528", None))
        self.SubtitleLabel_3.setText(QCoreApplication.translate("Form", u"   \u56fe\u7247\u4fdd\u5b58\u8def\u5f84\uff1a", None))
        self.ChosePath.setText(QCoreApplication.translate("Form", u"\u9009\u53d6 ", None))
        self.SubtitleLabel_4.setText(QCoreApplication.translate("Form", u"   \u81ea\u52a8\u66f4\u6362\u9891\u7387\uff1a", None))
        self.AutoStartButton.setOnText(QCoreApplication.translate("Form", u"\u5f00\u673a\u81ea\u52a8\u66f4\u6362", None))
        self.AutoStartButton.setOffText(QCoreApplication.translate("Form", u"\u4e0d\u5f00\u673a\u81ea\u542f\u52a8", None))
        self.SubtitleLabel.setText(QCoreApplication.translate("Form", u"\u6bcf", None))
        self.SubtitleLabel_2.setText(QCoreApplication.translate("Form", u"\u66f4\u6362\u4e00\u6b21", None))
        self.SubtitleLabel_7.setText(QCoreApplication.translate("Form", u" \u5f53\u524d\u72b6\u6001\uff1a", None))
        self.CurrentStage.setText(QCoreApplication.translate("Form", u" \u4e0b\u6b21\u66f4\u6362\uff1aN \u5c0f\u65f6\u540e", None))
        self.CancelSettings.setText(QCoreApplication.translate("Form", u"\u653e\u5f03\u66f4\u6539", None))
        self.SaveSettings.setText(QCoreApplication.translate("Form", u"\u5e94\u7528", None))
    # retranslateUi

