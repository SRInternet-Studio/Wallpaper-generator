# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'WelcomePageNext.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

from qfluentwidgets import (CardWidget, IconWidget, PrimaryPushButton, PixmapLabel, 
    PushButton, SmoothScrollArea, SubtitleLabel, TitleLabel)
# from UI.Control_tools.PixmapLabel import APixmapLabel

import V4Resources_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1051, 604)
        Form.setMinimumSize(0, 0)
        Form.setStyleSheet(u"border-image: url(:/PNG/PNG/oyama-mahiro-ai~1.png);")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(12, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.ApplicationTitle = TitleLabel(Form)
        self.ApplicationTitle.setObjectName(u"ApplicationTitle")
        self.ApplicationTitle.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.ApplicationTitle.setWordWrap(True)

        self.horizontalLayout.addWidget(self.ApplicationTitle)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(64, 64))
        self.label.setStyleSheet(u"image: url(:/ICO/NewIcon.ico);")

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer_10 = QSpacerItem(6, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_10)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.ToadyCard = CardWidget(Form)
        self.ToadyCard.setObjectName(u"ToadyCard")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ToadyCard.sizePolicy().hasHeightForWidth())
        self.ToadyCard.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QVBoxLayout(self.ToadyCard)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.SmoothScrollArea = SmoothScrollArea(self.ToadyCard)
        self.SmoothScrollArea.setObjectName(u"SmoothScrollArea")
        self.SmoothScrollArea.setAutoFillBackground(False)
        self.SmoothScrollArea.setFrameShape(QFrame.NoFrame)
        self.SmoothScrollArea.setFrameShadow(QFrame.Raised)
        self.SmoothScrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        # self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 2449, 1574))
        self.gridLayout = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName(u"gridLayout")
        self.PixmapLabel = QLabel(self.scrollAreaWidgetContents)
        self.PixmapLabel.setObjectName(u"PixmapLabel")
        self.PixmapLabel.setPixmap(QPixmap(u":/PNG/BACKIMG1.png"))
        # self.PixmapLabel.setAlignment(Qt.AlignCenter)
        # self.PixmapLabel.setSizePolicy(
        #     QSizePolicy.Policy.Ignored,  # 水平策略：尽可能扩展
        #     QSizePolicy.Policy.Expanding   # 垂直策略：完全忽略自身大小需求
        # )
        self.PixmapLabel.setScaledContents(True)  # 确保图片缩放

        self.gridLayout.addWidget(self.PixmapLabel, 0, 0, 1, 1)

        self.SmoothScrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.SmoothScrollArea)

        self.verticalSpacer = QSpacerItem(20, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.TodayQuote = SubtitleLabel(self.ToadyCard)
        self.TodayQuote.setObjectName(u"TodayQuote")
        self.TodayQuote.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.TodayQuote.sizePolicy().hasHeightForWidth())
        self.TodayQuote.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font.setBold(True)
        self.TodayQuote.setFont(font)
        self.TodayQuote.setToolTipDuration(-1)
        self.TodayQuote.setAlignment(Qt.AlignRight|Qt.AlignTop|Qt.AlignTrailing)
        self.TodayQuote.setWordWrap(False)
        self.TodayQuote.setIndent(-1)

        self.verticalLayout_2.addWidget(self.TodayQuote)


        self.verticalLayout.addWidget(self.ToadyCard)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.FortuneCard = CardWidget(Form)
        self.FortuneCard.setObjectName(u"FortuneCard")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.FortuneCard.sizePolicy().hasHeightForWidth())
        self.FortuneCard.setSizePolicy(sizePolicy2)
        self.FortuneCard.setMaximumSize(QSize(16777215, 148))
        self.verticalLayout_4 = QVBoxLayout(self.FortuneCard)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalSpacer_4 = QSpacerItem(20, 3, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_3.addItem(self.verticalSpacer_4)

        self.SubtitleLabel = SubtitleLabel(self.FortuneCard)
        self.SubtitleLabel.setObjectName(u"SubtitleLabel")
        sizePolicy2.setHeightForWidth(self.SubtitleLabel.sizePolicy().hasHeightForWidth())
        self.SubtitleLabel.setSizePolicy(sizePolicy2)
        font1 = QFont()
        font1.setFamilies([u"HarmonyOS Sans SC"])
        font1.setPointSize(16)
        font1.setBold(True)
        font1.setKerning(True)
        font1.setStyleStrategy(QFont.PreferAntialias)
        self.SubtitleLabel.setFont(font1)

        self.verticalLayout_3.addWidget(self.SubtitleLabel)

        self.verticalSpacer_3 = QSpacerItem(20, 2, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_3.addItem(self.verticalSpacer_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_2 = QSpacerItem(7, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.IconWidget = IconWidget(self.FortuneCard)
        self.IconWidget.setObjectName(u"IconWidget")
        sizePolicy.setHeightForWidth(self.IconWidget.sizePolicy().hasHeightForWidth())
        self.IconWidget.setSizePolicy(sizePolicy)
        self.IconWidget.setMaximumSize(QSize(50, 50))

        self.horizontalLayout_4.addWidget(self.IconWidget)

        self.horizontalSpacer_3 = QSpacerItem(5, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.SubtitleLabel_2 = SubtitleLabel(self.FortuneCard)
        self.SubtitleLabel_2.setObjectName(u"SubtitleLabel_2")
        sizePolicy1.setHeightForWidth(self.SubtitleLabel_2.sizePolicy().hasHeightForWidth())
        self.SubtitleLabel_2.setSizePolicy(sizePolicy1)
        self.SubtitleLabel_2.setMinimumSize(QSize(0, 75))
        font2 = QFont()
        font2.setFamilies([u"HarmonyOS Sans SC"])
        font2.setPointSize(14)
        font2.setBold(True)
        font2.setKerning(True)
        font2.setStyleStrategy(QFont.PreferAntialias)
        self.SubtitleLabel_2.setFont(font2)
        self.SubtitleLabel_2.setWordWrap(True)

        self.horizontalLayout_4.addWidget(self.SubtitleLabel_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)


        self.horizontalLayout_2.addWidget(self.FortuneCard)

        self.DelayCard = CardWidget(Form)
        self.DelayCard.setObjectName(u"DelayCard")
        sizePolicy2.setHeightForWidth(self.DelayCard.sizePolicy().hasHeightForWidth())
        self.DelayCard.setSizePolicy(sizePolicy2)
        self.DelayCard.setMaximumSize(QSize(250, 148))
        self.verticalLayout_5 = QVBoxLayout(self.DelayCard)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalSpacer_5 = QSpacerItem(20, 3, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_6.addItem(self.verticalSpacer_5)

        self.SubtitleLabel_3 = SubtitleLabel(self.DelayCard)
        self.SubtitleLabel_3.setObjectName(u"SubtitleLabel_3")
        sizePolicy2.setHeightForWidth(self.SubtitleLabel_3.sizePolicy().hasHeightForWidth())
        self.SubtitleLabel_3.setSizePolicy(sizePolicy2)
        self.SubtitleLabel_3.setFont(font1)

        self.verticalLayout_6.addWidget(self.SubtitleLabel_3)

        self.verticalSpacer_6 = QSpacerItem(20, 2, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_6.addItem(self.verticalSpacer_6)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_4 = QSpacerItem(7, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)

        self.IconWidget_2 = IconWidget(self.DelayCard)
        self.IconWidget_2.setObjectName(u"IconWidget_2")
        sizePolicy.setHeightForWidth(self.IconWidget_2.sizePolicy().hasHeightForWidth())
        self.IconWidget_2.setSizePolicy(sizePolicy)
        self.IconWidget_2.setMinimumSize(QSize(50, 50))
        self.IconWidget_2.setMaximumSize(QSize(50, 50))

        self.horizontalLayout_5.addWidget(self.IconWidget_2)

        self.horizontalSpacer_5 = QSpacerItem(5, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_5)

        self.SubtitleLabel_4 = SubtitleLabel(self.DelayCard)
        self.SubtitleLabel_4.setObjectName(u"SubtitleLabel_4")
        sizePolicy1.setHeightForWidth(self.SubtitleLabel_4.sizePolicy().hasHeightForWidth())
        self.SubtitleLabel_4.setSizePolicy(sizePolicy1)
        self.SubtitleLabel_4.setMinimumSize(QSize(0, 75))
        self.SubtitleLabel_4.setFont(font2)
        self.SubtitleLabel_4.setWordWrap(True)

        self.horizontalLayout_5.addWidget(self.SubtitleLabel_4)


        self.verticalLayout_6.addLayout(self.horizontalLayout_5)


        self.verticalLayout_5.addLayout(self.verticalLayout_6)


        self.horizontalLayout_2.addWidget(self.DelayCard)

        self.DelayCard_2 = CardWidget(Form)
        self.DelayCard_2.setObjectName(u"DelayCard_2")
        sizePolicy2.setHeightForWidth(self.DelayCard_2.sizePolicy().hasHeightForWidth())
        self.DelayCard_2.setSizePolicy(sizePolicy2)
        self.DelayCard_2.setMaximumSize(QSize(250, 148))
        self.verticalLayout_7 = QVBoxLayout(self.DelayCard_2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalSpacer_7 = QSpacerItem(20, 3, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_8.addItem(self.verticalSpacer_7)

        self.SubtitleLabel_5 = SubtitleLabel(self.DelayCard_2)
        self.SubtitleLabel_5.setObjectName(u"SubtitleLabel_5")
        sizePolicy2.setHeightForWidth(self.SubtitleLabel_5.sizePolicy().hasHeightForWidth())
        self.SubtitleLabel_5.setSizePolicy(sizePolicy2)
        self.SubtitleLabel_5.setFont(font1)

        self.verticalLayout_8.addWidget(self.SubtitleLabel_5)

        self.verticalSpacer_8 = QSpacerItem(20, 2, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_8.addItem(self.verticalSpacer_8)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_6 = QSpacerItem(7, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_6)

        self.IconWidget_3 = IconWidget(self.DelayCard_2)
        self.IconWidget_3.setObjectName(u"IconWidget_3")
        sizePolicy.setHeightForWidth(self.IconWidget_3.sizePolicy().hasHeightForWidth())
        self.IconWidget_3.setSizePolicy(sizePolicy)
        self.IconWidget_3.setMinimumSize(QSize(50, 50))
        self.IconWidget_3.setMaximumSize(QSize(50, 50))

        self.horizontalLayout_6.addWidget(self.IconWidget_3)

        self.horizontalSpacer_7 = QSpacerItem(5, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_7)

        self.SubtitleLabel_6 = SubtitleLabel(self.DelayCard_2)
        self.SubtitleLabel_6.setObjectName(u"SubtitleLabel_6")
        sizePolicy1.setHeightForWidth(self.SubtitleLabel_6.sizePolicy().hasHeightForWidth())
        self.SubtitleLabel_6.setSizePolicy(sizePolicy1)
        self.SubtitleLabel_6.setMinimumSize(QSize(0, 75))
        self.SubtitleLabel_6.setFont(font2)
        self.SubtitleLabel_6.setWordWrap(True)

        self.horizontalLayout_6.addWidget(self.SubtitleLabel_6)


        self.verticalLayout_8.addLayout(self.horizontalLayout_6)


        self.verticalLayout_7.addLayout(self.verticalLayout_8)


        self.horizontalLayout_2.addWidget(self.DelayCard_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.SubtitleLabel_8 = SubtitleLabel(Form)
        self.SubtitleLabel_8.setObjectName(u"SubtitleLabel_8")
        font3 = QFont()
        font3.setFamilies([u"HarmonyOS Sans SC Black"])
        font3.setPointSize(16)
        font3.setBold(True)
        self.SubtitleLabel_8.setFont(font3)

        self.horizontalLayout_3.addWidget(self.SubtitleLabel_8)

        self.PrimaryPushButton = PrimaryPushButton(Form)
        self.PrimaryPushButton.setObjectName(u"PrimaryPushButton")

        self.horizontalLayout_3.addWidget(self.PrimaryPushButton)

        self.PushButton_2 = PushButton(Form)
        self.PushButton_2.setObjectName(u"PushButton_2")

        self.horizontalLayout_3.addWidget(self.PushButton_2)

        self.horizontalSpacer_8 = QSpacerItem(5, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_8)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.SubtitleLabel_7 = SubtitleLabel(Form)
        self.SubtitleLabel_7.setObjectName(u"SubtitleLabel_7")
        font4 = QFont()
        font4.setFamilies([u"HarmonyOS Sans SC"])
        font4.setPointSize(12)
        font4.setBold(True)
        self.SubtitleLabel_7.setFont(font4)
        self.SubtitleLabel_7.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.SubtitleLabel_7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.SubtitleLabel_7)

        self.PushButton = PushButton(Form)
        self.PushButton.setObjectName(u"PushButton")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.PushButton.sizePolicy().hasHeightForWidth())
        self.PushButton.setSizePolicy(sizePolicy3)

        self.horizontalLayout_7.addWidget(self.PushButton)

        self.horizontalSpacer_9 = QSpacerItem(5, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_9)


        self.verticalLayout.addLayout(self.horizontalLayout_7)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.ApplicationTitle.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:700;\">\u58c1\u7eb8\u751f\u6210\u5668 5 NEXT</span></p><p><span style=\" font-size:18pt; font-weight:700;\">for Windows</span></p></body></html>", None))
        self.label.setText("")
#if QT_CONFIG(tooltip)
        self.TodayQuote.setToolTip(QCoreApplication.translate("Form", u"\u6bcf\u65e5\u4e00\u8a00\u6765\u6e90\u4e8e\u3010\u4e00\u8a00\u3011\u63a5\u53e3", None))
#endif // QT_CONFIG(tooltip)
        self.TodayQuote.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">\u5b81\u613f\u5e26\u7740\u6d51\u8eab\u4f24\u75db\u52c7\u6562\u7ad9\u8d77 \u8ba9\u6cea\u6c34\u6d12\u6ee1\u5c18\u57c3\u4e0e\u82cd\u7a79\u4e4b\u95f4\u3002\u2014\u2014 \u4eca\u65e5\u56fe\u7247</span></p></body></html>", None))
        self.SubtitleLabel.setText(QCoreApplication.translate("Form", u" \u4eca\u65e5\u8fd0\u52bf", None))
        self.SubtitleLabel_2.setText(QCoreApplication.translate("Form", u"\u5b9c\uff1a\u751f\u56fe\n"
"\u5fcc\uff1a\u5199\u4f5c\u4e1a\n"
"\u2026\u2026", None))
        self.SubtitleLabel_3.setText(QCoreApplication.translate("Form", u" \u751f\u56fe\u5ef6\u8fdf", None))
        self.SubtitleLabel_4.setText(QCoreApplication.translate("Form", u"\u4f4e\u81f3\n"
"1.14 ms", None))
        self.SubtitleLabel_5.setText(QCoreApplication.translate("Form", u" \u56fe\u7247\u6e90\u6570\u91cf", None))
        self.SubtitleLabel_6.setText(QCoreApplication.translate("Form", u"\u73b0\u5df2\u6536\u5f55\n"
"1145 \u4e2a\u63a5\u53e3", None))
        self.SubtitleLabel_8.setText(QCoreApplication.translate("Form", u" \u66f4\u591a\u529f\u80fd\uff1a", None))
        self.PrimaryPushButton.setText(QCoreApplication.translate("Form", u"\u6e10\u53d8\u8272\u58c1\u7eb8\u751f\u6210", None))
        self.PushButton_2.setText(QCoreApplication.translate("Form", u"\u81ea\u52a8\u66f4\u6362\u58c1\u7eb8\u7684\u6258\u76d8\u7a0b\u5e8f", None))
        self.SubtitleLabel_7.setText(QCoreApplication.translate("Form", u" \u7248\u672c 5.1.0 - DEBUG - \u5df2\u6700\u65b0", None))
        self.PushButton.setText(QCoreApplication.translate("Form", u"\u53cd\u9988 Bug", None))
    # retranslateUi

