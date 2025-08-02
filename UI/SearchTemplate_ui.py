# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SearchTemplate.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

from qfluentwidgets import (CardWidget, IndeterminateProgressBar, LineEdit, PrimaryPushButton,
    PushButton, SimpleCardWidget, SmoothScrollArea, SubtitleLabel,
    SwitchButton, ToolButton)

class Ui_SearchTemplate(object):
    def setupUi(self, SearchTemplate):
        if not SearchTemplate.objectName():
            SearchTemplate.setObjectName(u"SearchTemplate")
        SearchTemplate.resize(904, 623)
        self.verticalLayout = QVBoxLayout(SearchTemplate)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_12 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_12)

        self.WidgetTitle = SubtitleLabel(SearchTemplate)
        self.WidgetTitle.setObjectName(u"WidgetTitle")
        font = QFont()
        font.setFamilies([u"HarmonyOS Sans SC"])
        font.setPointSize(20)
        font.setBold(True)
        self.WidgetTitle.setFont(font)
        self.WidgetTitle.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.WidgetTitle)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer_8 = QSpacerItem(20, 8, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_8)

        self.SimpleCardWidget = SimpleCardWidget(SearchTemplate)
        self.SimpleCardWidget.setObjectName(u"SimpleCardWidget")
        self.SimpleCardWidget.setMinimumSize(QSize(361, 0))
        self.SimpleCardWidget.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_3 = QVBoxLayout(self.SimpleCardWidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.SmoothScrollArea = SmoothScrollArea(self.SimpleCardWidget)
        self.SmoothScrollArea.setObjectName(u"SmoothScrollArea")
        self.SmoothScrollArea.setLayoutDirection(Qt.LeftToRight)
        self.SmoothScrollArea.setStyleSheet(u"background: transparent;\n"
"border: none;")
        self.SmoothScrollArea.setWidgetResizable(True)
        self.SmoothScrollArea.setAlignment(Qt.AlignCenter)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 868, 525))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer_7 = QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer_7)

        self.SearchContainer = QHBoxLayout()
        self.SearchContainer.setObjectName(u"SearchContainer")
        self.horizontalSpacer_9 = QSpacerItem(5, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.SearchContainer.addItem(self.horizontalSpacer_9)

        self.SearchBox = LineEdit(self.scrollAreaWidgetContents)
        self.SearchBox.setObjectName(u"SearchBox")

        self.SearchContainer.addWidget(self.SearchBox)

        self.SearchButton = ToolButton(self.scrollAreaWidgetContents)
        self.SearchButton.setObjectName(u"SearchButton")

        self.SearchContainer.addWidget(self.SearchButton)

        self.horizontalSpacer_8 = QSpacerItem(5, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.SearchContainer.addItem(self.horizontalSpacer_8)


        self.verticalLayout_2.addLayout(self.SearchContainer)

        self.verticalSpacer_21 = QSpacerItem(10, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer_21)

        # self.Plugins_Container_ = QHBoxLayout()
        # self.Plugins_Container_.setObjectName(u"Plugins_Container_")
        # self.Label_Plugin_Card_ = CardWidget(self.scrollAreaWidgetContents)
        # self.Label_Plugin_Card_.setObjectName(u"Label_Plugin_Card_")
        # sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        # sizePolicy.setHorizontalStretch(0)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(self.Label_Plugin_Card_.sizePolicy().hasHeightForWidth())
        # self.Label_Plugin_Card_.setSizePolicy(sizePolicy)
        # self.Label_Plugin_Card_.setMinimumSize(QSize(0, 0))
        # self.Label_Plugin_Card_.setMaximumSize(QSize(16777215, 16777215))
        # self.verticalLayout_11 = QVBoxLayout(self.Label_Plugin_Card_)
        # self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        # self.Plugins_Internal_Container = QVBoxLayout()
        # self.Plugins_Internal_Container.setObjectName(u"Plugins_Internal_Container")
        # self.verticalSpacer_12 = QSpacerItem(20, 3, QSizePolicy.Minimum, QSizePolicy.Fixed)

        # self.Plugins_Internal_Container.addItem(self.verticalSpacer_12)

        # self.Plugin_Title = SubtitleLabel(self.Label_Plugin_Card_)
        # self.Plugin_Title.setObjectName(u"Plugin_Title")
        # sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        # sizePolicy1.setHorizontalStretch(0)
        # sizePolicy1.setVerticalStretch(0)
        # sizePolicy1.setHeightForWidth(self.Plugin_Title.sizePolicy().hasHeightForWidth())
        # self.Plugin_Title.setSizePolicy(sizePolicy1)
        # font1 = QFont()
        # font1.setFamilies([u"HarmonyOS Sans SC"])
        # font1.setPointSize(16)
        # font1.setBold(True)
        # font1.setKerning(True)
        # font1.setStyleStrategy(QFont.PreferAntialias)
        # self.Plugin_Title.setFont(font1)

        # self.Plugins_Internal_Container.addWidget(self.Plugin_Title)

        # self.verticalSpacer_13 = QSpacerItem(20, 1, QSizePolicy.Minimum, QSizePolicy.Fixed)

        # self.Plugins_Internal_Container.addItem(self.verticalSpacer_13)

        # self.Plugins_Internal_Container1 = QHBoxLayout()
        # self.Plugins_Internal_Container1.setObjectName(u"Plugins_Internal_Container1")
        # self.horizontalSpacer_20 = QSpacerItem(7, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        # self.Plugins_Internal_Container1.addItem(self.horizontalSpacer_20)

        # self.verticalLayout_15 = QVBoxLayout()
        # self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        # self.Plugin_Icon = QLabel(self.Label_Plugin_Card_)
        # self.Plugin_Icon.setObjectName(u"Plugin_Icon")
        # sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        # sizePolicy2.setHorizontalStretch(0)
        # sizePolicy2.setVerticalStretch(0)
        # sizePolicy2.setHeightForWidth(self.Plugin_Icon.sizePolicy().hasHeightForWidth())
        # self.Plugin_Icon.setSizePolicy(sizePolicy2)
        # self.Plugin_Icon.setMinimumSize(QSize(60, 60))
        # self.Plugin_Icon.setMaximumSize(QSize(60, 16777215))
        # self.Plugin_Icon.setStyleSheet(u"image: url(:/ICO/NewIcon.ico);")
        # self.Plugin_Icon.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        # self.verticalLayout_15.addWidget(self.Plugin_Icon)

        # self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Ignored)

        # self.verticalLayout_15.addItem(self.verticalSpacer)


        # self.Plugins_Internal_Container1.addLayout(self.verticalLayout_15)

        # self.horizontalSpacer_21 = QSpacerItem(5, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        # self.Plugins_Internal_Container1.addItem(self.horizontalSpacer_21)

        # self.verticalLayout_13 = QVBoxLayout()
        # self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        # self.Plugin_Intro = SubtitleLabel(self.Label_Plugin_Card_)
        # self.Plugin_Intro.setObjectName(u"Plugin_Intro")
        # sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        # sizePolicy3.setHorizontalStretch(0)
        # sizePolicy3.setVerticalStretch(0)
        # sizePolicy3.setHeightForWidth(self.Plugin_Intro.sizePolicy().hasHeightForWidth())
        # self.Plugin_Intro.setSizePolicy(sizePolicy3)
        # self.Plugin_Intro.setMinimumSize(QSize(0, 75))
        # font2 = QFont()
        # font2.setFamilies([u"HarmonyOS Sans SC"])
        # font2.setPointSize(14)
        # font2.setBold(True)
        # font2.setKerning(True)
        # font2.setStyleStrategy(QFont.PreferAntialias)
        # self.Plugin_Intro.setFont(font2)
        # self.Plugin_Intro.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        # self.Plugin_Intro.setWordWrap(True)

        # self.verticalLayout_13.addWidget(self.Plugin_Intro)

        # self.horizontalLayout_6 = QHBoxLayout()
        # self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        # self.AbilityButton = SwitchButton(self.Label_Plugin_Card_)
        # self.AbilityButton.setObjectName(u"AbilityButton")
        # self.AbilityButton.setChecked(True)

        # self.horizontalLayout_6.addWidget(self.AbilityButton)

        # self.horizontalSpacer_5 = QSpacerItem(178, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        # self.horizontalLayout_6.addItem(self.horizontalSpacer_5)

        # self.ActionButton = PrimaryPushButton(self.Label_Plugin_Card_)
        # self.ActionButton.setObjectName(u"ActionButton")

        # self.horizontalLayout_6.addWidget(self.ActionButton)

        # self.horizontalSpacer_6 = QSpacerItem(5, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        # self.horizontalLayout_6.addItem(self.horizontalSpacer_6)


        # self.verticalLayout_13.addLayout(self.horizontalLayout_6)


        # self.Plugins_Internal_Container1.addLayout(self.verticalLayout_13)


        # self.Plugins_Internal_Container.addLayout(self.Plugins_Internal_Container1)


        # self.verticalLayout_11.addLayout(self.Plugins_Internal_Container)


        # self.Plugins_Container_.addWidget(self.Label_Plugin_Card_)

        # self.Label_Plugin_Card_1 = CardWidget(self.scrollAreaWidgetContents)
        # self.Label_Plugin_Card_1.setObjectName(u"Label_Plugin_Card_1")
        # sizePolicy.setHeightForWidth(self.Label_Plugin_Card_1.sizePolicy().hasHeightForWidth())
        # self.Label_Plugin_Card_1.setSizePolicy(sizePolicy)
        # self.Label_Plugin_Card_1.setMinimumSize(QSize(0, 0))
        # self.Label_Plugin_Card_1.setMaximumSize(QSize(16777215, 16777215))
        # self.verticalLayout_12 = QVBoxLayout(self.Label_Plugin_Card_1)
        # self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        # self.Plugins_Internal_Container_2 = QVBoxLayout()
        # self.Plugins_Internal_Container_2.setObjectName(u"Plugins_Internal_Container_2")
        # self.verticalSpacer_16 = QSpacerItem(20, 3, QSizePolicy.Minimum, QSizePolicy.Fixed)

        # self.Plugins_Internal_Container_2.addItem(self.verticalSpacer_16)

        # self.Plugin_Title_2 = SubtitleLabel(self.Label_Plugin_Card_1)
        # self.Plugin_Title_2.setObjectName(u"Plugin_Title_2")
        # sizePolicy1.setHeightForWidth(self.Plugin_Title_2.sizePolicy().hasHeightForWidth())
        # self.Plugin_Title_2.setSizePolicy(sizePolicy1)
        # self.Plugin_Title_2.setFont(font1)

        # self.Plugins_Internal_Container_2.addWidget(self.Plugin_Title_2)

        # self.verticalSpacer_17 = QSpacerItem(20, 1, QSizePolicy.Minimum, QSizePolicy.Fixed)

        # self.Plugins_Internal_Container_2.addItem(self.verticalSpacer_17)

        # self.Plugins_Internal_Container1_2 = QHBoxLayout()
        # self.Plugins_Internal_Container1_2.setObjectName(u"Plugins_Internal_Container1_2")
        # self.horizontalSpacer_23 = QSpacerItem(7, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        # self.Plugins_Internal_Container1_2.addItem(self.horizontalSpacer_23)

        # self.verticalLayout_20 = QVBoxLayout()
        # self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        # self.Plugin_Icon_2 = QLabel(self.Label_Plugin_Card_1)
        # self.Plugin_Icon_2.setObjectName(u"Plugin_Icon_2")
        # sizePolicy2.setHeightForWidth(self.Plugin_Icon_2.sizePolicy().hasHeightForWidth())
        # self.Plugin_Icon_2.setSizePolicy(sizePolicy2)
        # self.Plugin_Icon_2.setMinimumSize(QSize(60, 60))
        # self.Plugin_Icon_2.setMaximumSize(QSize(60, 16777215))
        # self.Plugin_Icon_2.setStyleSheet(u"image: url(:/ICO/NewIcon.ico);")
        # self.Plugin_Icon_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        # self.verticalLayout_20.addWidget(self.Plugin_Icon_2)

        # self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Ignored)

        # self.verticalLayout_20.addItem(self.verticalSpacer_3)


        # self.Plugins_Internal_Container1_2.addLayout(self.verticalLayout_20)

        # self.horizontalSpacer_24 = QSpacerItem(5, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        # self.Plugins_Internal_Container1_2.addItem(self.horizontalSpacer_24)

        # self.verticalLayout_21 = QVBoxLayout()
        # self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        # self.Plugin_Intro_2 = SubtitleLabel(self.Label_Plugin_Card_1)
        # self.Plugin_Intro_2.setObjectName(u"Plugin_Intro_2")
        # sizePolicy3.setHeightForWidth(self.Plugin_Intro_2.sizePolicy().hasHeightForWidth())
        # self.Plugin_Intro_2.setSizePolicy(sizePolicy3)
        # self.Plugin_Intro_2.setMinimumSize(QSize(0, 75))
        # self.Plugin_Intro_2.setFont(font2)
        # self.Plugin_Intro_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        # self.Plugin_Intro_2.setWordWrap(True)

        # self.verticalLayout_21.addWidget(self.Plugin_Intro_2)

        # self.horizontalLayout_7 = QHBoxLayout()
        # self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        # self.AbilityButton_2 = SwitchButton(self.Label_Plugin_Card_1)
        # self.AbilityButton_2.setObjectName(u"AbilityButton_2")
        # self.AbilityButton_2.setChecked(True)

        # self.horizontalLayout_7.addWidget(self.AbilityButton_2)

        # self.horizontalSpacer_10 = QSpacerItem(178, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        # self.horizontalLayout_7.addItem(self.horizontalSpacer_10)

        # self.ActionButton_2 = PrimaryPushButton(self.Label_Plugin_Card_1)
        # self.ActionButton_2.setObjectName(u"ActionButton_2")

        # self.horizontalLayout_7.addWidget(self.ActionButton_2)

        # self.horizontalSpacer_11 = QSpacerItem(5, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        # self.horizontalLayout_7.addItem(self.horizontalSpacer_11)


        # self.verticalLayout_21.addLayout(self.horizontalLayout_7)


        # self.Plugins_Internal_Container1_2.addLayout(self.verticalLayout_21)


        # self.Plugins_Internal_Container_2.addLayout(self.Plugins_Internal_Container1_2)


        # self.verticalLayout_12.addLayout(self.Plugins_Internal_Container_2)


        # self.Plugins_Container_.addWidget(self.Label_Plugin_Card_1)


        # self.verticalLayout_2.addLayout(self.Plugins_Container_)

        self.verticalSpacer_9 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_9)

        self.ProgressLine = IndeterminateProgressBar(self.scrollAreaWidgetContents)
        self.ProgressLine.setObjectName(u"ProgressLine")

        self.verticalLayout_2.addWidget(self.ProgressLine)

        self.SmoothScrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_3.addWidget(self.SmoothScrollArea)


        self.verticalLayout.addWidget(self.SimpleCardWidget)


        self.retranslateUi(SearchTemplate)

        QMetaObject.connectSlotsByName(SearchTemplate)
    # setupUi

    def retranslateUi(self, SearchTemplate):
        SearchTemplate.setWindowTitle(QCoreApplication.translate("SearchTemplate", u"\u641c\u7d22 - \u56fe\u7247\u6e90\u5e02\u573a", None))
        self.WidgetTitle.setText(QCoreApplication.translate("SearchTemplate", u"\u641c\u7d22 - \u56fe\u7247\u6e90\u5e02\u573a", None))
        # self.Plugin_Title.setText(QCoreApplication.translate("SearchTemplate", u" Pixiv \u751f\u6210", None))
        # self.Plugin_Icon.setText("")
        # self.Plugin_Intro.setText(QCoreApplication.translate("SearchTemplate", u"\u6ca1\u6709\u76f8\u5173\u4ecb\u7ecd (README.md)", None))
        # self.AbilityButton.setOnText(QCoreApplication.translate("SearchTemplate", u"\u542f\u7528", None))
        # self.AbilityButton.setOffText(QCoreApplication.translate("SearchTemplate", u"\u7981\u7528", None))
        # self.ActionButton.setText(QCoreApplication.translate("SearchTemplate", u"\u6dfb\u52a0\u5230 \u58c1\u7eb8\u751f\u6210\u5668", None))
        # self.Plugin_Title_2.setText(QCoreApplication.translate("SearchTemplate", u" \u793a\u4f8b\u63d2\u4ef6", None))
        # self.Plugin_Icon_2.setText("")
        # self.Plugin_Intro_2.setText(QCoreApplication.translate("SearchTemplate", u"\u6ca1\u6709\u76f8\u5173\u4ecb\u7ecd (README.md)", None))
        # self.AbilityButton_2.setOnText(QCoreApplication.translate("SearchTemplate", u"\u542f\u7528", None))
        # self.AbilityButton_2.setOffText(QCoreApplication.translate("SearchTemplate", u"\u7981\u7528", None))
        # self.ActionButton_2.setText(QCoreApplication.translate("SearchTemplate", u"\u6dfb\u52a0\u5230 \u58c1\u7eb8\u751f\u6210\u5668", None))
    # retranslateUi

