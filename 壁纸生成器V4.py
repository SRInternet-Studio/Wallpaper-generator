# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'v4-NewUitjJoiR.ui'
##
# Created by: Qt User Interface Compiler version 6.4.3
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

import asyncio
import base64
import subprocess
import psutil
import re
import ctypes
import time
import traceback
from PySide6 import QtGui
from PySide6 import QtCore
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt, QTimer, QModelIndex, Signal)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGraphicsDropShadowEffect, QGridLayout, QHBoxLayout,
                               QHeaderView, QLayout, QListWidgetItem, QSizePolicy,
                               QSpacerItem, QTableWidgetItem, QVBoxLayout, QWidget, QDialog, QStyleOptionViewItem, QMessageBox, QFileDialog)

from qfluentwidgets import (BodyLabel, CardWidget, CheckBox, ComboBox,
                            CommandBar, CommandBarView, DisplayLabel, DoubleSpinBox, ElevatedCardWidget, FluentIcon, HorizontalFlipView,
                            HorizontalPipsPager, HyperlinkLabel, IndeterminateProgressBar, LargeTitleLabel,
                            LineEdit, MessageBox, MessageDialog, OpacityAniStackedWidget, PopUpAniStackedWidget, Pivot, PlainTextEdit,
                            PrimaryPushButton, PushButton, RadioButton, SegmentedToolWidget,
                            SegmentedWidget, SimpleCardWidget, Slider, SmoothScrollArea,
                            SpinBox, StrongBodyLabel, SubtitleLabel, TableWidget,
                            TitleLabel, Dialog, Flyout, InfoBarIcon, FlyoutView, FlipImageDelegate, Action, FlyoutAnimationType)
import requests
import threading
import random
import V4Resources

from datetime import datetime
from PIL import Image

import Dialog as DialogUi  # type: ignore
import V4About

import logging
import os
import sys

# 设置日志记录的基本配置
logging.basicConfig(
    level=logging.DEBUG,  # 设置日志级别为 DEBUG
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'  # 设置日志格式
)

# class DialogWindow(QWidget, DialogUI):
#     def __init__(self, parent=None, title: str="标题", content: str="内容"):
#         super(DialogWindow, self).__init__(parent)
#         self.setupUi(self, title, content)  # 初始化 UI 界面


class Ui_Form(object):
    #     def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
    #         painter = QPainter(self)
    #         pixmap = QPixmap(".//BACKIMG2.jpg")
    #         painter.drawPixmap(self.rect(), pixmap)

    #     def __init__(self):
    #         super().__init__()
    #         self.pixmap = QPixmap(".//BACKIMG2.png")

    #     def paintEvent(self, event):
    #         painter = QPainter(self)
    #         painter.drawPixmap(self.rect(), self.pixmap)
    #         super().paintEvent(event)

    update_AIsignal = Signal(str)
    error_AIsignal = Signal(str)

    def update_background(self):
        # 获取当前窗口的尺寸
        window_width = self.MainUI.width()
        window_height = self.MainUI.height()

        # 计算图像缩放比例
        pixmap_width = self.pixmap.width()
        pixmap_height = self.pixmap.height()

        scale_x = window_width / pixmap_width
        scale_y = window_height / pixmap_height

        # 选择使图像的短边适应窗口的比例
        scale = max(scale_x, scale_y)

        # 创建缩放后的图像
        scaled_pixmap = self.pixmap.scaled(
            pixmap_width * scale,
            pixmap_height * scale,
            Qt.AspectRatioMode.IgnoreAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )

        # 更新背景图像
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(scaled_pixmap))
        self.MainUI.setPalette(palette)
        self.ACGImages.setItemSize(self.ACGImages.size())
        self.PixivImages.setItemSize(self.PixivImages.size())
        self.AIImages.setItemSize(self.AIImages.size())
        # self.ACGImages.setMinimumSize(self.ElevatedCardWidget.size())

    def setupUi(self, Form: QWidget):

        self.MainUI = Form
        self.AIWorkingList = []
        self.interval = 0
        self.update_AIsignal.connect(self.GetAICompleted)
        self.error_AIsignal.connect(self.GetAIFailed)

        # self.loop = asyncio.get_event_loop()
        # if self.loop.is_running():
        #     print("Event loop is already running.")
        # else:
        #     asyncio.set_event_loop(self.loop)

        if not self.MainUI.objectName():
            self.MainUI.setObjectName(u"Form")

        self.MainUI.setWindowTitle("壁纸生成器 4")
        self.MainUI.setWindowIcon(QIcon("./NewIcon.ico"))
        self.MainUI.resize(1109, 650)
        absolute_path = os.path.abspath('BACKIMG2.png')
        # border-image: url(BACKIMG2.png);
        self.MainUI.setStyleSheet(
            f"background-image: url('.//BACKIMG2.png'); background-repeat: no-repeat; background-position: center;")

        pixmap = QPixmap('./BACKIMG1.png')  # <---------------背景图片
        self.pixmap = pixmap  # 加载图片

        # self.palette = QPalette()
        # self.MainUI.setPalette(QPalette(self.palette()))  # 初始调色板设置

        # 获取窗口的高度
        window_height = self.MainUI.height()

        # 计算调整后的高度和宽度
        scaled_height = window_height
        scaled_width = int(pixmap.width() * (scaled_height / pixmap.height()))

        # 缩放图片
        pixmap = pixmap.scaled(scaled_width, scaled_height,
                               Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)

        # 创建一个 QPalette 对象，并设置背景图片
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(QPixmap(pixmap)))

        # 设置主窗口的调色板
        self.MainUI.setPalette(palette)

        self.verticalLayout = QVBoxLayout(self.MainUI)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget_3 = QWidget(self.MainUI)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setStyleSheet(u"border-image: transparent;\n"
                                    "background: transparent;")
        self.verticalLayout_7 = QVBoxLayout(self.widget_3)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.TopMenu = SegmentedWidget(self.widget_3)
        self.TopMenu.setObjectName(u"TopMenu")
        self.TopMenu.setStyleSheet(u"PivotItem {\n"
                                   "    padding: 10px 12px;\n"
                                   "    color: white;\n"
                                   "    background-color: transparent;\n"
                                   "    border: none;\n"
                                   "    outline: none;\n"
                                   "    margin: 0;\n"
                                   "}\n"
                                   "\n"
                                   "PivotItem[isSelected=true]:hover {\n"
                                   "    color: rgba(0, 0, 0, 0.63);\n"
                                   "}\n"
                                   "\n"
                                   "PivotItem[isSelected=true]:pressed {\n"
                                   "    color: rgba(0, 0, 0, 0.53);\n"
                                   "}\n"
                                   "\n"
                                   "PivotItem[isSelected=false]:pressed {\n"
                                   "    color: rgba(0, 0, 0, 0.75);\n"
                                   "}\n"
                                   "\n"
                                   "PivotItem[hasIcon=false] {\n"
                                   "    padding-left: 12px;\n"
                                   "    padding-right: 12px;\n"
                                   "}\n"
                                   "\n"
                                   "PivotItem[hasIcon=true] {\n"
                                   "    padding-left: 36px;\n"
                                   "    padding-right: 12px;\n"
                                   "}\n"
                                   "\n"
                                   "Pivot {\n"
                                   "    border: none;\n"
                                   "    background-color: transparent;\n"
                                   "}\n"
                                   "\n"
                                   "#view {\n"
                                   "    background-color: transparent;\n"
                                   "}\n"
                                   "\n"
                                   "SegmentedToolItem {\n"
                                   "    padding: 5px 9px 6px 8px;\n"
                                   "}\n"
                                   "\n"
                                   "SegmentedWidget, SegmentedToolWidget {\n"
                                   "    background-color: transparent;\n"
                                   "    border: 1px solid rgba(0, 0, 0, 0.0578);\n"
                                   "    border-radius: 6px;\n"
                                   "}\n"
                                   "\n"
                                   ""
                                   "SegmentedItem[isSelected=false],\n"
                                   "SegmentedToolItem[isSelected=false] {\n"
                                   "    padding-top: 3px;\n"
                                   "    padding-bottom: 3px;\n"
                                   "    background-color: transparent;\n"
                                   "    border: none;\n"
                                   "    border-radius: 6px;\n"
                                   "    margin: 3px 2px;\n"
                                   "}\n"
                                   "\n"
                                   "SegmentedItem[isSelected=false]:hover,\n"
                                   "SegmentedToolItem[isSelected=false]:hover {\n"
                                   "    background-color: rgba(0, 0, 0, 9);\n"
                                   "}\n"
                                   "\n"
                                   "SegmentedItem[isSelected=false]:pressed,\n"
                                   "SegmentedToolItem[isSelected=false]:pressed {\n"
                                   "    background-color: rgba(0, 0, 0, 6);\n"
                                   "    margin: 3px 4px 3px 4px;\n"
                                   "}\n"
                                   "\n"
                                   "SegmentedItem[isSelected=true],\n"
                                   "SegmentedToolItem[isSelected=true] {\n"
                                   "    padding-top: 6px;\n"
                                   "    padding-bottom: 6px;\n"
                                   "    background-color: rgba(255, 255, 255, 0.7);\n"
                                   "    border: 1px solid rgba(0, 0, 0, 0.073);\n"
                                   "    border-bottom: 1px solid rgba(0, 0, 0, 0.183);\n"
                                   "    border-radius: 6px;\n"
                                   "    margin: 0px;\n"
                                   "    color: black;\n"
                                   "}\n"
                                   "\n"
                                   "SegmentedItem[isSelected=true]:hover,\n"
                                   "SegmentedItem[isSelected=t"
                                   "rue]:pressed,\n"
                                   "SegmentedToolItem[isSelected=true]:hover,\n"
                                   "SegmentedToolItem[isSelected=true]:pressed {\n"
                                   "    color: black;\n"
                                   "}")

        self.verticalLayout_7.addWidget(self.TopMenu)

        self.verticalLayout.addWidget(self.widget_3)

        self.OpacityAniStackedWidget = PopUpAniStackedWidget(self.MainUI)
        self.OpacityAniStackedWidget.setObjectName(u"OpacityAniStackedWidget")
        self.OpacityAniStackedWidget.setStyleSheet(u"border-image: transparent;\n"
                                                   "background: transparent;")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_2 = QVBoxLayout(self.page)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")

        self.effect_shadow = QGraphicsDropShadowEffect(self.page)
        self.effect_shadow.setOffset(0, 0)
        self.effect_shadow.setBlurRadius(30)
        self.effect_shadow.setColor(Qt.GlobalColor.gray)

        self.DisplayLabel = DisplayLabel(self.page)
        self.DisplayLabel.setObjectName(u"DisplayLabel")
        self.DisplayLabel.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setFamilies([u"HarmonyOS Sans SC"])
        font.setPointSize(51)
        font.setBold(False)
        self.DisplayLabel.setFont(font)
        self.DisplayLabel.setAlignment(Qt.AlignBottom | Qt.AlignHCenter)
        self.DisplayLabel.setProperty("lightColor", QColor(245, 245, 245))
        # self.DisplayLabel.setProperty("lightColor", QColor(30, 30, 30))
        self.DisplayLabel.setProperty("darkColor", QColor(0, 0, 0))
        self.DisplayLabel.setGraphicsEffect(self.effect_shadow)

        self.gridLayout.addWidget(self.DisplayLabel, 2, 0, 1, 1)

        self.TitleLabel = TitleLabel(self.page)
        self.TitleLabel.setObjectName(u"TitleLabel")
        font1 = QFont()
        font1.setFamilies([u"HarmonyOS Sans SC"])
        font1.setPointSize(18)
        font1.setBold(True)
        self.TitleLabel.setFont(font1)
        self.TitleLabel.setAlignment(Qt.AlignBottom | Qt.AlignHCenter)
        self.TitleLabel.setProperty("lightColor", QColor(245, 245, 245))
        # self.TitleLabel.setProperty("lightColor", QColor(30, 30, 30))
        self.TitleLabel.setProperty("darkColor", QColor(0, 0, 0))
        self.TitleLabel.setGraphicsEffect(self.effect_shadow)

        self.gridLayout.addWidget(self.TitleLabel, 1, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(
            20, 100, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_3, 0, 0, 1, 1)

        self.verticalLayout_2.addLayout(self.gridLayout)

        self.verticalSpacer = QSpacerItem(
            20, 152, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_2 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.ToACG = PushButton(self.page)
        self.ToACG.setObjectName(u"ToACG")
        self.ToACG.setMinimumSize(QSize(200, 0))
        self.ToACG.setMaximumSize(QSize(200, 16777215))

        self.ToACG.clicked.connect(self.ToACGClicked)

        self.horizontalLayout_3.addWidget(self.ToACG)

        # self.horizontalSpacer = QSpacerItem(
        #     40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        # self.horizontalLayout_3.addItem(self.horizontalSpacer)

        # self.ToPixiv = PushButton(self.page)
        # self.ToPixiv.setObjectName(u"ToPixiv")
        # self.ToPixiv.setMinimumSize(QSize(200, 0))
        # self.ToPixiv.setMaximumSize(QSize(16777215, 16777215))

        # self.ToPixiv.clicked.connect(self.ToPixivClicked)

        # self.horizontalLayout_3.addWidget(self.ToPixiv)

        self.horizontalSpacer_3 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.ToAI = PushButton(self.page)
        self.ToAI.setObjectName(u"ToAI")
        self.ToAI.setMinimumSize(QSize(200, 0))
        self.ToAI.setMaximumSize(QSize(200, 16777215))
        self.ToAI.setProperty("hasIcon", False)

        self.ToAI.clicked.connect(self.ToAIClicked)

        self.horizontalLayout_3.addWidget(self.ToAI)

        self.horizontalSpacer_4 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)

        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.verticalSpacer_2 = QSpacerItem(
            20, 151, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        # self.OpacityAniStackedWidget.addWidget(self.page)
        self.addSubInterface(self.page, "page", "更多功能")

        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.horizontalLayout_2 = QHBoxLayout(self.page_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.SimpleCardWidget = SimpleCardWidget(self.page_2)
        self.SimpleCardWidget.setObjectName(u"SimpleCardWidget")
        self.SimpleCardWidget.setMinimumSize(QSize(361, 0))
        self.SimpleCardWidget.setMaximumSize(QSize(361, 16777215))
        self.verticalLayout_3 = QVBoxLayout(self.SimpleCardWidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.SmoothScrollArea = SmoothScrollArea(self.SimpleCardWidget)
        self.SmoothScrollArea.setObjectName(u"SmoothScrollArea")
        self.SmoothScrollArea.setStyleSheet(u"background: transparent;\n"
                                            "border: none;")
        self.SmoothScrollArea.setWidgetResizable(True)
        self.SmoothScrollArea.setAlignment(Qt.AlignCenter)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(
            u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 329, 301))
        self.gridLayout_2 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.ACGKind = ComboBox(self.scrollAreaWidgetContents)
        self.ACGKind.setObjectName(u"ACGKind")
        self.ACGKind.setStyleSheet(u"ComboBox {\n"
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
        self.ACGKind.setFlat(False)
        self.ACGKind.clear()
        self.ACGKind.addItem("随机")
        self.ACGKind.addItem("精选")
        self.ACGKind.addItem("白毛")
        self.ACGKind.addItem("兽娘")
        self.ACGKind.addItem("星空")
        self.ACGKind.setCurrentIndex(0)

        self.gridLayout_2.addWidget(self.ACGKind, 4, 1, 1, 3)

        self.ACGContentKind = RadioButton(self.scrollAreaWidgetContents)
        self.ACGContentKind.setObjectName(u"ACGContentKind")
        self.ACGContentKind.setChecked(True)
        self.ACGContentKind.toggled.connect(self.ACGUseContent)

        self.gridLayout_2.addWidget(self.ACGContentKind, 2, 0, 1, 2)

        self.verticalSpacer_8 = QSpacerItem(
            20, 30, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.gridLayout_2.addItem(self.verticalSpacer_8, 9, 2, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(
            20, 20, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.gridLayout_2.addItem(self.verticalSpacer_4, 1, 2, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(
            20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_2.addItem(self.verticalSpacer_6, 5, 0, 1, 1)

        self.ACGDevicesKind = RadioButton(self.scrollAreaWidgetContents)
        self.ACGDevicesKind.setObjectName(u"ACGDevicesKind")
        self.ACGDevicesKind.toggled.connect(self.ACGUseSize)

        self.gridLayout_2.addWidget(self.ACGDevicesKind, 2, 2, 1, 2)

        self.ACGProgress = IndeterminateProgressBar(
            self.scrollAreaWidgetContents)
        self.ACGProgress.setObjectName(u"ACGProgress")
        self.ACGProgress.setVisible(False)

        self.gridLayout_2.addWidget(self.ACGProgress, 12, 0, 1, 4)

        self.ACGStart = PrimaryPushButton(self.scrollAreaWidgetContents)
        self.ACGStart.setObjectName(u"ACGStart")
        self.ACGStart.clicked.connect(
            self.ACGStartGenerator)

        self.gridLayout_2.addWidget(self.ACGStart, 10, 0, 1, 4)

        self.ACGSlider = Slider(self.scrollAreaWidgetContents)
        self.ACGSlider.setObjectName(u"ACGSlider")
        self.ACGSlider.setMinimumSize(QSize(200, 24))
        self.ACGSlider.setOrientation(Qt.Horizontal)
        self.ACGSlider.setRange(1, 100)  # 设置最小值为 1，最大值为 100
        self.ACGSlider.setSingleStep(1)  # 设置每次滑动的间隔为 1

        self.ACGSlider.valueChanged.connect(self.ACG_Sl_ValueChanged)

        self.gridLayout_2.addWidget(self.ACGSlider, 8, 0, 1, 4)

        self.verticalSpacer_5 = QSpacerItem(
            20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_2.addItem(self.verticalSpacer_5, 3, 0, 1, 1)

        self.verticalSpacer_21 = QSpacerItem(
            10, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_2.addItem(self.verticalSpacer_21, 11, 0, 1, 1)

        self.SubtitleLabel = SubtitleLabel(self.scrollAreaWidgetContents)
        self.SubtitleLabel.setObjectName(u"SubtitleLabel")
        font2 = QFont()
        font2.setFamilies([u"HarmonyOS Sans SC"])
        font2.setPointSize(20)
        font2.setBold(False)
        self.SubtitleLabel.setFont(font2)
        self.SubtitleLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.SubtitleLabel, 0, 0, 1, 4)

        self.verticalSpacer_7 = QSpacerItem(
            20, 0, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_2.addItem(self.verticalSpacer_7, 7, 0, 1, 1)

        self.ACGNumber = SpinBox(self.scrollAreaWidgetContents)
        self.ACGNumber.setObjectName(u"ACGNumber")
        self.ACGNumber.setMinimum(1)
        self.ACGNumber.setMaximum(100)

        self.ACGNumber.valueChanged.connect(self.ACG_Sp_ValueChanged)
        # self.ACGNumber.upButton.connect(self.ACG_Sp_ValueChanged)

        self.gridLayout_2.addWidget(self.ACGNumber, 6, 3, 1, 1)

        self.StrongBodyLabel_2 = StrongBodyLabel(self.scrollAreaWidgetContents)
        self.StrongBodyLabel_2.setObjectName(u"StrongBodyLabel_2")
        font3 = QFont()
        font3.setFamilies([u"HarmonyOS Sans SC"])
        font3.setPointSize(16)
        font3.setBold(False)
        self.StrongBodyLabel_2.setFont(font3)

        self.gridLayout_2.addWidget(self.StrongBodyLabel_2, 6, 0, 1, 3)

        self.StrongBodyLabel = StrongBodyLabel(self.scrollAreaWidgetContents)
        self.StrongBodyLabel.setObjectName(u"StrongBodyLabel")
        self.StrongBodyLabel.setFont(font3)

        self.gridLayout_2.addWidget(self.StrongBodyLabel, 4, 0, 1, 1)

        self.verticalSpacer_9 = QSpacerItem(
            20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_9, 13, 0, 1, 1)

        self.SmoothScrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_3.addWidget(self.SmoothScrollArea)

        self.horizontalLayout_2.addWidget(self.SimpleCardWidget)

        self.widget = QWidget(self.page_2)
        self.widget.setObjectName(u"widget")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QSize(361, 0))
        self.widget.setLayoutDirection(Qt.LeftToRight)
        self.widget.setAutoFillBackground(False)
        self.widget.setStyleSheet(u"QVBoxLayout {\n"
                                  "    alignment: center;\n"
                                  "}")
        self.verticalLayout_4 = QVBoxLayout(self.widget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_4.setContentsMargins(-1, 1, -1, -1)
        self.ElevatedCardWidget = ElevatedCardWidget(self.widget)
        self.ElevatedCardWidget.setObjectName(u"ElevatedCardWidget")
        self.ElevatedCardWidget.setMinimumSize(QSize(0, 450))
        self.ElevatedCardWidget.setMaximumSize(QSize(16777215, 16777215))
        self.gridLayout_3 = QVBoxLayout(self.ElevatedCardWidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.ACGImages = HorizontalFlipView(self.ElevatedCardWidget)
        self.ACGImages.setObjectName(u"ACGImages")
        self.ACGImages.setAspectRatioMode(Qt.AspectRatioMode.KeepAspectRatio)
        self.ACGImages.setItemAlignment(
            Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignVCenter)
        self.ACGImages.clicked.connect(
            lambda: self.ShowSetBackgroundTools(self.ACGImages))

        # self.gridLayout_3.addWidget(self.ACGImages, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.ACGImages)

        self.verticalLayout_4.addWidget(self.ElevatedCardWidget)

        self.widget_7 = QWidget(self.widget)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setMaximumSize(QSize(16777215, 51))
        self.horizontalLayout = QHBoxLayout(self.widget_7)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_5 = QSpacerItem(
            210, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_5)

        self.horizontalSpacer_9 = QSpacerItem(
            40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_9)

        self.ACGShow = HorizontalPipsPager(self.widget_7)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        QListWidgetItem(self.ACGShow)
        self.ACGShow.setObjectName(u"ACGShow")

        self.horizontalLayout.addWidget(self.ACGShow)

        self.horizontalSpacer_7 = QSpacerItem(
            210, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_7)

        self.ACGShowNumber = SpinBox(self.widget_7)
        self.ACGShowNumber.setObjectName(u"ACGShowNumber")
        self.ACGShowNumber.setMaximumSize(QSize(150, 33))
        self.ACGShowNumber.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.ACGShowNumber.setMinimum(0)
        self.ACGShowNumber.setMaximum(0)
        self.ACGShowNumber.valueChanged.connect(self.ACG_Ssp_ValueChanged)

        self.horizontalLayout.addWidget(self.ACGShowNumber)

        self.verticalLayout_4.addWidget(self.widget_7)

        # self.verticalLayout_4.addWidget(self.ACGCommandBar)

        self.horizontalLayout_2.addWidget(self.widget)

        # self.OpacityAniStackedWidget.addWidget(self.page_2)
        self.addSubInterface(self.page_2, "page_2", "ACG壁纸生成")

        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.horizontalLayout_5 = QHBoxLayout(self.page_3)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.SimpleCardWidget_2 = SimpleCardWidget(self.page_3)
        self.SimpleCardWidget_2.setObjectName(u"SimpleCardWidget_2")
        self.SimpleCardWidget_2.setMinimumSize(QSize(361, 0))
        self.SimpleCardWidget_2.setMaximumSize(QSize(361, 16777215))
        self.verticalLayout_5 = QVBoxLayout(self.SimpleCardWidget_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.SmoothScrollArea_2 = SmoothScrollArea(self.SimpleCardWidget_2)
        self.SmoothScrollArea_2.setObjectName(u"SmoothScrollArea_2")
        self.SmoothScrollArea_2.setStyleSheet(u"background: transparent;\n"
                                              "border: none;")
        self.SmoothScrollArea_2.setWidgetResizable(True)
        self.SmoothScrollArea_2.setAlignment(Qt.AlignCenter)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(
            u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 321, 379))
        self.gridLayout_4 = QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.StrongBodyLabel_4 = StrongBodyLabel(
            self.scrollAreaWidgetContents_2)
        self.StrongBodyLabel_4.setObjectName(u"StrongBodyLabel_4")
        font4 = QFont()
        font4.setFamilies([u"HarmonyOS Sans SC"])
        font4.setPointSize(14)
        font4.setBold(False)
        self.StrongBodyLabel_4.setFont(font4)

        self.gridLayout_4.addWidget(self.StrongBodyLabel_4, 4, 1, 1, 1)

        self.verticalSpacer_15 = QSpacerItem(
            20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_4.addItem(self.verticalSpacer_15, 3, 1, 1, 1)

        self.verticalSpacer_20 = QSpacerItem(
            20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_4.addItem(self.verticalSpacer_20, 5, 1, 1, 1)

        self.verticalSpacer_14 = QSpacerItem(
            20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_4.addItem(self.verticalSpacer_14, 8, 1, 1, 1)

        self.verticalSpacer_12 = QSpacerItem(
            20, 30, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.gridLayout_4.addItem(self.verticalSpacer_12, 12, 2, 1, 1)

        self.PixivNumber = SpinBox(self.scrollAreaWidgetContents_2)
        self.PixivNumber.setObjectName(u"PixivNumber")
        self.PixivNumber.setMinimum(1)
        self.PixivNumber.setMaximum(15)

        self.PixivNumber.valueChanged.connect(self.Pixiv_Sp_ValueChanged)

        self.gridLayout_4.addWidget(self.PixivNumber, 9, 3, 1, 1)

        self.verticalSpacer_13 = QSpacerItem(
            20, 20, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.gridLayout_4.addItem(self.verticalSpacer_13, 1, 2, 1, 1)

        self.verticalSpacer_22 = QSpacerItem(
            10, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_4.addItem(self.verticalSpacer_22, 14, 1, 1, 1)

        self.PixivTags = LineEdit(self.scrollAreaWidgetContents_2)
        self.PixivTags.setObjectName(u"PixivTags")

        self.gridLayout_4.addWidget(self.PixivTags, 7, 1, 1, 3)

        self.verticalSpacer_17 = QSpacerItem(
            20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_17, 16, 1, 1, 1)

        self.PixivIsR18 = CheckBox(self.scrollAreaWidgetContents_2)
        self.PixivIsR18.setObjectName(u"PixivIsR18")
        font5 = QFont()
        font5.setFamilies([u"Segoe UI"])
        font5.setBold(False)
        font5.setItalic(False)
        self.PixivIsR18.setFont(font5)
        self.PixivIsR18.setStyleSheet(u"CheckBox {\n"
                                      "    color: black;\n"
                                      "    font: 14px 'Segoe UI', 'Microsoft YaHei', 'PingFang SC';\n"
                                      "    spacing: 8px;\n"
                                      "    min-width: 28px;\n"
                                      "    min-height: 22px;\n"
                                      "    outline: none;\n"
                                      "    margin-left: 1px;\n"
                                      "}\n"
                                      "\n"
                                      "CheckBox::indicator {\n"
                                      "    width: 18px;\n"
                                      "    height: 18px;\n"
                                      "    border-radius: 5px;\n"
                                      "    border: 1px solid rgba(0, 0, 0, 0.48);\n"
                                      "    background-color: rgba(0, 0, 0, 0.022);\n"
                                      "}\n"
                                      "\n"
                                      "CheckBox::indicator:hover {\n"
                                      "    border: 1px solid rgba(0, 0, 0, 0.56);\n"
                                      "    background-color: rgba(0, 0, 0, 0.05);\n"
                                      "}\n"
                                      "\n"
                                      "CheckBox::indicator:pressed {\n"
                                      "    border: 1px solid rgba(0, 0, 0, 0.27);\n"
                                      "    background-color: rgba(0, 0, 0, 0.12);\n"
                                      "}\n"
                                      "\n"
                                      "CheckBox::indicator:checked,\n"
                                      "CheckBox::indicator:indeterminate {\n"
                                      "    border: 1px solid #0096fa;\n"
                                      "    background-color: #0096fa;\n"
                                      "}\n"
                                      "\n"
                                      "\n"
                                      "CheckBox::indicator:checked:hover,\n"
                                      "CheckBox::indicator:indeterminate:hover {\n"
                                      "    border: 1px solid #0096fa;\n"
                                      "    background-color: #0096fa;\n"
                                      ""
                                      "}\n"
                                      "\n"
                                      "CheckBox::indicator:checked:pressed,\n"
                                      "CheckBox::indicator:indeterminate:pressed {\n"
                                      "    border: 1px solid #19a0fa;\n"
                                      "    background-color: #19a0fa;\n"
                                      "}\n"
                                      "\n"
                                      "CheckBox:disabled {\n"
                                      "    color: rgba(0, 0, 0, 110);\n"
                                      "}\n"
                                      "\n"
                                      "CheckBox::indicator:disabled {\n"
                                      "    border: 1px solid rgba(0, 0, 0, 0.27);\n"
                                      "    background-color: transparent;\n"
                                      "}\n"
                                      "\n"
                                      "CheckBox::indicator:checked:disabled,\n"
                                      "CheckBox::indicator:indeterminate:disabled {\n"
                                      "    border: 1px solid rgb(199, 199, 199);\n"
                                      "    background-color: rgb(199, 199, 199);\n"
                                      "}")

        self.gridLayout_4.addWidget(self.PixivIsR18, 2, 2, 1, 2)

        self.StrongBodyLabel_3 = StrongBodyLabel(
            self.scrollAreaWidgetContents_2)
        self.StrongBodyLabel_3.setObjectName(u"StrongBodyLabel_3")
        self.StrongBodyLabel_3.setFont(font4)

        self.gridLayout_4.addWidget(self.StrongBodyLabel_3, 9, 1, 1, 2)

        self.PixivProgress = IndeterminateProgressBar(
            self.scrollAreaWidgetContents_2)
        self.PixivProgress.setObjectName(u"PixivProgress")
        self.PixivProgress.setCustomBarColor(
            QColor(0, 150, 250), QColor(0, 150, 250))
        self.PixivProgress.setVisible(False)

        self.gridLayout_4.addWidget(self.PixivProgress, 15, 1, 1, 3)

        self.StrongBodyLabel_5 = StrongBodyLabel(
            self.scrollAreaWidgetContents_2)
        self.StrongBodyLabel_5.setObjectName(u"StrongBodyLabel_5")
        self.StrongBodyLabel_5.setFont(font4)
        self.StrongBodyLabel_5.setProperty("lightColor", QColor(0, 0, 0))

        self.gridLayout_4.addWidget(self.StrongBodyLabel_5, 6, 1, 1, 3)

        self.verticalSpacer_16 = QSpacerItem(
            20, 0, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_4.addItem(self.verticalSpacer_16, 10, 1, 1, 1)

        self.PixivStart = PrimaryPushButton(self.scrollAreaWidgetContents_2)
        self.PixivStart.setObjectName(u"PixivStart")
        self.PixivStart.setStyleSheet(u"PushButton, ToolButton, ToggleButton, ToggleToolButton {\n"
                                      "    color: black;\n"
                                      "    background: rgba(255, 255, 255, 0.7);\n"
                                      "    border: 1px solid rgba(0, 0, 0, 0.073);\n"
                                      "    border-bottom: 1px solid rgba(0, 0, 0, 0.183);\n"
                                      "    border-radius: 5px;\n"
                                      "    /* font: 14px 'Segoe UI', 'Microsoft YaHei'; */\n"
                                      "    padding: 5px 12px 6px 12px;\n"
                                      "    outline: none;\n"
                                      "}\n"
                                      "\n"
                                      "ToolButton {\n"
                                      "    padding: 5px 9px 6px 8px;\n"
                                      "}\n"
                                      "\n"
                                      "PushButton[hasIcon=false] {\n"
                                      "    padding: 5px 12px 6px 12px;\n"
                                      "}\n"
                                      "\n"
                                      "PushButton[hasIcon=true] {\n"
                                      "    padding: 5px 12px 6px 36px;\n"
                                      "}\n"
                                      "\n"
                                      "DropDownToolButton, PrimaryDropDownToolButton {\n"
                                      "    padding: 5px 31px 6px 8px;\n"
                                      "}\n"
                                      "\n"
                                      "DropDownPushButton[hasIcon=false],\n"
                                      "PrimaryDropDownPushButton[hasIcon=false] {\n"
                                      "    padding: 5px 31px 6px 12px;\n"
                                      "}\n"
                                      "\n"
                                      "DropDownPushButton[hasIcon=true],\n"
                                      "PrimaryDropDownPushButton[hasIcon=true] {\n"
                                      "    padding: 5px 31px 6px 36px;\n"
                                      "}\n"
                                      "\n"
                                      "PushButton:hover, ToolButton:hover, ToggleButton:hover, To"
                                      "ggleToolButton:hover {\n"
                                      "    background: rgba(249, 249, 249, 0.5);\n"
                                      "}\n"
                                      "\n"
                                      "PushButton:pressed, ToolButton:pressed, ToggleButton:pressed, ToggleToolButton:pressed {\n"
                                      "    color: rgba(0, 0, 0, 0.63);\n"
                                      "    background: rgba(249, 249, 249, 0.3);\n"
                                      "    border-bottom: 1px solid rgba(0, 0, 0, 0.073);\n"
                                      "}\n"
                                      "\n"
                                      "PushButton:disabled, ToolButton:disabled, ToggleButton:disabled, ToggleToolButton:disabled {\n"
                                      "    color: rgba(0, 0, 0, 0.36);\n"
                                      "    background: rgba(249, 249, 249, 0.3);\n"
                                      "    border: 1px solid rgba(0, 0, 0, 0.06);\n"
                                      "    border-bottom: 1px solid rgba(0, 0, 0, 0.06);\n"
                                      "}\n"
                                      "\n"
                                      "\n"
                                      "PrimaryPushButton,\n"
                                      "PrimaryToolButton,\n"
                                      "ToggleButton:checked,\n"
                                      "ToggleToolButton:checked {\n"
                                      "    color: white;\n"
                                      "    background-color: #0096fa;\n"
                                      "    border: 1px solid #19a0fa;\n"
                                      "    border-bottom: 1px solid #64befa;\n"
                                      "}\n"
                                      "\n"
                                      "PrimaryPushButton:hover,\n"
                                      "PrimaryToolButton:hover,\n"
                                      "ToggleButton:checked:hover,\n"
                                      "ToggleToolButton:checked:hover {\n"
                                      "    background-color: #19a0fa"
                                      ";\n"
                                      "    border: 1px solid #19a0fa;\n"
                                      "    border-bottom: 1px solid #64befa;\n"
                                      "}\n"
                                      "\n"
                                      "PrimaryPushButton:pressed,\n"
                                      "PrimaryToolButton:pressed,\n"
                                      "ToggleButton:checked:pressed,\n"
                                      "ToggleToolButton:checked:pressed {\n"
                                      "    color: rgba(255, 255, 255, 0.63);\n"
                                      "    background-color: #19a0fa;\n"
                                      "    border: 1px solid #19a0fa;\n"
                                      "}\n"
                                      "\n"
                                      "PrimaryPushButton:disabled,\n"
                                      "PrimaryToolButton:disabled,\n"
                                      "ToggleButton:checked:disabled,\n"
                                      "ToggleToolButton:checked:disabled {\n"
                                      "    color: rgba(255, 255, 255, 0.9);\n"
                                      "    background-color: rgb(205, 205, 205);\n"
                                      "    border: 1px solid rgb(205, 205, 205);\n"
                                      "}\n"
                                      "\n"
                                      "SplitDropButton,\n"
                                      "PrimarySplitDropButton {\n"
                                      "    border-left: none;\n"
                                      "    border-top-left-radius: 0;\n"
                                      "    border-bottom-left-radius: 0;\n"
                                      "}\n"
                                      "\n"
                                      "#splitPushButton,\n"
                                      "#splitToolButton,\n"
                                      "#primarySplitPushButton,\n"
                                      "#primarySplitToolButton {\n"
                                      "    border-top-right-radius: 0;\n"
                                      "    border-bottom-right-radius: 0;\n"
                                      "}\n"
                                      "\n"
                                      "#splitPushButton:pressed,\n"
                                      "#splitTool"
                                      "Button:pressed,\n"
                                      "SplitDropButton:pressed {\n"
                                      "    border-bottom: 1px solid rgba(0, 0, 0, 0.183);\n"
                                      "}\n"
                                      "\n"
                                      "PrimarySplitDropButton:pressed {\n"
                                      "    border-bottom: 1px solid #64befa;\n"
                                      "}\n"
                                      "\n"
                                      "#primarySplitPushButton, #primarySplitToolButton {\n"
                                      "    border-right: 1px solid #19a0fa;\n"
                                      "}\n"
                                      "\n"
                                      "#primarySplitPushButton:pressed, #primarySplitToolButton:pressed {\n"
                                      "    border-bottom: 1px solid #64befa;\n"
                                      "}\n"
                                      "\n"
                                      "HyperlinkButton {\n"
                                      "    /* font: 14px 'Segoe UI', 'Microsoft YaHei'; */\n"
                                      "    padding: 6px 12px 6px 12px;\n"
                                      "    color: #0096fa;\n"
                                      "    border: none;\n"
                                      "    border-radius: 6px;\n"
                                      "    background-color: transparent;\n"
                                      "}\n"
                                      "\n"
                                      "HyperlinkButton[hasIcon=false] {\n"
                                      "    padding: 6px 12px 6px 12px;\n"
                                      "}\n"
                                      "\n"
                                      "HyperlinkButton[hasIcon=true] {\n"
                                      "    padding: 6px 12px 6px 36px;\n"
                                      "}\n"
                                      "\n"
                                      "HyperlinkButton:hover {\n"
                                      "    color: #0096fa;\n"
                                      "    background-color: rgba(0, 0, 0, 10);\n"
                                      "    border: none;\n"
                                      "}\n"
                                      "\n"
                                      "HyperlinkButton:pressed {\n"
                                      "    color: #0096fa;\n"
                                      ""
                                      "    background-color: rgba(0, 0, 0, 6);\n"
                                      "    border: none;\n"
                                      "}\n"
                                      "\n"
                                      "HyperlinkButton:disabled {\n"
                                      "    color: rgba(0, 0, 0, 0.43);\n"
                                      "    background-color: transparent;\n"
                                      "    border: none;\n"
                                      "}\n"
                                      "\n"
                                      "\n"
                                      "RadioButton {\n"
                                      "    min-height: 24px;\n"
                                      "    max-height: 24px;\n"
                                      "    background-color: transparent;\n"
                                      "    font: 14px 'Segoe UI', 'Microsoft YaHei', 'PingFang SC';\n"
                                      "    color: black;\n"
                                      "}\n"
                                      "\n"
                                      "RadioButton::indicator {\n"
                                      "    width: 18px;\n"
                                      "    height: 18px;\n"
                                      "    border-radius: 11px;\n"
                                      "    border: 2px solid #999999;\n"
                                      "    background-color: rgba(0, 0, 0, 5);\n"
                                      "    margin-right: 4px;\n"
                                      "}\n"
                                      "\n"
                                      "RadioButton::indicator:hover {\n"
                                      "    background-color: rgba(0, 0, 0, 0);\n"
                                      "}\n"
                                      "\n"
                                      "RadioButton::indicator:pressed {\n"
                                      "    border: 2px solid #bbbbbb;\n"
                                      "    background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5,\n"
                                      "            stop:0 rgb(255, 255, 255),\n"
                                      "            stop:0.5 rgb(255, 255, 255),\n"
                                      "            stop:0.6 rgb(225, 2"
                                      "24, 223),\n"
                                      "            stop:1 rgb(225, 224, 223));\n"
                                      "}\n"
                                      "\n"
                                      "RadioButton::indicator:checked {\n"
                                      "    height: 22px;\n"
                                      "    width: 22px;\n"
                                      "    border: none;\n"
                                      "    border-radius: 11px;\n"
                                      "    background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5,\n"
                                      "            stop:0 rgb(255, 255, 255),\n"
                                      "            stop:0.5 rgb(255, 255, 255),\n"
                                      "            stop:0.6 #0096fa,\n"
                                      "            stop:1 #0096fa);\n"
                                      "}\n"
                                      "\n"
                                      "RadioButton::indicator:checked:hover {\n"
                                      "    background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5,\n"
                                      "            stop:0 rgb(255, 255, 255),\n"
                                      "            stop:0.6 rgb(255, 255, 255),\n"
                                      "            stop:0.7 #0096fa,\n"
                                      "            stop:1 #0096fa);\n"
                                      "}\n"
                                      "\n"
                                      "RadioButton::indicator:checked:pressed {\n"
                                      "    background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5,\n"
                                      "            stop:0 rgb(255, 255, 255),\n"
                                      "            stop:0.5 rgb(255, 255, 255),\n"
                                      "            stop:0.6 #0"
                                      "096fa,\n"
                                      "            stop:1 #0096fa);\n"
                                      "}\n"
                                      "\n"
                                      "RadioButton:disabled {\n"
                                      "    color: rgba(0, 0, 0, 110);\n"
                                      "}\n"
                                      "\n"
                                      "RadioButton::indicator:disabled {\n"
                                      "    border: 2px solid #bbbbbb;\n"
                                      "    background-color: transparent;\n"
                                      "}\n"
                                      "\n"
                                      "RadioButton::indicator:disabled:checked {\n"
                                      "    border: none;\n"
                                      "    background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5,\n"
                                      "            stop:0 rgb(255, 255, 255),\n"
                                      "            stop:0.5 rgb(255, 255, 255),\n"
                                      "            stop:0.6 rgba(0, 0, 0, 0.2169),\n"
                                      "            stop:1 rgba(0, 0, 0, 0.2169));\n"
                                      "}\n"
                                      "\n"
                                      "TransparentToolButton,\n"
                                      "TransparentToggleToolButton,\n"
                                      "TransparentDropDownToolButton,\n"
                                      "TransparentPushButton,\n"
                                      "TransparentDropDownPushButton,\n"
                                      "TransparentTogglePushButton {\n"
                                      "    background-color: transparent;\n"
                                      "    border: none;\n"
                                      "    border-radius: 5px;\n"
                                      "    margin: 0;\n"
                                      "}\n"
                                      "\n"
                                      "TransparentToolButton:hover,\n"
                                      "TransparentToggleToolButton:hover,\n"
                                      "TransparentDropDownToolButton:ho"
                                      "ver,\n"
                                      "TransparentPushButton:hover,\n"
                                      "TransparentDropDownPushButton:hover,\n"
                                      "TransparentTogglePushButton:hover {\n"
                                      "    background-color: rgba(0, 0, 0, 9);\n"
                                      "    border: none;\n"
                                      "}\n"
                                      "\n"
                                      "TransparentToolButton:pressed,\n"
                                      "TransparentToggleToolButton:pressed,\n"
                                      "TransparentDropDownToolButton:pressed,\n"
                                      "TransparentPushButton:pressed,\n"
                                      "TransparentDropDownPushButton:pressed,\n"
                                      "TransparentTogglePushButton:pressed {\n"
                                      "    background-color: rgba(0, 0, 0, 6);\n"
                                      "    border: none;\n"
                                      "}\n"
                                      "\n"
                                      "TransparentToolButton:disabled,\n"
                                      "TransparentToggleToolButton:disabled,\n"
                                      "TransparentDropDownToolButton:disabled,\n"
                                      "TransprentPushButton:disabled,\n"
                                      "TransparentDropDownPushButton:disabled,\n"
                                      "TransprentTogglePushButton:disabled {\n"
                                      "    background-color: transparent;\n"
                                      "    border: none;\n"
                                      "}\n"
                                      "\n"
                                      "\n"
                                      "PillPushButton,\n"
                                      "PillPushButton:hover,\n"
                                      "PillPushButton:pressed,\n"
                                      "PillPushButton:disabled,\n"
                                      "PillPushButton:checked,\n"
                                      "PillPushButton:checked:hover,\n"
                                      "PillPushButton:checked:p"
                                      "ressed,\n"
                                      "PillPushButton:disabled:checked,\n"
                                      "PillToolButton,\n"
                                      "PillToolButton:hover,\n"
                                      "PillToolButton:pressed,\n"
                                      "PillToolButton:disabled,\n"
                                      "PillToolButton:checked,\n"
                                      "PillToolButton:checked:hover,\n"
                                      "PillToolButton:checked:pressed,\n"
                                      "PillToolButton:disabled:checked {\n"
                                      "    background-color: transparent;\n"
                                      "    border: none;\n"
                                      "}\n"
                                      "")
        self.PixivStart.clicked.connect(
            lambda: asyncio.run(self.PixivStartGenerator()))

        self.gridLayout_4.addWidget(self.PixivStart, 13, 1, 1, 3)

        self.SubtitleLabel_2 = SubtitleLabel(self.scrollAreaWidgetContents_2)
        self.SubtitleLabel_2.setObjectName(u"SubtitleLabel_2")
        font6 = QFont()
        font6.setFamilies([u"\u9489\u9489\u8fdb\u6b65\u4f53"])
        font6.setPointSize(20)
        font6.setBold(False)
        self.SubtitleLabel_2.setFont(font6)
        self.SubtitleLabel_2.setAlignment(Qt.AlignCenter)
        self.SubtitleLabel_2.setProperty("lightColor", QColor(0, 150, 250))

        self.gridLayout_4.addWidget(self.SubtitleLabel_2, 0, 1, 1, 3)

        self.PixivIsAI = CheckBox(self.scrollAreaWidgetContents_2)
        self.PixivIsAI.setObjectName(u"PixivIsAI")
        self.PixivIsAI.setFont(font5)
        self.PixivIsAI.setStyleSheet(u"CheckBox {\n"
                                     "    color: black;\n"
                                     "    font: 14px 'Segoe UI', 'Microsoft YaHei', 'PingFang SC';\n"
                                     "    spacing: 8px;\n"
                                     "    min-width: 28px;\n"
                                     "    min-height: 22px;\n"
                                     "    outline: none;\n"
                                     "    margin-left: 1px;\n"
                                     "}\n"
                                     "\n"
                                     "CheckBox::indicator {\n"
                                     "    width: 18px;\n"
                                     "    height: 18px;\n"
                                     "    border-radius: 5px;\n"
                                     "    border: 1px solid rgba(0, 0, 0, 0.48);\n"
                                     "    background-color: rgba(0, 0, 0, 0.022);\n"
                                     "}\n"
                                     "\n"
                                     "CheckBox::indicator:hover {\n"
                                     "    border: 1px solid rgba(0, 0, 0, 0.56);\n"
                                     "    background-color: rgba(0, 0, 0, 0.05);\n"
                                     "}\n"
                                     "\n"
                                     "CheckBox::indicator:pressed {\n"
                                     "    border: 1px solid rgba(0, 0, 0, 0.27);\n"
                                     "    background-color: rgba(0, 0, 0, 0.12);\n"
                                     "}\n"
                                     "\n"
                                     "CheckBox::indicator:checked,\n"
                                     "CheckBox::indicator:indeterminate {\n"
                                     "    border: 1px solid #0096fa;\n"
                                     "    background-color: #0096fa;\n"
                                     "}\n"
                                     "\n"
                                     "\n"
                                     "CheckBox::indicator:checked:hover,\n"
                                     "CheckBox::indicator:indeterminate:hover {\n"
                                     "    border: 1px solid #00a7b3;\n"
                                     "    background-color: #00a7b3;\n"
                                     ""
                                     "}\n"
                                     "\n"
                                     "CheckBox::indicator:checked:pressed,\n"
                                     "CheckBox::indicator:indeterminate:pressed {\n"
                                     "    border: 1px solid #3eabb3;\n"
                                     "    background-color: #3eabb3;\n"
                                     "}\n"
                                     "\n"
                                     "CheckBox:disabled {\n"
                                     "    color: rgba(0, 0, 0, 110);\n"
                                     "}\n"
                                     "\n"
                                     "CheckBox::indicator:disabled {\n"
                                     "    border: 1px solid rgba(0, 0, 0, 0.27);\n"
                                     "    background-color: transparent;\n"
                                     "}\n"
                                     "\n"
                                     "CheckBox::indicator:checked:disabled,\n"
                                     "CheckBox::indicator:indeterminate:disabled {\n"
                                     "    border: 1px solid rgb(199, 199, 199);\n"
                                     "    background-color: rgb(199, 199, 199);\n"
                                     "}")

        self.gridLayout_4.addWidget(self.PixivIsAI, 2, 1, 1, 1)

        self.PixivUID = LineEdit(self.scrollAreaWidgetContents_2)
        self.PixivUID.setObjectName(u"PixivUID")

        self.gridLayout_4.addWidget(self.PixivUID, 4, 2, 1, 2)

        self.PixivSlider = Slider(self.scrollAreaWidgetContents_2)
        self.PixivSlider.setObjectName(u"PixivSlider")
        self.PixivSlider.setMinimumSize(QSize(200, 24))
        self.PixivSlider.setOrientation(Qt.Horizontal)
        self.PixivSlider.setRange(1, 15)  # 设置最小值为 1，最大值为 100
        self.PixivSlider.setSingleStep(1)  # 设置每次滑动的间隔为 1

        self.PixivSlider.valueChanged.connect(self.Pixiv_Sl_ValueChanged)

        self.gridLayout_4.addWidget(self.PixivSlider, 11, 1, 1, 3)

        self.SmoothScrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_5.addWidget(self.SmoothScrollArea_2)

        self.HyperlinkLabel = HyperlinkLabel(self.SimpleCardWidget_2)
        self.HyperlinkLabel.setObjectName(u"HyperlinkLabel")
        font7 = QFont()
        font7.setFamilies([u"HarmonyOS Sans SC"])
        font7.setPointSize(11)
        font7.setBold(True)
        font7.setUnderline(False)
        font7.setStrikeOut(False)
        self.HyperlinkLabel.setFont(font7)
        self.HyperlinkLabel.setStyleSheet(u"HyperlinkLabel {\n"
                                          "    color: #0096fa;\n"
                                          "    border: none;\n"
                                          "    background-color: transparent;\n"
                                          "    text-align: left;\n"
                                          "    padding: 0;\n"
                                          "    margin: 0;\n"
                                          "}\n"
                                          "\n"
                                          "HyperlinkLabel[underline=true] {\n"
                                          "    text-decoration: underline;\n"
                                          "}\n"
                                          "\n"
                                          "HyperlinkLabel[underline=false] {\n"
                                          "    text-decoration: none;\n"
                                          "}\n"
                                          "\n"
                                          "HyperlinkLabel:hover {\n"
                                          "    color: #007780;\n"
                                          "}\n"
                                          "\n"
                                          "HyperlinkLabel:pressed {\n"
                                          "    color: #00a7b3;\n"
                                          "}")
        self.HyperlinkLabel.clicked.connect(self.PixivshowDialog)

        self.verticalLayout_5.addWidget(self.HyperlinkLabel)

        self.horizontalLayout_5.addWidget(self.SimpleCardWidget_2)

        self.widget_2 = QWidget(self.page_3)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy.setHeightForWidth(
            self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setMinimumSize(QSize(361, 0))
        self.widget_2.setLayoutDirection(Qt.LeftToRight)
        self.widget_2.setAutoFillBackground(False)
        self.widget_2.setStyleSheet(u"QVBoxLayout {\n"
                                    "    alignment: center;\n"
                                    "}")
        self.verticalLayout_6 = QVBoxLayout(self.widget_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_6.setContentsMargins(-1, 1, -1, -1)
        self.ElevatedCardWidget_2 = ElevatedCardWidget(self.widget_2)
        self.ElevatedCardWidget_2.setObjectName(u"ElevatedCardWidget_2")
        self.ElevatedCardWidget_2.setMinimumSize(QSize(361, 450))
        self.ElevatedCardWidget_2.setMaximumSize(QSize(16777215, 16777215))
        self.gridLayout_5 = QGridLayout(self.ElevatedCardWidget_2)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.PixivImages = HorizontalFlipView(self.ElevatedCardWidget_2)
        self.PixivImages.setAspectRatioMode(Qt.AspectRatioMode.KeepAspectRatio)
        self.PixivImages.setItemAlignment(
            Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignVCenter)
        self.PixivImages.setObjectName(u"PixivImages")
        self.PixivImages.clicked.connect(
            lambda: self.ShowSetBackgroundPixiv(self.PixivImages))

        self.gridLayout_5.addWidget(self.PixivImages, 0, 0, 1, 1)

        self.verticalLayout_6.addWidget(self.ElevatedCardWidget_2)

        self.widget_6 = QWidget(self.widget_2)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setMaximumSize(QSize(16777215, 51))
        self.horizontalLayout_4 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_8 = QSpacerItem(
            210, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_8)

        self.horizontalSpacer_6 = QSpacerItem(
            40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_6)

        self.PixivShow = HorizontalPipsPager(self.widget_6)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        QListWidgetItem(self.PixivShow)
        self.PixivShow.setObjectName(u"PixivShow")

        self.horizontalLayout_4.addWidget(self.PixivShow)

        self.horizontalSpacer_10 = QSpacerItem(
            210, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_10)

        self.PixivShowNumber = SpinBox(self.widget_6)
        self.PixivShowNumber.setObjectName(u"PixivShowNumber")
        self.PixivShowNumber.setMaximumSize(QSize(150, 33))
        self.PixivShowNumber.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.PixivShowNumber.setMinimum(0)
        self.PixivShowNumber.setMaximum(0)
        self.PixivShowNumber.valueChanged.connect(self.Pixiv_Ssp_ValueChanged)

        self.horizontalLayout_4.addWidget(self.PixivShowNumber)

        self.verticalLayout_6.addWidget(self.widget_6)

        # self.PixivCommandBar = CommandBar(self.widget_2)
        # self.PixivCommandBar.setObjectName(u"PixivCommandBar")
        # self.PixivCommandBar.setMinimumSize(QSize(1, 34))
        # self.PixivCommandBar.setLayoutDirection(Qt.LeftToRight)
        # self.PixivCommandBar.setAutoFillBackground(False)
        # self.PixivCommandBar.setFrameShape(QFrame.NoFrame)
        # self.PixivCommandBar.setFrameShadow(QFrame.Plain)

        # self.verticalLayout_6.addWidget(self.PixivCommandBar)

        self.horizontalLayout_5.addWidget(self.widget_2)

        # self.OpacityAniStackedWidget.addWidget(self.page_3)
        self.addSubInterface(self.page_3, "page_3", "Pixiv生成器")

        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.horizontalLayout_7 = QHBoxLayout(self.page_5)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.SimpleCardWidget_4 = SimpleCardWidget(self.page_5)
        self.SimpleCardWidget_4.setObjectName(u"SimpleCardWidget_4")
        self.SimpleCardWidget_4.setMinimumSize(QSize(380, 0))
        self.SimpleCardWidget_4.setMaximumSize(QSize(361, 16777215))
        self.verticalLayout_9 = QVBoxLayout(self.SimpleCardWidget_4)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.AIPages = SegmentedToolWidget(self.SimpleCardWidget_4)
        self.AIPages.setObjectName(u"AIPages")

        self.verticalLayout_9.addWidget(self.AIPages)

        self.OpacityAniStackedWidget_2 = PopUpAniStackedWidget(
            self.SimpleCardWidget_4)
        self.OpacityAniStackedWidget_2.setObjectName(
            u"OpacityAniStackedWidget_2")
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.gridLayout_10 = QGridLayout(self.page_6)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.SmoothScrollArea_3 = SmoothScrollArea(self.page_6)
        self.SmoothScrollArea_3.setObjectName(u"SmoothScrollArea_3")
        self.SmoothScrollArea_3.setStyleSheet(u"background: transparent;\n"
                                              "border: none;")
        self.SmoothScrollArea_3.setWidgetResizable(True)
        self.SmoothScrollArea_3.setAlignment(Qt.AlignCenter)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(
            u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 338, 765))
        self.gridLayout_9 = QGridLayout(self.scrollAreaWidgetContents_3)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.verticalSpacer_36 = QSpacerItem(
            20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_9.addItem(self.verticalSpacer_36, 27, 1, 1, 1)

        self.SubtitleLabel_5 = SubtitleLabel(self.scrollAreaWidgetContents_3)
        self.SubtitleLabel_5.setObjectName(u"SubtitleLabel_5")
        self.SubtitleLabel_5.setFont(font6)
        self.SubtitleLabel_5.setStyleSheet(
            u"color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(170, 58, 217, 255), stop:1 rgba(106, 55, 233, 255));")
        self.SubtitleLabel_5.setAlignment(Qt.AlignCenter)
        self.SubtitleLabel_5.setProperty("lightColor", QColor(139, 43, 231))

        self.gridLayout_9.addWidget(self.SubtitleLabel_5, 1, 1, 1, 3)

        self.StrongBodyLabel_7 = StrongBodyLabel(
            self.scrollAreaWidgetContents_3)
        self.StrongBodyLabel_7.setObjectName(u"StrongBodyLabel_7")
        self.StrongBodyLabel_7.setFont(font4)

        self.gridLayout_9.addWidget(self.StrongBodyLabel_7, 10, 1, 1, 1)

        self.verticalSpacer_39 = QSpacerItem(
            20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_9.addItem(self.verticalSpacer_39, 24, 1, 1, 1)

        self.verticalSpacer_38 = QSpacerItem(
            20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_9.addItem(self.verticalSpacer_38, 13, 1, 1, 1)

        self.verticalSpacer_32 = QSpacerItem(
            20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_9.addItem(self.verticalSpacer_32, 5, 1, 1, 1)

        self.AISteps = DoubleSpinBox(self.scrollAreaWidgetContents_3)
        self.AISteps.setObjectName(u"AISteps")
        self.AISteps.setStyleSheet(u"SpinBox, DoubleSpinBox, DateEdit, DateTimeEdit, TimeEdit,\n"
                                   "CompactSpinBox,\n"
                                   "CompactDoubleSpinBox,\n"
                                   "CompactDateEdit,\n"
                                   "CompactDateTimeEdit,\n"
                                   "CompactTimeEdit {\n"
                                   "    color: black;\n"
                                   "    background-color: rgba(255, 255, 255, 0.7);\n"
                                   "    border: 1px solid rgba(0, 0, 0, 13);\n"
                                   "    border-bottom: 1px solid rgba(0, 0, 0, 100);\n"
                                   "    border-radius: 5px;\n"
                                   "    /* font: 14px \"Segoe UI\", \"Microsoft YaHei\"; */\n"
                                   "    padding: 0px 80px 0 10px;\n"
                                   "    selection-background-color: #8b2be7;\n"
                                   "}\n"
                                   "\n"
                                   "CompactSpinBox,\n"
                                   "CompactDoubleSpinBox,\n"
                                   "CompactDateEdit,\n"
                                   "CompactDateTimeEdit,\n"
                                   "CompactTimeEdit {\n"
                                   "    padding: 0px 26px 0 10px;\n"
                                   "}\n"
                                   "\n"
                                   "SpinBox:hover,\n"
                                   "DoubleSpinBox:hover,\n"
                                   "DateEdit:hover,\n"
                                   "DateTimeEdit:hover,\n"
                                   "TimeEdit:hover,\n"
                                   "CompactSpinBox:hover,\n"
                                   "CompactDoubleSpinBox:hover,\n"
                                   "CompactDateEdit:hover,\n"
                                   "CompactDateTimeEdit:hover,\n"
                                   "CompactTimeEdit:hover {\n"
                                   "    background-color: rgba(249, 249, 249, 0.5);\n"
                                   "    border: 1px solid rgba(0, 0, 0, "
                                   "13);\n"
                                   "    border-bottom: 1px solid rgba(0, 0, 0, 100);\n"
                                   "}\n"
                                   "\n"
                                   "SpinBox:focus,\n"
                                   "DoubleSpinBox:focus,\n"
                                   "DateEdit:focus,\n"
                                   "DateTimeEdit:focus,\n"
                                   "TimeEdit:focus,\n"
                                   "CompactSpinBox:focus,\n"
                                   "CompactDoubleSpinBox:focus,\n"
                                   "CompactDateEdit:focus,\n"
                                   "CompactDateTimeEdit:focus,\n"
                                   "CompactTimeEdit:focus {\n"
                                   "    border-bottom: 1px solid rgba(0, 0, 0, 13);\n"
                                   "    background-color: white;\n"
                                   "}\n"
                                   "\n"
                                   "SpinBox:disabled,\n"
                                   "DoubleSpinBox:disabled,\n"
                                   "DateEdit:disabled,\n"
                                   "DateTimeEdit:disabled,\n"
                                   "TimeEdit:disabled,\n"
                                   "CompactSpinBox:disabled,\n"
                                   "CompactDoubleSpinBox:disabled,\n"
                                   "CompactDateEdit:disabled,\n"
                                   "CompactDateTimeEdit:disabled,\n"
                                   "CompactTimeEdit:disabled {\n"
                                   "    color: rgba(0, 0, 0, 150);\n"
                                   "    background-color: rgba(249, 249, 249, 0.5);\n"
                                   "    border: 1px solid rgba(0, 0, 0, 13);\n"
                                   "    border-bottom: 1px solid rgba(0, 0, 0, 13);\n"
                                   "}\n"
                                   "\n"
                                   "SpinButton {\n"
                                   "    background-color: transparent;\n"
                                   "    border-radius: 4px;\n"
                                   "    margin: 0;\n"
                                   "}\n"
                                   "\n"
                                   "SpinButton:ho"
                                   "ver {\n"
                                   "    background-color: rgba(0, 0, 0, 9);\n"
                                   "}\n"
                                   "\n"
                                   "SpinButton:pressed {\n"
                                   "    background-color: rgba(0, 0, 0, 6);\n"
                                   "}")
        self.AISteps.setMinimum(1)
        self.AISteps.setMaximum(2)
        self.AISteps.setSingleStep(0.01)

        self.gridLayout_9.addWidget(self.AISteps, 10, 3, 1, 1)

        self.AIObey = SpinBox(self.scrollAreaWidgetContents_3)
        self.AIObey.setObjectName(u"AIObey")
        self.AIObey.setStyleSheet(u"SpinBox, DoubleSpinBox, DateEdit, DateTimeEdit, TimeEdit,\n"
                                  "CompactSpinBox,\n"
                                  "CompactDoubleSpinBox,\n"
                                  "CompactDateEdit,\n"
                                  "CompactDateTimeEdit,\n"
                                  "CompactTimeEdit {\n"
                                  "    color: black;\n"
                                  "    background-color: rgba(255, 255, 255, 0.7);\n"
                                  "    border: 1px solid rgba(0, 0, 0, 13);\n"
                                  "    border-bottom: 1px solid rgba(0, 0, 0, 100);\n"
                                  "    border-radius: 5px;\n"
                                  "    /* font: 14px \"Segoe UI\", \"Microsoft YaHei\"; */\n"
                                  "    padding: 0px 80px 0 10px;\n"
                                  "    selection-background-color: #8b2be7;\n"
                                  "}\n"
                                  "\n"
                                  "CompactSpinBox,\n"
                                  "CompactDoubleSpinBox,\n"
                                  "CompactDateEdit,\n"
                                  "CompactDateTimeEdit,\n"
                                  "CompactTimeEdit {\n"
                                  "    padding: 0px 26px 0 10px;\n"
                                  "}\n"
                                  "\n"
                                  "SpinBox:hover,\n"
                                  "DoubleSpinBox:hover,\n"
                                  "DateEdit:hover,\n"
                                  "DateTimeEdit:hover,\n"
                                  "TimeEdit:hover,\n"
                                  "CompactSpinBox:hover,\n"
                                  "CompactDoubleSpinBox:hover,\n"
                                  "CompactDateEdit:hover,\n"
                                  "CompactDateTimeEdit:hover,\n"
                                  "CompactTimeEdit:hover {\n"
                                  "    background-color: rgba(249, 249, 249, 0.5);\n"
                                  "    border: 1px solid rgba(0, 0, 0, "
                                  "13);\n"
                                  "    border-bottom: 1px solid rgba(0, 0, 0, 100);\n"
                                  "}\n"
                                  "\n"
                                  "SpinBox:focus,\n"
                                  "DoubleSpinBox:focus,\n"
                                  "DateEdit:focus,\n"
                                  "DateTimeEdit:focus,\n"
                                  "TimeEdit:focus,\n"
                                  "CompactSpinBox:focus,\n"
                                  "CompactDoubleSpinBox:focus,\n"
                                  "CompactDateEdit:focus,\n"
                                  "CompactDateTimeEdit:focus,\n"
                                  "CompactTimeEdit:focus {\n"
                                  "    border-bottom: 1px solid rgba(0, 0, 0, 13);\n"
                                  "    background-color: white;\n"
                                  "}\n"
                                  "\n"
                                  "SpinBox:disabled,\n"
                                  "DoubleSpinBox:disabled,\n"
                                  "DateEdit:disabled,\n"
                                  "DateTimeEdit:disabled,\n"
                                  "TimeEdit:disabled,\n"
                                  "CompactSpinBox:disabled,\n"
                                  "CompactDoubleSpinBox:disabled,\n"
                                  "CompactDateEdit:disabled,\n"
                                  "CompactDateTimeEdit:disabled,\n"
                                  "CompactTimeEdit:disabled {\n"
                                  "    color: rgba(0, 0, 0, 150);\n"
                                  "    background-color: rgba(249, 249, 249, 0.5);\n"
                                  "    border: 1px solid rgba(0, 0, 0, 13);\n"
                                  "    border-bottom: 1px solid rgba(0, 0, 0, 13);\n"
                                  "}\n"
                                  "\n"
                                  "SpinButton {\n"
                                  "    background-color: transparent;\n"
                                  "    border-radius: 4px;\n"
                                  "    margin: 0;\n"
                                  "}\n"
                                  "\n"
                                  "SpinButton:ho"
                                  "ver {\n"
                                  "    background-color: rgba(0, 0, 0, 9);\n"
                                  "}\n"
                                  "\n"
                                  "SpinButton:pressed {\n"
                                  "    background-color: rgba(0, 0, 0, 6);\n"
                                  "}")
        self.AIObey.setMinimum(1)
        self.AIObey.setMaximum(10)

        self.gridLayout_9.addWidget(self.AIObey, 15, 3, 1, 1)

        self.AIStart = PrimaryPushButton(self.scrollAreaWidgetContents_3)
        self.AIStart.setObjectName(u"AIStart")
        self.AIStart.setStyleSheet(u"PushButton, ToolButton, ToggleButton, ToggleToolButton {\n"
                                   "    color: black;\n"
                                   "    background: rgba(255, 255, 255, 0.7);\n"
                                   "    border: 1px solid rgba(0, 0, 0, 0.073);\n"
                                   "    border-bottom: 1px solid rgba(0, 0, 0, 0.183);\n"
                                   "    border-radius: 5px;\n"
                                   "    /* font: 14px 'Segoe UI', 'Microsoft YaHei'; */\n"
                                   "    padding: 5px 12px 6px 12px;\n"
                                   "    outline: none;\n"
                                   "}\n"
                                   "\n"
                                   "ToolButton {\n"
                                   "    padding: 5px 9px 6px 8px;\n"
                                   "}\n"
                                   "\n"
                                   "PushButton[hasIcon=false] {\n"
                                   "    padding: 5px 12px 6px 12px;\n"
                                   "}\n"
                                   "\n"
                                   "PushButton[hasIcon=true] {\n"
                                   "    padding: 5px 12px 6px 36px;\n"
                                   "}\n"
                                   "\n"
                                   "DropDownToolButton, PrimaryDropDownToolButton {\n"
                                   "    padding: 5px 31px 6px 8px;\n"
                                   "}\n"
                                   "\n"
                                   "DropDownPushButton[hasIcon=false],\n"
                                   "PrimaryDropDownPushButton[hasIcon=false] {\n"
                                   "    padding: 5px 31px 6px 12px;\n"
                                   "}\n"
                                   "\n"
                                   "DropDownPushButton[hasIcon=true],\n"
                                   "PrimaryDropDownPushButton[hasIcon=true] {\n"
                                   "    padding: 5px 31px 6px 36px;\n"
                                   "}\n"
                                   "\n"
                                   "PushButton:hover, ToolButton:hover, ToggleButton:hover, To"
                                   "ggleToolButton:hover {\n"
                                   "    background: rgba(249, 249, 249, 0.5);\n"
                                   "}\n"
                                   "\n"
                                   "PushButton:pressed, ToolButton:pressed, ToggleButton:pressed, ToggleToolButton:pressed {\n"
                                   "    color: rgba(0, 0, 0, 0.63);\n"
                                   "    background: rgba(249, 249, 249, 0.3);\n"
                                   "    border-bottom: 1px solid rgba(0, 0, 0, 0.073);\n"
                                   "}\n"
                                   "\n"
                                   "PushButton:disabled, ToolButton:disabled, ToggleButton:disabled, ToggleToolButton:disabled {\n"
                                   "    color: rgba(0, 0, 0, 0.36);\n"
                                   "    background: rgba(249, 249, 249, 0.3);\n"
                                   "    border: 1px solid rgba(0, 0, 0, 0.06);\n"
                                   "    border-bottom: 1px solid rgba(0, 0, 0, 0.06);\n"
                                   "}\n"
                                   "\n"
                                   "\n"
                                   "PrimaryPushButton,\n"
                                   "PrimaryToolButton,\n"
                                   "ToggleButton:checked,\n"
                                   "ToggleToolButton:checked {\n"
                                   "    color: white;\n"
                                   "    background-color: #8b2be7;\n"
                                   "    border: 1px solid #b52fff;\n"
                                   "    border-bottom: 1px solid #6c21b3;\n"
                                   "}\n"
                                   "\n"
                                   "PrimaryPushButton:hover,\n"
                                   "PrimaryToolButton:hover,\n"
                                   "ToggleButton:checked:hover,\n"
                                   "ToggleToolButton:checked:hover {\n"
                                   "    background-color: #b52fff"
                                   ";\n"
                                   "    border: 1px solid #2daab3;\n"
                                   "    border-bottom: 1px solid #6c21b3;\n"
                                   "}\n"
                                   "\n"
                                   "PrimaryPushButton:pressed,\n"
                                   "PrimaryToolButton:pressed,\n"
                                   "ToggleButton:checked:pressed,\n"
                                   "ToggleToolButton:checked:pressed {\n"
                                   "    color: rgba(255, 255, 255, 0.63);\n"
                                   "    background-color: #c22fff;\n"
                                   "    border: 1px solid #c22fff;\n"
                                   "}\n"
                                   "\n"
                                   "PrimaryPushButton:disabled,\n"
                                   "PrimaryToolButton:disabled,\n"
                                   "ToggleButton:checked:disabled,\n"
                                   "ToggleToolButton:checked:disabled {\n"
                                   "    color: rgba(255, 255, 255, 0.9);\n"
                                   "    background-color: rgb(205, 205, 205);\n"
                                   "    border: 1px solid rgb(205, 205, 205);\n"
                                   "}\n"
                                   "\n"
                                   "SplitDropButton,\n"
                                   "PrimarySplitDropButton {\n"
                                   "    border-left: none;\n"
                                   "    border-top-left-radius: 0;\n"
                                   "    border-bottom-left-radius: 0;\n"
                                   "}\n"
                                   "\n"
                                   "#splitPushButton,\n"
                                   "#splitToolButton,\n"
                                   "#primarySplitPushButton,\n"
                                   "#primarySplitToolButton {\n"
                                   "    border-top-right-radius: 0;\n"
                                   "    border-bottom-right-radius: 0;\n"
                                   "}\n"
                                   "\n"
                                   "#splitPushButton:pressed,\n"
                                   "#splitTool"
                                   "Button:pressed,\n"
                                   "SplitDropButton:pressed {\n"
                                   "    border-bottom: 1px solid rgba(0, 0, 0, 0.183);\n"
                                   "}\n"
                                   "\n"
                                   "PrimarySplitDropButton:pressed {\n"
                                   "    border-bottom: 1px solid #6c21b3;\n"
                                   "}\n"
                                   "\n"
                                   "#primarySplitPushButton, #primarySplitToolButton {\n"
                                   "    border-right: 1px solid #c22fff;\n"
                                   "}\n"
                                   "\n"
                                   "#primarySplitPushButton:pressed, #primarySplitToolButton:pressed {\n"
                                   "    border-bottom: 1px solid #6c21b3;\n"
                                   "}\n"
                                   "\n"
                                   "HyperlinkButton {\n"
                                   "    /* font: 14px 'Segoe UI', 'Microsoft YaHei'; */\n"
                                   "    padding: 6px 12px 6px 12px;\n"
                                   "    color: #8b2be7;\n"
                                   "    border: none;\n"
                                   "    border-radius: 6px;\n"
                                   "    background-color: transparent;\n"
                                   "}\n"
                                   "\n"
                                   "HyperlinkButton[hasIcon=false] {\n"
                                   "    padding: 6px 12px 6px 12px;\n"
                                   "}\n"
                                   "\n"
                                   "HyperlinkButton[hasIcon=true] {\n"
                                   "    padding: 6px 12px 6px 36px;\n"
                                   "}\n"
                                   "\n"
                                   "HyperlinkButton:hover {\n"
                                   "    color: #8b2be7;\n"
                                   "    background-color: rgba(0, 0, 0, 10);\n"
                                   "    border: none;\n"
                                   "}\n"
                                   "\n"
                                   "HyperlinkButton:pressed {\n"
                                   "    color: #8b2be7;\n"
                                   ""
                                   "    background-color: rgba(0, 0, 0, 6);\n"
                                   "    border: none;\n"
                                   "}\n"
                                   "\n"
                                   "HyperlinkButton:disabled {\n"
                                   "    color: rgba(0, 0, 0, 0.43);\n"
                                   "    background-color: transparent;\n"
                                   "    border: none;\n"
                                   "}\n"
                                   "\n"
                                   "\n"
                                   "RadioButton {\n"
                                   "    min-height: 24px;\n"
                                   "    max-height: 24px;\n"
                                   "    background-color: transparent;\n"
                                   "    font: 14px 'Segoe UI', 'Microsoft YaHei', 'PingFang SC';\n"
                                   "    color: black;\n"
                                   "}\n"
                                   "\n"
                                   "RadioButton::indicator {\n"
                                   "    width: 18px;\n"
                                   "    height: 18px;\n"
                                   "    border-radius: 11px;\n"
                                   "    border: 2px solid #999999;\n"
                                   "    background-color: rgba(0, 0, 0, 5);\n"
                                   "    margin-right: 4px;\n"
                                   "}\n"
                                   "\n"
                                   "RadioButton::indicator:hover {\n"
                                   "    background-color: rgba(0, 0, 0, 0);\n"
                                   "}\n"
                                   "\n"
                                   "RadioButton::indicator:pressed {\n"
                                   "    border: 2px solid #bbbbbb;\n"
                                   "    background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5,\n"
                                   "            stop:0 rgb(255, 255, 255),\n"
                                   "            stop:0.5 rgb(255, 255, 255),\n"
                                   "            stop:0.6 rgb(225, 2"
                                   "24, 223),\n"
                                   "            stop:1 rgb(225, 224, 223));\n"
                                   "}\n"
                                   "\n"
                                   "RadioButton::indicator:checked {\n"
                                   "    height: 22px;\n"
                                   "    width: 22px;\n"
                                   "    border: none;\n"
                                   "    border-radius: 11px;\n"
                                   "    background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5,\n"
                                   "            stop:0 rgb(255, 255, 255),\n"
                                   "            stop:0.5 rgb(255, 255, 255),\n"
                                   "            stop:0.6 #8b2be7,\n"
                                   "            stop:1 #8b2be7);\n"
                                   "}\n"
                                   "\n"
                                   "RadioButton::indicator:checked:hover {\n"
                                   "    background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5,\n"
                                   "            stop:0 rgb(255, 255, 255),\n"
                                   "            stop:0.6 rgb(255, 255, 255),\n"
                                   "            stop:0.7 #8b2be7,\n"
                                   "            stop:1 #8b2be7);\n"
                                   "}\n"
                                   "\n"
                                   "RadioButton::indicator:checked:pressed {\n"
                                   "    background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5,\n"
                                   "            stop:0 rgb(255, 255, 255),\n"
                                   "            stop:0.5 rgb(255, 255, 255),\n"
                                   "            stop:0.6 #8"
                                   "b2be7,\n"
                                   "            stop:1 #8b2be7);\n"
                                   "}\n"
                                   "\n"
                                   "RadioButton:disabled {\n"
                                   "    color: rgba(0, 0, 0, 110);\n"
                                   "}\n"
                                   "\n"
                                   "RadioButton::indicator:disabled {\n"
                                   "    border: 2px solid #bbbbbb;\n"
                                   "    background-color: transparent;\n"
                                   "}\n"
                                   "\n"
                                   "RadioButton::indicator:disabled:checked {\n"
                                   "    border: none;\n"
                                   "    background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5,\n"
                                   "            stop:0 rgb(255, 255, 255),\n"
                                   "            stop:0.5 rgb(255, 255, 255),\n"
                                   "            stop:0.6 rgba(0, 0, 0, 0.2169),\n"
                                   "            stop:1 rgba(0, 0, 0, 0.2169));\n"
                                   "}\n"
                                   "\n"
                                   "TransparentToolButton,\n"
                                   "TransparentToggleToolButton,\n"
                                   "TransparentDropDownToolButton,\n"
                                   "TransparentPushButton,\n"
                                   "TransparentDropDownPushButton,\n"
                                   "TransparentTogglePushButton {\n"
                                   "    background-color: transparent;\n"
                                   "    border: none;\n"
                                   "    border-radius: 5px;\n"
                                   "    margin: 0;\n"
                                   "}\n"
                                   "\n"
                                   "TransparentToolButton:hover,\n"
                                   "TransparentToggleToolButton:hover,\n"
                                   "TransparentDropDownToolButton:ho"
                                   "ver,\n"
                                   "TransparentPushButton:hover,\n"
                                   "TransparentDropDownPushButton:hover,\n"
                                   "TransparentTogglePushButton:hover {\n"
                                   "    background-color: rgba(0, 0, 0, 9);\n"
                                   "    border: none;\n"
                                   "}\n"
                                   "\n"
                                   "TransparentToolButton:pressed,\n"
                                   "TransparentToggleToolButton:pressed,\n"
                                   "TransparentDropDownToolButton:pressed,\n"
                                   "TransparentPushButton:pressed,\n"
                                   "TransparentDropDownPushButton:pressed,\n"
                                   "TransparentTogglePushButton:pressed {\n"
                                   "    background-color: rgba(0, 0, 0, 6);\n"
                                   "    border: none;\n"
                                   "}\n"
                                   "\n"
                                   "TransparentToolButton:disabled,\n"
                                   "TransparentToggleToolButton:disabled,\n"
                                   "TransparentDropDownToolButton:disabled,\n"
                                   "TransprentPushButton:disabled,\n"
                                   "TransparentDropDownPushButton:disabled,\n"
                                   "TransprentTogglePushButton:disabled {\n"
                                   "    background-color: transparent;\n"
                                   "    border: none;\n"
                                   "}\n"
                                   "\n"
                                   "\n"
                                   "PillPushButton,\n"
                                   "PillPushButton:hover,\n"
                                   "PillPushButton:pressed,\n"
                                   "PillPushButton:disabled,\n"
                                   "PillPushButton:checked,\n"
                                   "PillPushButton:checked:hover,\n"
                                   "PillPushButton:checked:p"
                                   "ressed,\n"
                                   "PillPushButton:disabled:checked,\n"
                                   "PillToolButton,\n"
                                   "PillToolButton:hover,\n"
                                   "PillToolButton:pressed,\n"
                                   "PillToolButton:disabled,\n"
                                   "PillToolButton:checked,\n"
                                   "PillToolButton:checked:hover,\n"
                                   "PillToolButton:checked:pressed,\n"
                                   "PillToolButton:disabled:checked {\n"
                                   "    background-color: transparent;\n"
                                   "    border: none;\n"
                                   "}\n"
                                   "")
        self.AIStart.clicked.connect(self.AISStartGenerator)

        self.gridLayout_9.addWidget(self.AIStart, 25, 1, 1, 3)

        self.StrongBodyLabel_9 = StrongBodyLabel(
            self.scrollAreaWidgetContents_3)
        self.StrongBodyLabel_9.setObjectName(u"StrongBodyLabel_9")
        self.StrongBodyLabel_9.setFont(font4)
        self.StrongBodyLabel_9.setProperty("lightColor", QColor(0, 0, 0))

        self.gridLayout_9.addWidget(self.StrongBodyLabel_9, 6, 1, 1, 3)

        self.StrongBodyLabel_12 = StrongBodyLabel(
            self.scrollAreaWidgetContents_3)
        self.StrongBodyLabel_12.setObjectName(u"StrongBodyLabel_12")
        self.StrongBodyLabel_12.setFont(font4)

        self.gridLayout_9.addWidget(self.StrongBodyLabel_12, 17, 1, 1, 2)

        self.verticalSpacer_40 = QSpacerItem(
            20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_9.addItem(self.verticalSpacer_40, 18, 1, 1, 1)

        self.verticalSpacer_34 = QSpacerItem(
            20, 20, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.gridLayout_9.addItem(self.verticalSpacer_34, 2, 2, 1, 1)

        self.verticalSpacer_33 = QSpacerItem(
            20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_9.addItem(self.verticalSpacer_33, 16, 2, 1, 1)

        self.verticalSpacer_30 = QSpacerItem(
            20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_9.addItem(self.verticalSpacer_30, 9, 1, 1, 1)

        self.StrongBodyLabel_6 = StrongBodyLabel(
            self.scrollAreaWidgetContents_3)
        self.StrongBodyLabel_6.setObjectName(u"StrongBodyLabel_6")
        self.StrongBodyLabel_6.setFont(font4)

        self.gridLayout_9.addWidget(self.StrongBodyLabel_6, 20, 1, 1, 3)

        self.AIBadTags = PlainTextEdit(self.scrollAreaWidgetContents_3)
        self.AIBadTags.setObjectName(u"AIBadTags")
        self.AIBadTags.setMaximumSize(QSize(16777215, 100))
        self.AIBadTags.setStyleSheet(u"LineEdit, TextEdit, PlainTextEdit {\n"
                                     "    color: black;\n"
                                     "    background-color: rgba(255, 255, 255, 0.7);\n"
                                     "    border: 1px solid rgba(0, 0, 0, 13);\n"
                                     "    border-bottom: 1px solid rgba(0, 0, 0, 100);\n"
                                     "    border-radius: 5px;\n"
                                     "    /* font: 14px \"Segoe UI\", \"Microsoft YaHei\"; */\n"
                                     "    padding: 0px 10px;\n"
                                     "    selection-background-color: #8b2be7;\n"
                                     "}\n"
                                     "\n"
                                     "TextEdit,\n"
                                     "PlainTextEdit {\n"
                                     "    padding: 2px 3px 2px 8px;\n"
                                     "}\n"
                                     "\n"
                                     "LineEdit:hover, TextEdit:hover, PlainTextEdit:hover {\n"
                                     "    background-color: rgba(249, 249, 249, 0.5);\n"
                                     "    border: 1px solid rgba(0, 0, 0, 13);\n"
                                     "    border-bottom: 1px solid rgba(0, 0, 0, 100);\n"
                                     "}\n"
                                     "\n"
                                     "LineEdit:focus {\n"
                                     "    border-bottom: 1px solid rgba(0, 0, 0, 13);\n"
                                     "    background-color: white;\n"
                                     "}\n"
                                     "\n"
                                     "TextEdit:focus,\n"
                                     "PlainTextEdit:focus {\n"
                                     "    border-bottom: 1px solid #009faa;\n"
                                     "    background-color: white;\n"
                                     "}\n"
                                     "\n"
                                     "LineEdit:disabled, TextEdit:disabled,\n"
                                     "PlainTextEdit:disabled {\n"
                                     "    color: rgba(0, 0, 0,"
                                     " 150);\n"
                                     "    background-color: rgba(249, 249, 249, 0.3);\n"
                                     "    border: 1px solid rgba(0, 0, 0, 13);\n"
                                     "    border-bottom: 1px solid rgba(0, 0, 0, 13);\n"
                                     "}\n"
                                     "\n"
                                     "#lineEditButton {\n"
                                     "    background-color: transparent;\n"
                                     "    border-radius: 4px;\n"
                                     "    margin: 0;\n"
                                     "}\n"
                                     "\n"
                                     "#lineEditButton:hover {\n"
                                     "    background-color: rgba(0, 0, 0, 9);\n"
                                     "}\n"
                                     "\n"
                                     "#lineEditButton:pressed {\n"
                                     "    background-color: rgba(0, 0, 0, 6);\n"
                                     "}\n"
                                     "")

        self.gridLayout_9.addWidget(self.AIBadTags, 7, 1, 1, 3)

        self.verticalSpacer_37 = QSpacerItem(
            20, 0, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_9.addItem(self.verticalSpacer_37, 14, 1, 1, 1)

        self.StrongBodyLabel_8 = StrongBodyLabel(
            self.scrollAreaWidgetContents_3)
        self.StrongBodyLabel_8.setObjectName(u"StrongBodyLabel_8")
        self.StrongBodyLabel_8.setFont(font4)
        self.StrongBodyLabel_8.setProperty("lightColor", QColor(0, 0, 0))

        self.gridLayout_9.addWidget(self.StrongBodyLabel_8, 3, 1, 1, 3)

        self.AISize = ComboBox(self.scrollAreaWidgetContents_3)
        self.AISize.setObjectName(u"AISize")
        self.AISize.setStyleSheet(u"ComboBox {\n"
                                  "    border: 1px solid rgba(0, 0, 0, 0.073);\n"
                                  "    border-radius: 5px;\n"
                                  "    border-bottom: 1px solid rgba(0, 0, 0, 0.183);\n"
                                  "    padding: 5px 31px 6px 11px;\n"
                                  "    /* font: 14px 'Segoe UI', 'Microsoft YaHei', 'PingFang SC'; */\n"
                                  "    color: black;\n"
                                  "    background-color: rgba(255, 255, 255, 0.7);\n"
                                  "    text-align: left;\n"
                                  "    selection-background-color: #8b2be7\n"
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
        self.AISize.addItem("640")
        self.AISize.addItem("720")
        self.AISize.addItem("768")
        self.AISize.addItem("1024")

        self.gridLayout_9.addWidget(self.AISize, 12, 3, 1, 1)

        self.StrongBodyLabel_13 = StrongBodyLabel(
            self.scrollAreaWidgetContents_3)
        self.StrongBodyLabel_13.setObjectName(u"StrongBodyLabel_13")
        self.StrongBodyLabel_13.setFont(font4)

        self.gridLayout_9.addWidget(self.StrongBodyLabel_13, 21, 1, 1, 3)

        self.StrongBodyLabel_10 = StrongBodyLabel(
            self.scrollAreaWidgetContents_3)
        self.StrongBodyLabel_10.setObjectName(u"StrongBodyLabel_10")
        self.StrongBodyLabel_10.setFont(font4)

        self.gridLayout_9.addWidget(self.StrongBodyLabel_10, 12, 1, 1, 1)

        self.StrongBodyLabel_11 = StrongBodyLabel(
            self.scrollAreaWidgetContents_3)
        self.StrongBodyLabel_11.setObjectName(u"StrongBodyLabel_11")
        self.StrongBodyLabel_11.setFont(font4)

        self.gridLayout_9.addWidget(self.StrongBodyLabel_11, 15, 1, 1, 2)

        self.verticalSpacer_35 = QSpacerItem(
            10, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_9.addItem(self.verticalSpacer_35, 26, 1, 1, 1)

        self.StrongBodyLabel_15 = StrongBodyLabel(
            self.scrollAreaWidgetContents_3)
        self.StrongBodyLabel_15.setObjectName(u"StrongBodyLabel_15")
        self.StrongBodyLabel_15.setFont(font4)

        self.gridLayout_9.addWidget(self.StrongBodyLabel_15, 23, 1, 1, 3)

        self.AIFix = SpinBox(self.scrollAreaWidgetContents_3)
        self.AIFix.setObjectName(u"AIFix")
        self.AIFix.setStyleSheet(u"SpinBox, DoubleSpinBox, DateEdit, DateTimeEdit, TimeEdit,\n"
                                 "CompactSpinBox,\n"
                                 "CompactDoubleSpinBox,\n"
                                 "CompactDateEdit,\n"
                                 "CompactDateTimeEdit,\n"
                                 "CompactTimeEdit {\n"
                                 "    color: black;\n"
                                 "    background-color: rgba(255, 255, 255, 0.7);\n"
                                 "    border: 1px solid rgba(0, 0, 0, 13);\n"
                                 "    border-bottom: 1px solid rgba(0, 0, 0, 100);\n"
                                 "    border-radius: 5px;\n"
                                 "    /* font: 14px \"Segoe UI\", \"Microsoft YaHei\"; */\n"
                                 "    padding: 0px 80px 0 10px;\n"
                                 "    selection-background-color: #8b2be7;\n"
                                 "}\n"
                                 "\n"
                                 "CompactSpinBox,\n"
                                 "CompactDoubleSpinBox,\n"
                                 "CompactDateEdit,\n"
                                 "CompactDateTimeEdit,\n"
                                 "CompactTimeEdit {\n"
                                 "    padding: 0px 26px 0 10px;\n"
                                 "}\n"
                                 "\n"
                                 "SpinBox:hover,\n"
                                 "DoubleSpinBox:hover,\n"
                                 "DateEdit:hover,\n"
                                 "DateTimeEdit:hover,\n"
                                 "TimeEdit:hover,\n"
                                 "CompactSpinBox:hover,\n"
                                 "CompactDoubleSpinBox:hover,\n"
                                 "CompactDateEdit:hover,\n"
                                 "CompactDateTimeEdit:hover,\n"
                                 "CompactTimeEdit:hover {\n"
                                 "    background-color: rgba(249, 249, 249, 0.5);\n"
                                 "    border: 1px solid rgba(0, 0, 0, "
                                 "13);\n"
                                 "    border-bottom: 1px solid rgba(0, 0, 0, 100);\n"
                                 "}\n"
                                 "\n"
                                 "SpinBox:focus,\n"
                                 "DoubleSpinBox:focus,\n"
                                 "DateEdit:focus,\n"
                                 "DateTimeEdit:focus,\n"
                                 "TimeEdit:focus,\n"
                                 "CompactSpinBox:focus,\n"
                                 "CompactDoubleSpinBox:focus,\n"
                                 "CompactDateEdit:focus,\n"
                                 "CompactDateTimeEdit:focus,\n"
                                 "CompactTimeEdit:focus {\n"
                                 "    border-bottom: 1px solid rgba(0, 0, 0, 13);\n"
                                 "    background-color: white;\n"
                                 "}\n"
                                 "\n"
                                 "SpinBox:disabled,\n"
                                 "DoubleSpinBox:disabled,\n"
                                 "DateEdit:disabled,\n"
                                 "DateTimeEdit:disabled,\n"
                                 "TimeEdit:disabled,\n"
                                 "CompactSpinBox:disabled,\n"
                                 "CompactDoubleSpinBox:disabled,\n"
                                 "CompactDateEdit:disabled,\n"
                                 "CompactDateTimeEdit:disabled,\n"
                                 "CompactTimeEdit:disabled {\n"
                                 "    color: rgba(0, 0, 0, 150);\n"
                                 "    background-color: rgba(249, 249, 249, 0.5);\n"
                                 "    border: 1px solid rgba(0, 0, 0, 13);\n"
                                 "    border-bottom: 1px solid rgba(0, 0, 0, 13);\n"
                                 "}\n"
                                 "\n"
                                 "SpinButton {\n"
                                 "    background-color: transparent;\n"
                                 "    border-radius: 4px;\n"
                                 "    margin: 0;\n"
                                 "}\n"
                                 "\n"
                                 "SpinButton:ho"
                                 "ver {\n"
                                 "    background-color: rgba(0, 0, 0, 9);\n"
                                 "}\n"
                                 "\n"
                                 "SpinButton:pressed {\n"
                                 "    background-color: rgba(0, 0, 0, 6);\n"
                                 "}")
        self.AIFix.setMinimum(1)
        self.AIFix.setMaximum(10)

        self.gridLayout_9.addWidget(self.AIFix, 17, 3, 1, 1)

        self.StrongBodyLabel_14 = StrongBodyLabel(
            self.scrollAreaWidgetContents_3)
        self.StrongBodyLabel_14.setObjectName(u"StrongBodyLabel_14")
        self.StrongBodyLabel_14.setFont(font4)

        self.gridLayout_9.addWidget(self.StrongBodyLabel_14, 22, 1, 1, 3)

        self.verticalSpacer_31 = QSpacerItem(
            20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_9.addItem(self.verticalSpacer_31, 11, 1, 1, 1)

        self.AIGoodTags = PlainTextEdit(self.scrollAreaWidgetContents_3)
        self.AIGoodTags.setObjectName(u"AIGoodTags")
        self.AIGoodTags.setMaximumSize(QSize(16777215, 150))
        self.AIGoodTags.setStyleSheet(u"LineEdit, TextEdit, PlainTextEdit {\n"
                                      "    color: black;\n"
                                      "    background-color: rgba(255, 255, 255, 0.7);\n"
                                      "    border: 1px solid rgba(0, 0, 0, 13);\n"
                                      "    border-bottom: 1px solid rgba(0, 0, 0, 100);\n"
                                      "    border-radius: 5px;\n"
                                      "    /* font: 14px \"Segoe UI\", \"Microsoft YaHei\"; */\n"
                                      "    padding: 0px 10px;\n"
                                      "    selection-background-color: #8b2be7;\n"
                                      "}\n"
                                      "\n"
                                      "TextEdit,\n"
                                      "PlainTextEdit {\n"
                                      "    padding: 2px 3px 2px 8px;\n"
                                      "}\n"
                                      "\n"
                                      "LineEdit:hover, TextEdit:hover, PlainTextEdit:hover {\n"
                                      "    background-color: rgba(249, 249, 249, 0.5);\n"
                                      "    border: 1px solid rgba(0, 0, 0, 13);\n"
                                      "    border-bottom: 1px solid rgba(0, 0, 0, 100);\n"
                                      "}\n"
                                      "\n"
                                      "LineEdit:focus {\n"
                                      "    border-bottom: 1px solid rgba(0, 0, 0, 13);\n"
                                      "    background-color: white;\n"
                                      "}\n"
                                      "\n"
                                      "TextEdit:focus,\n"
                                      "PlainTextEdit:focus {\n"
                                      "    border-bottom: 1px solid #009faa;\n"
                                      "    background-color: white;\n"
                                      "}\n"
                                      "\n"
                                      "LineEdit:disabled, TextEdit:disabled,\n"
                                      "PlainTextEdit:disabled {\n"
                                      "    color: rgba(0, 0, 0,"
                                      " 150);\n"
                                      "    background-color: rgba(249, 249, 249, 0.3);\n"
                                      "    border: 1px solid rgba(0, 0, 0, 13);\n"
                                      "    border-bottom: 1px solid rgba(0, 0, 0, 13);\n"
                                      "}\n"
                                      "\n"
                                      "#lineEditButton {\n"
                                      "    background-color: transparent;\n"
                                      "    border-radius: 4px;\n"
                                      "    margin: 0;\n"
                                      "}\n"
                                      "\n"
                                      "#lineEditButton:hover {\n"
                                      "    background-color: rgba(0, 0, 0, 9);\n"
                                      "}\n"
                                      "\n"
                                      "#lineEditButton:pressed {\n"
                                      "    background-color: rgba(0, 0, 0, 6);\n"
                                      "}\n"
                                      "")

        self.gridLayout_9.addWidget(self.AIGoodTags, 4, 1, 1, 3)

        self.StrongBodyLabel_16 = StrongBodyLabel(
            self.scrollAreaWidgetContents_3)
        self.StrongBodyLabel_16.setObjectName(u"StrongBodyLabel_16")
        self.StrongBodyLabel_16.setFont(font4)

        self.gridLayout_9.addWidget(self.StrongBodyLabel_16, 19, 1, 1, 3)

        self.SmoothScrollArea_3.setWidget(self.scrollAreaWidgetContents_3)

        self.gridLayout_10.addWidget(self.SmoothScrollArea_3, 0, 0, 1, 1)

        # self.OpacityAniStackedWidget_2.addWidget(self.page_6)
        self.addPageInterface(self.page_6, "page_6", FluentIcon.TRANSPARENT)

        self.page_7 = QWidget()
        self.page_7.setObjectName(u"page_7")
        self.gridLayout_12 = QGridLayout(self.page_7)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.SmoothScrollArea_4 = SmoothScrollArea(self.page_7)
        self.SmoothScrollArea_4.setObjectName(u"SmoothScrollArea_4")
        self.SmoothScrollArea_4.setStyleSheet(u"background: transparent;\n"
                                              "border: none;")
        self.SmoothScrollArea_4.setWidgetResizable(True)
        self.SmoothScrollArea_4.setAlignment(Qt.AlignCenter)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(
            u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 273, 153))
        self.gridLayout_11 = QGridLayout(self.scrollAreaWidgetContents_4)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.AIProgress = IndeterminateProgressBar(
            self.scrollAreaWidgetContents_4)
        self.AIProgress.setObjectName(u"AIProgress")
        self.AIProgress.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(170, 58, 217, 255), stop:1 rgba(106, 55, 233, 255));\n"
                                      "border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(170, 58, 217, 255), stop:1 rgba(106, 55, 233, 255));\n"
                                      "color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(170, 58, 217, 255), stop:1 rgba(106, 55, 233, 255));\n"
                                      "gridline-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(170, 58, 217, 255), stop:1 rgba(106, 55, 233, 255));")
        light = QColor(139, 43, 231)
        self.AIProgress.setCustomBarColor(light, light)
        self.AIProgress.setVisible(False)

        self.gridLayout_11.addWidget(self.AIProgress, 4, 1, 1, 2)

        self.AIList = TableWidget(self.scrollAreaWidgetContents_4)
        self.AIList.setObjectName(u"AIList")
        self.AIList.setBorderVisible(True)
        self.AIList.setBorderRadius(8)

        self.AIList.setWordWrap(False)
        self.AIList.setRowCount(3)
        self.AIList.setColumnCount(2)

        self.AIList.verticalHeader().hide()
        self.AIList.setHorizontalHeaderLabels(['标签', '进度'])
        # self.AIList.resizeColumnsToContents()

        self.gridLayout_11.addWidget(self.AIList, 6, 1, 1, 1)

        self.SubtitleLabel_6 = SubtitleLabel(self.scrollAreaWidgetContents_4)
        self.SubtitleLabel_6.setObjectName(u"SubtitleLabel_6")
        self.SubtitleLabel_6.setFont(font6)
        self.SubtitleLabel_6.setAlignment(Qt.AlignCenter)
        self.SubtitleLabel_6.setProperty("lightColor", QColor(139, 43, 231))

        self.gridLayout_11.addWidget(self.SubtitleLabel_6, 1, 1, 1, 2)

        self.verticalSpacer_49 = QSpacerItem(
            20, 0, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_11.addItem(self.verticalSpacer_49, 3, 1, 1, 1)

        self.verticalSpacer_41 = QSpacerItem(
            20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_11.addItem(self.verticalSpacer_41, 5, 1, 1, 1)

        self.SmoothScrollArea_4.setWidget(self.scrollAreaWidgetContents_4)

        self.gridLayout_12.addWidget(self.SmoothScrollArea_4, 0, 0, 1, 1)

        # self.OpacityAniStackedWidget_2.addWidget(self.page_7)
        self.addPageInterface(self.page_7, "page_7", FluentIcon.SYNC)

        self.verticalLayout_9.addWidget(self.OpacityAniStackedWidget_2)

        self.BodyLabel_2 = BodyLabel(self.SimpleCardWidget_4)
        self.BodyLabel_2.setObjectName(u"BodyLabel_2")

        self.verticalLayout_9.addWidget(self.BodyLabel_2)

        self.BodyLabel = BodyLabel(self.SimpleCardWidget_4)
        self.BodyLabel.setObjectName(u"BodyLabel")

        self.verticalLayout_9.addWidget(self.BodyLabel)

        self.horizontalLayout_7.addWidget(self.SimpleCardWidget_4)

        self.widget_4 = QWidget(self.page_5)
        self.widget_4.setObjectName(u"widget_4")
        sizePolicy.setHeightForWidth(
            self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy)
        self.widget_4.setMinimumSize(QSize(361, 0))
        self.widget_4.setLayoutDirection(Qt.LeftToRight)
        self.widget_4.setAutoFillBackground(False)
        self.verticalLayout_8 = QVBoxLayout(self.widget_4)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_8.setContentsMargins(-1, 1, -1, -1)
        self.ElevatedCardWidget_3 = ElevatedCardWidget(self.widget_4)
        self.ElevatedCardWidget_3.setObjectName(u"ElevatedCardWidget_3")
        self.ElevatedCardWidget_3.setMinimumSize(QSize(361, 450))
        self.ElevatedCardWidget_3.setMaximumSize(QSize(16777215, 16777215))
        self.ElevatedCardWidget_3.setAutoFillBackground(False)
        self.gridLayout_8 = QGridLayout(self.ElevatedCardWidget_3)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.AIImages = HorizontalFlipView(self.ElevatedCardWidget_3)
        self.AIImages.setObjectName(u"AIImages")
        self.AIImages.setAspectRatioMode(Qt.AspectRatioMode.KeepAspectRatio)
        self.AIImages.setItemAlignment(
            Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignVCenter)
        self.AIImages.setObjectName(u"AIImages")
        self.AIImages.clicked.connect(
            lambda: self.ShowSetBackgroundAI(self.AIImages))
        # self.AIImages.setMinimumSize(QSize(480, 270))
        # self.AIImages.setSizeIncrement(QSize(0, -1))

        self.gridLayout_8.addWidget(self.AIImages, 0, 0, 1, 1)

        self.verticalLayout_8.addWidget(self.ElevatedCardWidget_3)

        self.widget_5 = QWidget(self.widget_4)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setMaximumSize(QSize(16777215, 51))
        self.horizontalLayout_6 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_13 = QSpacerItem(
            163, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_13)

        self.horizontalSpacer_14 = QSpacerItem(
            27, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_14)

        self.AIShow = HorizontalPipsPager(self.widget_5)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        QListWidgetItem(self.AIShow)
        self.AIShow.setObjectName(u"AIShow")

        self.horizontalLayout_6.addWidget(self.AIShow)

        self.horizontalSpacer_15 = QSpacerItem(
            162, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_15)

        self.AIShowNumber = SpinBox(self.widget_5)
        self.AIShowNumber.setObjectName(u"AIShowNumber")
        self.AIShowNumber.setMaximumSize(QSize(150, 33))
        self.AIShowNumber.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.AIShowNumber.setMinimum(0)
        self.AIShowNumber.setMaximum(0)
        self.AIShowNumber.valueChanged.connect(self.AI_Ssp_ValueChanged)

        self.horizontalLayout_6.addWidget(self.AIShowNumber)

        self.verticalLayout_8.addWidget(self.widget_5)

        # self.AICommandBar = CommandBar(self.widget_4)
        # self.AICommandBar.setObjectName(u"AICommandBar")
        # self.AICommandBar.setMinimumSize(QSize(1, 34))
        # self.AICommandBar.setLayoutDirection(Qt.LeftToRight)
        # self.AICommandBar.setAutoFillBackground(False)
        # self.AICommandBar.setFrameShape(QFrame.NoFrame)
        # self.AICommandBar.setFrameShadow(QFrame.Plain)

        # self.verticalLayout_8.addWidget(self.AICommandBar)

        self.horizontalLayout_7.addWidget(self.widget_4)

        # self.OpacityAniStackedWidget.addWidget(self.page_5)
        self.addSubInterface(self.page_5, "page_5", "AI画图")

        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.gridLayout_7 = QGridLayout(self.page_4)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.SimpleCardWidget_3 = SimpleCardWidget(self.page_4)
        self.SimpleCardWidget_3.setObjectName(u"SimpleCardWidget_3")
        self.gridLayout_6 = QGridLayout(self.SimpleCardWidget_3)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.verticalSpacer_23 = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer_23, 14, 2, 1, 1)

        self.verticalSpacer_24 = QSpacerItem(
            20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_6.addItem(self.verticalSpacer_24, 7, 1, 1, 1)

        self.UserAgency = RadioButton(self.SimpleCardWidget_3)
        self.UserAgency.setObjectName(u"UserAgency")

        self.gridLayout_6.addWidget(self.UserAgency, 13, 1, 1, 1)

        self.InsiderAgency = RadioButton(self.SimpleCardWidget_3)
        self.InsiderAgency.setObjectName(u"InsiderAgency")
        self.InsiderAgency.setChecked(True)

        self.gridLayout_6.addWidget(self.InsiderAgency, 9, 1, 1, 1)

        self.horizontalSpacer_11 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_11, 4, 4, 1, 1)

        self.SavePath = LineEdit(self.SimpleCardWidget_3)
        self.SavePath.setObjectName(u"SavePath")

        self.gridLayout_6.addWidget(self.SavePath, 5, 1, 1, 5)

        self.SubtitleLabel_4 = SubtitleLabel(self.SimpleCardWidget_3)
        self.SubtitleLabel_4.setObjectName(u"SubtitleLabel_4")

        self.gridLayout_6.addWidget(self.SubtitleLabel_4, 8, 1, 1, 1)

        self.SubtitleLabel_3 = SubtitleLabel(self.SimpleCardWidget_3)
        self.SubtitleLabel_3.setObjectName(u"SubtitleLabel_3")

        self.gridLayout_6.addWidget(self.SubtitleLabel_3, 4, 1, 1, 1)

        self.NoAgency = RadioButton(self.SimpleCardWidget_3)
        self.NoAgency.setObjectName(u"NoAgency")

        self.gridLayout_6.addWidget(self.NoAgency, 12, 1, 1, 1)

        self.LargeTitleLabel = LargeTitleLabel(self.SimpleCardWidget_3)
        self.LargeTitleLabel.setObjectName(u"LargeTitleLabel")
        font8 = QFont()
        font8.setFamilies([u"HarmonyOS Sans SC"])
        font8.setPointSize(32)
        font8.setBold(False)
        self.LargeTitleLabel.setFont(font8)

        self.gridLayout_6.addWidget(self.LargeTitleLabel, 3, 1, 1, 1)

        self.verticalSpacer_27 = QSpacerItem(
            20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_6.addItem(self.verticalSpacer_27, 1, 1, 1, 1)

        self.verticalSpacer_25 = QSpacerItem(
            20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_6.addItem(self.verticalSpacer_25, 17, 6, 1, 1)

        self.horizontalSpacer_12 = QSpacerItem(
            15, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_12, 8, 0, 1, 1)

        self.SaveSettings = PrimaryPushButton(self.SimpleCardWidget_3)
        self.SaveSettings.setObjectName(u"SaveSettings")
        self.SaveSettings.setMinimumSize(QSize(100, 0))
        self.SaveSettings.clicked.connect(self.WriteSettings)

        self.gridLayout_6.addWidget(self.SaveSettings, 16, 6, 1, 1)

        self.verticalSpacer_26 = QSpacerItem(
            10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.verticalSpacer_26, 16, 7, 1, 1)

        self.ChosePath = PushButton(self.SimpleCardWidget_3)
        self.ChosePath.setObjectName(u"ChosePath")
        self.ChosePath.setMinimumSize(QSize(100, 0))
        self.ChosePath.clicked.connect(self.ChoosePaths)

        self.gridLayout_6.addWidget(self.ChosePath, 5, 6, 1, 1)

        self.UserInputAgency = LineEdit(self.SimpleCardWidget_3)
        self.UserInputAgency.setObjectName(u"UserInputAgency")

        self.gridLayout_6.addWidget(self.UserInputAgency, 13, 2, 1, 5)

        self.AboutButton = PushButton(self.SimpleCardWidget_3)
        self.AboutButton.setObjectName(u"AboutButton")
        self.AboutButton.setMinimumSize(QSize(140, 0))
        self.AboutButton.clicked.connect(self.showAbout)

        self.gridLayout_6.addWidget(self.AboutButton, 16, 1, 1, 1)

        # self.verticalSpacer_28 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        # self.gridLayout_6.addItem(self.verticalSpacer_28, 18, 5, 1, 1)

        self.gridLayout_7.addWidget(self.SimpleCardWidget_3, 0, 0, 1, 1)

        # self.OpacityAniStackedWidget.addWidget(self.page_4)

        self.addSubInterface(self.page_4, "page_4", "设置")

        self.verticalLayout.addWidget(self.OpacityAniStackedWidget)

        self.retranslateUi(self.MainUI)
        self.ReadSettings()

        self.OpacityAniStackedWidget.setCurrentIndex(0)
        self.TopMenu.setCurrentItem(self.page.objectName())

        self.TopMenu.currentItemChanged.connect(
            lambda k:  self.OpacityAniStackedWidget.setCurrentWidget(self.OpacityAniStackedWidget.findChild(QWidget, k)))

        # print(len(self.OpacityAniStackedWidget))

        self.ACGKind.setDefault(True)
        self.OpacityAniStackedWidget_2.setCurrentIndex(0)
        self.AIPages.setCurrentItem(self.page_6.objectName())
        self.AIPages.currentItemChanged.connect(
            lambda k:  self.OpacityAniStackedWidget_2.setCurrentWidget(self.OpacityAniStackedWidget_2.findChild(QWidget, k)))

        self.ACGShow.currentIndexChanged.connect(self.ACG_S_IndexChanged)
        self.ACGImages.currentIndexChanged.connect(self.ACG_I_IndexChanged)

        self.PixivShow.currentIndexChanged.connect(self.Pixiv_S_IndexChanged)
        self.PixivImages.currentIndexChanged.connect(self.Pixiv_I_IndexChanged)

        self.AIShow.currentIndexChanged.connect(self.AI_S_IndexChanged)
        self.AIImages.currentIndexChanged.connect(self.AI_I_IndexChanged)

        self.update_background()

        QMetaObject.connectSlotsByName(self.MainUI)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.DisplayLabel.setText(QCoreApplication.translate(
            "Form", u"<html><head/><body><p><span style=\" font-size:18pt;\">\u58c1\u7eb8\u751f\u6210\u5668 \u53ef\u4ee5\u5feb\u901f\u5730\u5e2e\u4f60\u751f\u6210\u4e00\u5f20\u7cbe\u7f8e\u4e8c\u6b21\u5143\u58c1\u7eb8\u3002</span></p></body></html>", None))
        self.TitleLabel.setText(QCoreApplication.translate(
            "Form", u"<html><head/><body><p><span style=\" font-size:51pt;\">\u6b22\u8fce Welcome</span></p></body></html>", None))
        self.ToACG.setText(QCoreApplication.translate(
            "Form", u"自动化更换 ACG 壁纸", None))
        # self.ToPixiv.setText(QCoreApplication.translate(
        #     "Form", u"\u4ece Pixiv \u751f\u6210", None))
        self.ToAI.setText(QCoreApplication.translate(
            "Form", u"制作渐变色壁纸", None))
        # self.ACGKind.setText(QCoreApplication.translate("Form", u"1", None))
        self.ACGContentKind.setText(QCoreApplication.translate(
            "Form", u"\u6309\u5185\u5bb9\u7c7b\u578b", None))
        self.ACGDevicesKind.setText(QCoreApplication.translate(
            "Form", u"\u6309\u5c3a\u5bf8\u7c7b\u578b", None))
        self.ACGStart.setText(QCoreApplication.translate(
            "Form", u"\u751f\u6210", None))
        self.SubtitleLabel.setText(QCoreApplication.translate(
            "Form", u"ACG 壁纸\u751f\u6210\u5668", None))
        self.StrongBodyLabel_2.setText(QCoreApplication.translate(
            "Form", u"\u751f\u6210\u6570\u91cf (1~100)\uff1a", None))
        self.StrongBodyLabel.setText(QCoreApplication.translate(
            "Form", u"\u7b5b\u9009\u7c7b\u578b\uff1a", None))

        __sortingEnabled = self.ACGShow.isSortingEnabled()
        self.ACGShow.setSortingEnabled(False)
        ___qlistwidgetitem = self.ACGShow.item(160)
        ___qlistwidgetitem.setText(
            QCoreApplication.translate("Form", u"6", None))
        self.ACGShow.setSortingEnabled(__sortingEnabled)

        self.StrongBodyLabel_4.setText(QCoreApplication.translate(
            "Form", u"\u4f5c\u8005 UID (\u53ef\u9009)\uff1a", None))
        self.PixivTags.setText(QCoreApplication.translate(
            "Form", u"\u841d\u8389&\u767d\u4e1d", None))
        self.PixivIsR18.setText(QCoreApplication.translate(
            "Form", u"\u5305\u542b R18", None))
        self.StrongBodyLabel_3.setText(QCoreApplication.translate(
            "Form", u"\u751f\u6210\u6570\u91cf (1~15)\uff1a", None))
        self.StrongBodyLabel_5.setText(QCoreApplication.translate(
            "Form", u"\u6807\u7b7e Tags (\u53ef\u9009\uff0c\u4f7f\u7528 & \u5206\u5272)\uff1a", None))
        self.PixivStart.setText(QCoreApplication.translate(
            "Form", u"\u751f\u6210", None))
        self.SubtitleLabel_2.setText(QCoreApplication.translate(
            "Form", u"<html><head/><body><p><span style=\" color:#0096fa;\">Pixiv \u751f\u6210\u5668</span></p></body></html>", None))
        self.PixivIsAI.setText(QCoreApplication.translate(
            "Form", u"\u53bb\u9664 AI", None))
        self.PixivUID.setText(
            QCoreApplication.translate("Form", u"", None))
        self.HyperlinkLabel.setText(QCoreApplication.translate(
            "Form", u"\u4f7f\u7528\u5373\u4ee3\u8868\u60a8\u540c\u610f\u300a\u514d\u8d23\u58f0\u660e\u300b", None))

        __sortingEnabled1 = self.PixivShow.isSortingEnabled()
        self.PixivShow.setSortingEnabled(False)
        ___qlistwidgetitem1 = self.PixivShow.item(165)
        ___qlistwidgetitem1.setText(
            QCoreApplication.translate("Form", u"6", None))
        self.PixivShow.setSortingEnabled(__sortingEnabled1)

        self.SubtitleLabel_5.setText(QCoreApplication.translate(
            "Form", u"SRIntelligence AI\u753b\u56fe", None))
        self.StrongBodyLabel_7.setText(
            QCoreApplication.translate("Form", u"超分倍数 (1~2)\uff1a", None))
        self.AIStart.setText(QCoreApplication.translate(
            "Form", u"\u8fdb\u5165\u751f\u6210\u5217\u961f", None))
        self.StrongBodyLabel_9.setText(QCoreApplication.translate(
            "Form", u"\u53cd\u5411\u6807\u7b7e\uff08\u6392\u9664\u3001\u7ea0\u9519\uff09\uff1a", None))
        self.StrongBodyLabel_12.setText(QCoreApplication.translate(
            "Form", u"\u9ad8\u6e05\u4fee\u590d (1~10)\uff1a", None))
        self.StrongBodyLabel_6.setText(QCoreApplication.translate(
            "Form", u"\u91cd\u7ed8\u5e45\u5ea6\uff1a                      0.5", None))
        self.AIBadTags.setPlainText(QCoreApplication.translate(
            "Form", u"EasyNegative, nsfw, lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, username, blurry", None))
        self.StrongBodyLabel_8.setText(QCoreApplication.translate(
            "Form", u"\u6807\u7b7e \u6216 \u63cf\u8ff0\u4f60\u60f3\u8981\u751f\u6210\u7684\u5185\u5bb9\uff1a", None))
        self.AISize.setText(QCoreApplication.translate("Form", u"640", None))
        self.StrongBodyLabel_13.setText(QCoreApplication.translate(
            "Form", u"\u8d85\u5206\u7b97\u6cd5\uff1a                      Lanczos", None))
        self.StrongBodyLabel_10.setText(QCoreApplication.translate(
            "Form", u"\u6700\u4f4e\u5206\u8fa8\u7387\uff1a", None))
        self.StrongBodyLabel_11.setText(QCoreApplication.translate(
            "Form", u"\u6807\u7b7e\u5951\u5408\u5ea6 (1~10)\uff1a", None))
        self.StrongBodyLabel_15.setText(QCoreApplication.translate(
            "Form", u"\u91c7\u6837\u65b9\u6cd5\uff1a                      Euler a", None))
        self.StrongBodyLabel_14.setText(QCoreApplication.translate(
            "Form", u"迭代步数\uff1a                      20", None))
        self.StrongBodyLabel_16.setText(QCoreApplication.translate(
            "Form", u"\u5176\u4ed6\u5e38\u91cf\uff1a", None))
        self.SubtitleLabel_6.setText(QCoreApplication.translate(
            "Form", u"<html><head/><body><p><span style=\" color:#8b2be7;\">\u751f\u6210\u961f\u5217 \u2014 \u6b63\u5728\u8fdb\u884c</span></p></body></html>", None))
        self.BodyLabel_2.setText(QCoreApplication.translate(
            "Form", u"<html><head/><body><p><span style=\" font-size:10pt;\">\u57fa\u4e8e </span><span style=\" font-size:10pt; font-weight:700;\">Stable Diffusion</span><span style=\" font-size:10pt;\"> v1 \u6784\u5efa</span></p></body></html>", None))
        self.BodyLabel.setText(QCoreApplication.translate(
            "Form", u"<html><head/><body><p><span style=\" font-size:10pt;\">\u7531 </span><span style=\" font-size:10pt; font-weight:700; text-decoration: underline;\">SRIntelligence Service\u670d\u52a1\u5668\u96c6\u7fa4</span><span style=\" font-size:10pt;\"> \u63d0\u4f9b\u4e91\u7aef\u5904\u7406\u652f\u6301</span></p></body></html>", None))

        __sortingEnabled2 = self.AIShow.isSortingEnabled()
        self.AIShow.setSortingEnabled(False)
        ___qlistwidgetitem2 = self.AIShow.item(170)
        ___qlistwidgetitem2.setText(
            QCoreApplication.translate("Form", u"6", None))
        self.AIShow.setSortingEnabled(__sortingEnabled2)

        self.UserAgency.setText(QCoreApplication.translate(
            "Form", u"\u81ea\u5b9a\u4e49\u4ee3\u7406\uff1a", None))
        self.InsiderAgency.setText(QCoreApplication.translate(
            "Form", u"\u5185\u7f6e\u4ee3\u7406", None))
        self.SubtitleLabel_4.setText(QCoreApplication.translate(
            "Form", u"Pixiv \u4ee3\u7406\u8bbe\u7f6e\uff1a", None))
        self.SubtitleLabel_3.setText(QCoreApplication.translate(
            "Form", u"\u56fe\u7247\u4fdd\u5b58\u8def\u5f84\uff1a", None))
        self.NoAgency.setText(QCoreApplication.translate(
            "Form", u"\u65e0\u4ee3\u7406/\u7cfb\u7edf\u4ee3\u7406", None))
        self.LargeTitleLabel.setText(
            QCoreApplication.translate("Form", u"\u8bbe\u7f6e", None))
        self.SaveSettings.setText(
            QCoreApplication.translate("Form", u"\u5e94\u7528", None))
        self.ChosePath.setText(QCoreApplication.translate(
            "Form", u"\u9009\u53d6 ", None))
        self.UserInputAgency.setText(QCoreApplication.translate(
            "Form", u"不包含 http:// 或 https:// 的链接（例如 i.pixiv.re ）", None))

        self.AboutButton.setText(QCoreApplication.translate(
            "Form", u"\u5173\u4e8e \u58c1\u7eb8\u751f\u6210\u5668", None))

        self.ACGShow.setPageNumber(self.ACGImages.count())
        self.PixivShow.setPageNumber(self.PixivImages.count())
        self.AIShow.setPageNumber(self.AIImages.count())

    def addSubInterface(self, widget: QWidget, objectName, text):
        widget.setObjectName(objectName)
        # widget.setAlignment(Qt.AlignCenter)
        self.OpacityAniStackedWidget.addWidget(widget)
        self.TopMenu.addItem(routeKey=objectName, text=text)

    def addPageInterface(self, widget: QWidget, objectName, text):
        widget.setObjectName(objectName)
        # widget.setAlignment(Qt.AlignCenter)
        self.OpacityAniStackedWidget_2.addWidget(widget)
        self.AIPages.addItem(routeKey=objectName, icon=text)

    def clean_filename(self, filename):
        # 定义要替换的特殊字符列表
        special_chars = r'[\\/:*?"<>|]'
        # 使用正则表达式替换特殊字符为空
        cleaned_filename = re.sub(special_chars, '', filename)
        return cleaned_filename

    def showAbout(self):
        BatchWindow = QDialog()
        ui1 = V4About.Ui_Dialog()
        ui1.setupUi(BatchWindow)
        BatchWindow.exec_()

        # showani = random.randint(0,4)
        # print(showani)
        # match showani:
        #     case 0:
        #         Flyout.make(self.ACGCommandBar, target, self, FlyoutAnimationType.DROP_DOWN)
        #     case 1:
        #         Flyout.make(self.ACGCommandBar, target, self, FlyoutAnimationType.FADE_IN)
        #     case 2:
        #         Flyout.make(self.ACGCommandBar, target, self, FlyoutAnimationType.PULL_UP)
        #     case 3:
        #         Flyout.make(self.ACGCommandBar, target, self, FlyoutAnimationType.SLIDE_LEFT)
        #     case 4:
        #         Flyout.make(self.ACGCommandBar, target, self, FlyoutAnimationType.SLIDE_RIGHT)

    # retranslateUi

# ———————————————————————————————————————
# ————————————Settings———————————————————
# ———————————————————————————————————————

    def ReadSettings(self):

        if os.path.exists(os.path.abspath('./generated_pixmap')) == False:
            os.makedirs(os.path.abspath('./generated_pixmap'))

        norma_settings = f"{os.path.abspath('./generated_pixmap')}\nInsider"
        try:
            with open("generate_settings.Sr", "r") as s:
                sc = s.read()
                s.close()
            self.settings = sc.split("\n")
            if len(self.settings) != 2:
                msg_box = QMessageBox()
                msg_box.setWindowTitle("设置文件损坏")
                msg_box.setText("保存的设置疑似损坏或丢失，导致无法正常读取。我们将重置以下设置：\n    保存路径：" +
                                " ./generated_pixmap" + "\n    Pixiv 代理设置：内置代理")
                msg_box.setIcon(QMessageBox.Icon.Warning)
                msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
                msg_box.show()
                msg_box.exec()
                with open("generate_settings.Sr", "w") as a:
                    a.write(norma_settings)
                    a.close()
                self.ReadSettings()
            elif os.path.exists(self.settings[0]) == False:
                msg_box = QMessageBox()
                msg_box.setWindowTitle("找不到生成的图片")
                msg_box.setText(
                    "图片的生成路径已丢失或损坏。我们将重置以下设置：\n    保存路径：" + " ./generated_pixmap")
                msg_box.setIcon(QMessageBox.Icon.Warning)
                msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
                msg_box.show()
                msg_box.exec()

                new_settings = f"{os.path.abspath('./generated_pixmap')}\n{self.settings[1]}"
                with open("generate_settings.Sr", "w") as a:
                    a.write(new_settings)
                    a.close()
                self.ReadSettings()
            else:
                self.SavePath.setText(self.settings[0])
                match self.settings[1]:
                    case "Insider":
                        self.InsiderAgency.setChecked(True)
                    case "None":
                        self.NoAgency.setChecked(True)
                    case _:
                        self.UserAgency.setChecked(True)
                        self.UserInputAgency.setText(self.settings[1])

        except:
            msg_box = QMessageBox()
            msg_box.setWindowTitle("设置文件损坏")
            msg_box.setText("保存的设置疑似损坏或丢失，导致无法正常读取。我们将重置以下设置：\n    保存路径：" +
                            " ./generated_pixmap" + "\n    Pixiv 代理设置：内置代理")
            msg_box.setIcon(QMessageBox.Icon.Warning)
            msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg_box.show()
            msg_box.exec()
            with open("generate_settings.Sr", "w") as a:
                a.write(norma_settings)
                a.close()
            self.ReadSettings()

    def WriteSettings(self):
        if self.InsiderAgency.isChecked():
            settings = f"{self.SavePath.text()}\nInsider"
        elif self.NoAgency.isChecked():
            settings = f"{self.SavePath.text()}\nNone"
        else:
            settings = f"{self.SavePath.text()}\n{self.UserInputAgency.text()}"

        with open("generate_settings.Sr", "w") as a:
            a.write(settings)
            a.close()
        self.ReadSettings()

        Flyout.create(
            icon=InfoBarIcon.SUCCESS,
            title='配置已保存',
            content=f"更改将立即生效(/≧▽≦)/",
            target=self.SaveSettings,
            parent=self,
            isClosable=True,

        )

    def ChoosePaths(self):
        new_path = QFileDialog.getExistingDirectory(
            self, '生成的图片将会保存在：', self.settings[0])
        if new_path:
            self.SavePath.setText(new_path)

    def is_process_running(self, process_name):
        for proc in psutil.process_iter(['name']):
            if proc.info['name'] == process_name:
                return True
        return False
    
    def is_connected(self) -> bool:
        try:
            subprocess.check_call(
                ['ping', 'cn.bing.com', '-n', '1'],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                creationflags=subprocess.CREATE_NO_WINDOW
            )
            return True
        except subprocess.CalledProcessError:
            return False


# ———————————————————————————————————————
# ————————————Interaction-ACG————————————
# ———————————————————————————————————————

    def download_image(self, url, save, i):
        print('Thread {} started'.format(i))
        image = requests.get(url)
        with open(save, 'wb') as f:
            f.write(image.content)  # 保存图片
        print(save + " 结束")
        self.completed_threads += 1
        self.GeneratedACG.append(save)

    def ShowSetBackgroundTools(self, target: HorizontalFlipView):
        self.ACGCommandBar = CommandBarView(self)
        # self.ACGCommandBar.setObjectName(u"ACGCommandBar")
        # self.ACGCommandBar.setMinimumSize(QSize(1, 34))
        # self.ACGCommandBar.setLayoutDirection(Qt.LeftToRight)
        # self.ACGCommandBar.setAutoFillBackground(False)
        # self.ACGCommandBar.setFrameShape(QFrame.NoFrame)
        # self.ACGCommandBar.setFrameShadow(QFrame.Plain)
        self.ACGCommandBar.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        # self.ACGCommandBar.addAction(Action(FluentIcon.IMAGE_EXPORT, "设为壁纸", self))
        action = Action(FluentIcon.PHOTO, os.path.basename(
            self.GeneratedACG[self.ACGImages.currentIndex()]), self)
        action.triggered.connect(lambda: os.startfile(
            self.GeneratedACG[self.ACGImages.currentIndex()]))
        self.ACGCommandBar.addAction(action=action)
        action = Action(FluentIcon.IMAGE_EXPORT, "设为壁纸", self)
        action.triggered.connect(self.ACGSetBackground)
        self.ACGCommandBar.addAction(action=action)
        action = Action(FluentIcon.FOLDER, "在资源管理器中打开", self)
        # os.system(f'explorer /select, {os.path.realpath(self.GeneratedACG[self.ACGImages.currentIndex()])}')
        action.triggered.connect(lambda: os.startfile(
            os.path.dirname(self.GeneratedACG[self.ACGImages.currentIndex()])))
        self.ACGCommandBar.addAction(action=action)
        self.ACGCommandBar.resizeToSuitableWidth()
        Flyout.make(self.ACGCommandBar, target, self,
                    FlyoutAnimationType.DROP_DOWN)

    def ACGSetBackground(self):
        new_wall: str = '"{}"'.format(self.GeneratedACG[self.ACGImages.currentIndex()])
        # ctypes.windll.user32.SystemParametersInfoW(20, 0, new_wall, 3)
        # os.startfile("Set_Wallpaper.exe", arguments=new_wall)
        process = subprocess.Popen(f"Set_Wallpaper.exe {new_wall}")
        process.wait()

        Flyout.create(
            icon=InfoBarIcon.SUCCESS,
            title=f'壁纸已设置o(*≧▽≦)ツ',
            content=os.path.basename(new_wall),
            target=self.ACGImages,
            parent=self,
            isClosable=True,

        )

        print("ACGSetBackground: " + new_wall)

    def ToACGClicked(self):
        # self.OpacityAniStackedWidget.setCurrentIndex(1)
        # self.TopMenu.setCurrentItem(self.page_2.objectName())
        print("ToACGClicked")
        try:
            if not self.is_process_running("AutoWpChange_V4.exe"):
                os.startfile("AutoWpChange_V4.exe")
            else:
                Flyout.create(
                    icon=InfoBarIcon.SUCCESS,
                    title=f'托盘程序已在运行',
                    content="请勿重复运行 ~o( =∩ω∩= )m",
                    target=self.ToACG,
                    parent=self,
                    isClosable=True,

                )
        except:
            Flyout.create(
                icon=InfoBarIcon.ERROR,
                title=f'无法启动功能',
                content="文件可能已经丢失或损坏 (っ °Д °;)っ",
                target=self.ToACG,
                parent=self,
                isClosable=True,

            )

    # def ToPixivClicked(self):
    #     self.OpacityAniStackedWidget.setCurrentIndex(2)
    #     self.TopMenu.setCurrentItem(self.page_3.objectName())
    #     print("ToPixivClicked")

    def ToAIClicked(self):
        # self.OpacityAniStackedWidget.setCurrentIndex(3)
        # self.TopMenu.setCurrentItem(self.page_5.objectName())
        print("ToAIClicked")
        try:
            if not self.is_process_running("Wallpaper_Gradient.exe"):
                os.startfile("Wallpaper_Gradient.exe")
            else:
                Flyout.create(
                    icon=InfoBarIcon.SUCCESS,
                    title=f'制作窗口已经打开',
                    content="请勿重复运行 o(*￣▽￣*)ブ",
                    target=self.ToAI,
                    parent=self,
                    isClosable=True,

                )
        except:
            Flyout.create(
                icon=InfoBarIcon.ERROR,
                title=f'无法启动功能',
                content="文件可能已经丢失或损坏 /(ㄒoㄒ)/~~",
                target=self.ToAI,
                parent=self,
                isClosable=True,

            )

    def ACGUseContent(self, checked):
        if checked:
            self.ACGKind.clear()
            self.ACGKind.addItem("随机")
            self.ACGKind.addItem("精选")
            self.ACGKind.addItem("白毛")
            self.ACGKind.addItem("兽娘")
            self.ACGKind.addItem("星空")
            self.ACGKind.setCurrentIndex(0)

    def ACGUseSize(self, checked):
        if checked:
            self.ACGKind.clear()
            self.ACGKind.addItem("电脑壁纸")
            self.ACGKind.addItem("手机壁纸")
            self.ACGKind.setCurrentIndex(0)

    def ACG_Sl_ValueChanged(self):
        self.ACGNumber.setValue(self.ACGSlider.value())

    def ACG_Sp_ValueChanged(self):
        self.ACGSlider.setValue(self.ACGNumber.value())

    def ACG_I_IndexChanged(self):
        print("方向改变页面")
        self.ACGShowNumber.setValue(self.ACGImages.currentIndex() + 1)
        self.ACGShow.setCurrentIndex(self.ACGShowNumber.value() - 1)

    def ACG_S_IndexChanged(self):
        print("显示器改变页面")
        self.ACGShowNumber.setValue(self.ACGShow.currentIndex() + 1)
        self.ACGImages.setCurrentIndex(self.ACGShowNumber.value() - 1)

    def ACG_Ssp_ValueChanged(self):
        print("数值改变页面")
        self.ACGShow.setCurrentIndex(self.ACGShowNumber.value() - 1)
        self.ACGImages.setCurrentIndex(self.ACGShow.currentIndex())

    def ACGStartGenerator(self):
        if not self.is_connected():
            msg_box = QMessageBox()
            msg_box.setWindowTitle("没有网络可供使用")
            msg_box.setText("壁纸生成器 无法生成壁纸，因为需要一个活动的网络连接，但您的电脑没有链接到任何可用的网络。\n\n解决方案：单击系统任务栏右下角的网络图标，更换网络后重试。或右键网络图标，选择“诊断网络问题”或“疑难解答”。")
            msg_box.setIcon(QMessageBox.Icon.Critical)
            msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg_box.show()
            msg_box.exec()

            self.ACGStart.setText("生成")

            self.ACGStart.setEnabled(True)
            self.ACGProgress.setVisible(False)
            self.TopMenu.setEnabled(True)

            Flyout.create(
                icon=InfoBarIcon.WARNING,
                title=f'生成未成功',
                content=r"请检查您的网络后重试 {{{(>_<)}}}",
                target=self.ACGStart,
                parent=self,
                isClosable=True,

            )
            return

        try:
            print("StartGenerate")

    #         view = FlyoutView('开始生成', "正在生成 100 张，请耐心等待( •̀ ω •́ )✧", None, None, True)
    #         BallonMessage = Flyout(view)
    #         BallonMessage.setStyleSheet("background: transparent;\n"
    # "border: none;")
            self.ACGStart.setEnabled(False)
            self.ACGProgress.setVisible(True)
            self.TopMenu.setEnabled(False)

            match self.ACGKind.currentText():
                case "随机":
                    api = "https://api.iw233.cn/api.php?sort=random"
                    print("0")
                case "精选":
                    api = "https://api.iw233.cn/api.php?sort=top"
                    print("1")
                case "白毛":
                    api = "https://api.iw233.cn/api.php?sort=yin"
                    print("2")
                case "星空":
                    api = "https://api.iw233.cn/api.php?sort=xing"
                    print("3")
                case "兽娘":
                    api = "https://api.iw233.cn/api.php?sort=cat"
                    print("4")
                case "电脑壁纸":
                    api = "https://api.iw233.cn/api.php?sort=pc"
                    print("5")
                case "手机壁纸":
                    api = "https://api.iw233.cn/api.php?sort=mp"
                    print("6")

            Flyout.create(
                icon=InfoBarIcon.INFORMATION,
                title=f'{self.ACGKind.currentText()}生成',
                content=f"正在生成 {self.ACGNumber.value()} 张，请耐心等待( •̀ ω •́ )✧",
                target=self.ACGStart,
                parent=self,
                isClosable=True,

            )

            parameters = {
                "type": "json",
                'num': self.ACGNumber.value()
            }

            response = requests.get(api, params=parameters)
            print(parameters)
            outputurl = response.json()
            print(outputurl)
            output = outputurl["pic"]
            print(output)

            # current_directory = os.getcwd()

            # folder_name = 'generated_pixmap'

            # folder_path = os.path.join(current_directory, folder_name)

            # # 检查文件夹是否存在
            # if not os.path.exists(folder_path):
            #     os.makedirs(folder_path)
            #     print(f'文件夹 "{folder_name}" 已创建在 {folder_path}')
            # else:
            #     print(f'文件夹 "{folder_name}" 已存在于 {folder_path}')

            now = datetime.now()
            # 提取年月日
            month = now.month
            day = now.day
            # 提取时分秒
            hour = now.hour
            minute = now.minute
            second = now.second
            second_start = time.time()

            saved_filename = f"{month}-{day}_{hour}-{minute}-{second}"
            download_threads = []
            self.completed_threads = 0
            self.GeneratedACG = []

            print("文件名日期")

            for i in range(len(output)):
                if i != 0:
                    save = os.path.join(
                        self.settings[0], saved_filename + f"_{self.ACGKind.currentText()}_({i}).png")
                else:
                    save = os.path.join(
                        self.settings[0], saved_filename + f"_{self.ACGKind.currentText()}.png")
                url = output[i]
                # 创建并启动一个新的下载线程
                print(save)
                thread = threading.Thread(
                    target=self.download_image, args=(url, save, i))
                thread.start()

                # 将下载线程添加到列表中
                download_threads.append(thread)

            while self.completed_threads < len(output):
                self.ACGStart.setText(
                    f"正在生成 {self.completed_threads}/{len(output)} 张")
                QtCore.QCoreApplication.processEvents()

            for thread in download_threads:
                thread.join()

            # self.GeneratedACG = ["E:\壁纸生成器\Wallpaper-generator\图像生成插件\generated_pixmap\8-2_17-31-2_白毛_(5).png"]

            self.ACGImages.clear()

            for m in range(len(self.GeneratedACG)):
                self.ACGImages.addImage(self.GeneratedACG[m])
                time.sleep(0.05)

            self.ACGShow.setPageNumber(self.ACGImages.count())
            self.update_background()

            self.ACGShowNumber.setMinimum(1)
            self.ACGShowNumber.setMaximum(len(self.GeneratedACG))
            self.ACGShowNumber.setValue(1)

            self.ACGStart.setText("生成")

            self.ACGStart.setEnabled(True)
            self.ACGProgress.setVisible(False)
            self.TopMenu.setEnabled(True)

            Flyout.create(
                icon=InfoBarIcon.SUCCESS,
                title=f'已生成，耗时 {round(time.time() - second_start, 2)} 秒。',
                content=f"所有图片生成完毕啦！在设置的保存路径中找到它们吧ο(=•ω＜=)ρ⌒☆",
                target=self.ACGStart,
                parent=self,
                isClosable=True,

            )
        except (TimeoutError, ConnectionError, ConnectionRefusedError, ConnectionResetError, ConnectionAbortedError, requests.exceptions.ConnectionError) as e:

            e_list = str(traceback.format_exc()).split(
                "\nDuring handling of the above exception, another exception occurred:\n")
            msg_box = QMessageBox()
            msg_box.setWindowTitle("由于遇到错误，壁纸生成停止")
            msg_box.setText(
                "网络超时，请检查网络速度，或更换网络、重启网络适配器后再试。在尝试以上方法无果后，可将以下详细信息截图并反馈：\n\n" + e_list[0] + "\n" + e_list[len(e_list) - 1])
            msg_box.setIcon(QMessageBox.Icon.Warning)
            msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg_box.show()
            msg_box.exec()

            self.ACGStart.setText("生成")

            self.ACGStart.setEnabled(True)
            self.ACGProgress.setVisible(False)
            self.TopMenu.setEnabled(True)

            Flyout.create(
                icon=InfoBarIcon.WARNING,
                title=f'生成意外结束',
                content=f"检查弹出的窗口信息，并向我们反馈必要的内容，谢谢帮助o(TヘTo)",
                target=self.ACGStart,
                parent=self,
                isClosable=True,

            )

        except MemoryError as e:
            msg_box = QMessageBox()
            msg_box.setWindowTitle("由于遇到错误，壁纸生成停止")
            msg_box.setText("计算机中已无可用内存，无法保存或载入图片。")
            msg_box.setIcon(QMessageBox.Icon.Critical)
            msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg_box.show()
            msg_box.exec()

            self.ACGStart.setText("生成")

            self.ACGStart.setEnabled(True)
            self.ACGProgress.setVisible(False)
            self.TopMenu.setEnabled(True)

            Flyout.create(
                icon=InfoBarIcon.ERROR,
                title=f'生成意外结束',
                content=f"检查弹出的窗口信息，并向我们反馈必要的内容，谢谢帮助o(TヘTo)",
                target=self.ACGStart,
                parent=self,
                isClosable=True,

            )

        except SystemError as e:
            msg_box = QMessageBox()
            msg_box.setWindowTitle("由于遇到错误，壁纸生成停止")
            msg_box.setText(
                "您的系统发生错误，导致阻断了壁纸继续生成或载入，但这不是我们导致的。您可将以下详细信息截图并反馈我们或 Microsoft 工作人员：\n\n" + traceback.format_exc())
            msg_box.setIcon(QMessageBox.Icon.Critical)
            msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg_box.show()
            msg_box.exec()

            self.ACGStart.setText("生成")

            self.ACGStart.setEnabled(True)
            self.ACGProgress.setVisible(False)
            self.TopMenu.setEnabled(True)

            Flyout.create(
                icon=InfoBarIcon.ERROR,
                title=f'生成意外结束',
                content=f"检查弹出的窗口信息，并向我们反馈必要的内容，谢谢帮助o(TヘTo)",
                target=self.ACGStart,
                parent=self,
                isClosable=True,

            )

        except OverflowError as e:
            msg_box = QMessageBox()
            msg_box.setWindowTitle("由于遇到错误，壁纸生成停止")
            msg_box.setText(
                "这是一个巧合——因为生成的壁纸分辨率太高了，您的电脑发生了崩溃。请重新尝试生成壁纸，或前往保存路径查看已经生成的壁纸。\n如果多次生成均为这种情况，您可将以下详细信息反馈给我们：\n\n" + traceback.format_exc())
            msg_box.setIcon(QMessageBox.Icon.Warning)
            msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg_box.show()
            msg_box.exec()

            self.ACGStart.setText("生成")

            self.ACGStart.setEnabled(True)
            self.ACGProgress.setVisible(False)
            self.TopMenu.setEnabled(True)

            Flyout.create(
                icon=InfoBarIcon.WARNING,
                title=f'生成意外结束',
                content=f"检查弹出的窗口信息，并向我们反馈必要的内容，谢谢帮助o(TヘTo)",
                target=self.ACGStart,
                parent=self,
                isClosable=True,

            )

        except Exception as e:
            print(traceback.format_exc())
            msg_box = QMessageBox()
            msg_box.setWindowTitle("由于遇到错误，壁纸生成停止")
            msg_box.setText(
                "由于一个意外的错误，无法继续生成壁纸。可将以下详细信息截图并反馈：\n\n" + traceback.format_exc())
            msg_box.setIcon(QMessageBox.Icon.Critical)
            msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg_box.show()
            msg_box.exec()

            self.ACGStart.setText("生成")

            self.ACGStart.setEnabled(True)
            self.ACGProgress.setVisible(False)
            self.TopMenu.setEnabled(True)

            Flyout.create(
                icon=InfoBarIcon.ERROR,
                title=f'生成意外结束',
                content=f"检查弹出的窗口信息，并向我们反馈必要的内容，谢谢帮助o(TヘTo)",
                target=self.ACGStart,
                parent=self,
                isClosable=True,

            )


# ———————————————————————————————————————
# ————————————Interaction-Pixiv——————————
# ———————————————————————————————————————

    def verfiy_pixiv(self, file_path):
        try:
            img = Image.open(file_path)
            img.verify()  # 验证图像
            img.close()
            return True
        except (IOError, SyntaxError) as e:
            print(f"Error: {e}")
            return False

    def download_pixiv(self, url, info_dict, i):
        print(f'Thread {i} started {url}')
        headers = {"Referer": "https://www.pixiv.net"}
        try:
            if self.settings[1] == "None":
                image = requests.get(url, headers=headers)
            else:
                image = requests.get(url)
            with open(info_dict["save"], 'wb') as f:
                f.write(image.content)  # 保存图片
            if self.verfiy_pixiv(info_dict["save"]) == False:
                print(info_dict["save"] + " 失败！！！！！！")
                os.remove(info_dict["save"])
            else:
                print(info_dict["save"] + " 结束")
                self.GeneratedPixiv.append(info_dict)
        except Exception as e:
            print(e)

        self.completed_threads += 1

    def ShowSetBackgroundPixiv(self, target: HorizontalFlipView):
        self.PixivCommandBar = CommandBarView(self)
        # self.PixivCommandBar.setObjectName(u"PixivCommandBar")
        # self.PixivCommandBar.setMinimumSize(QSize(1, 34))
        # self.PixivCommandBar.setLayoutDirection(Qt.LeftToRight)
        # self.PixivCommandBar.setAutoFillBackground(False)
        # self.PixivCommandBar.setFrameShape(QFrame.NoFrame)
        # self.PixivCommandBar.setFrameShadow(QFrame.Plain)
        self.PixivCommandBar.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        # self.PixivCommandBar.addAction(Action(FluentIcon.IMAGE_EXPORT, "设为壁纸", self))
        action = Action(FluentIcon.PHOTO, os.path.basename(
            self.GeneratedPixiv[self.PixivImages.currentIndex()]['save']), self)
        action.triggered.connect(lambda: os.startfile(
            self.GeneratedPixiv[self.PixivImages.currentIndex()]['save']))
        self.PixivCommandBar.addAction(action=action)
        action = Action(FluentIcon.CERTIFICATE, "Pixiv 信息", self)
        action.triggered.connect(self.ShowPixivInfo)
        self.PixivCommandBar.addAction(action=action)
        action = Action(FluentIcon.IMAGE_EXPORT, "设为壁纸", self)
        action.triggered.connect(self.PixivSetBackground)
        self.PixivCommandBar.addAction(action=action)
        action = Action(FluentIcon.FOLDER, "在资源管理器中打开", self)
        # os.system(f'explorer /select, {os.path.realpath(self.GeneratedPixiv[self.PixivImages.currentIndex()]['save'])}')
        action.triggered.connect(lambda: os.startfile(os.path.dirname(
            self.GeneratedPixiv[self.PixivImages.currentIndex()]['save'])))
        self.PixivCommandBar.addAction(action=action)
        self.PixivCommandBar.resizeToSuitableWidth()
        Flyout.make(self.PixivCommandBar, target, self,
                    FlyoutAnimationType.DROP_DOWN)

    def ShowPixivInfo(self):
        if {self.GeneratedPixiv[self.PixivImages.currentIndex()]['aiType']} == 1:
            IsAI = "是"
        else:
            IsAI = "否"

        show_info = f'''作品名称：{self.GeneratedPixiv[self.PixivImages.currentIndex()]['title']}
作品 Pixiv ID：{self.GeneratedPixiv[self.PixivImages.currentIndex()]['pid']}
作者名称：{self.GeneratedPixiv[self.PixivImages.currentIndex()]['author']}
作者 User ID：{self.GeneratedPixiv[self.PixivImages.currentIndex()]['uid']}
作品画幅（长）：{self.GeneratedPixiv[self.PixivImages.currentIndex()]['width']}
作品画幅（宽）：{self.GeneratedPixiv[self.PixivImages.currentIndex()]['height']}
作品类型：{self.GeneratedPixiv[self.PixivImages.currentIndex()]['ext']}
是否 AI 参与：{IsAI}
上传日期：{self.GeneratedPixiv[self.PixivImages.currentIndex()]['uploadDate']}
本地路径：{self.GeneratedPixiv[self.PixivImages.currentIndex()]['save']}
包含本作品的标签 Tags：{self.GeneratedPixiv[self.PixivImages.currentIndex()]['tags']}
'''
        BatchWindow = QDialog()
        ui1 = DialogUi.Ui_Form(self.GeneratedPixiv[self.PixivImages.currentIndex(
        )]['title'], show_info, "好的", "取消", "True")
        ui1.setupUi(BatchWindow)
        BatchWindow.exec_()

    def PixivSetBackground(self):
        new_wall: str = '"{}"'.format(self.GeneratedPixiv[self.PixivImages.currentIndex()]['save'])
        # ctypes.windll.user32.SystemParametersInfoW(20, 0, new_wall, 3)
        # os.startfile("Set_Wallpaper.exe", arguments=new_wall)
        # process = subprocess.Popen(executable="Set_Wallpaper.exe", args=new_wall)
        process = subprocess.Popen(f"Set_Wallpaper.exe {new_wall}")
        process.wait()

        Flyout.create(
            icon=InfoBarIcon.SUCCESS,
            title=f'壁纸已设置o(*≧▽≦)ツ',
            content=os.path.basename(new_wall),
            target=self.PixivImages,
            parent=self,
            isClosable=True,

        )

        print("PixivSetBackground: " + new_wall)

    def Pixiv_Sl_ValueChanged(self):
        self.PixivNumber.setValue(self.PixivSlider.value())

    def Pixiv_Sp_ValueChanged(self):
        self.PixivSlider.setValue(self.PixivNumber.value())

    def Pixiv_I_IndexChanged(self):
        print("方向改变页面")
        self.PixivShowNumber.setValue(self.PixivImages.currentIndex() + 1)
        self.PixivShow.setCurrentIndex(self.PixivShowNumber.value() - 1)

    def Pixiv_S_IndexChanged(self):
        print("显示器改变页面")
        self.PixivShowNumber.setValue(self.PixivShow.currentIndex() + 1)
        self.PixivImages.setCurrentIndex(self.PixivShowNumber.value() - 1)

    def Pixiv_Ssp_ValueChanged(self):
        print("数值改变页面")
        self.PixivShow.setCurrentIndex(self.PixivShowNumber.value() - 1)
        self.PixivImages.setCurrentIndex(self.PixivShow.currentIndex())

    def PixivshowDialog(self):
        title = '免责声明'
        content = """思锐工作室 对于《壁纸生成器》系列产品的用户须知和免责声明（以下简称《声明》），请所有用户在使用本产品前务必认真仔细阅读。使用本产品即代表您同意本《声明》。
1. 本软件依赖于 Miklroi API、Lolicon API 等其他接口和开源项目，所有本产品相关的内容及所生成的任何图片均不可以用作任何商业用途，生成的图片由其作者保留所有权利，思锐工作室及其用户不承担任何责任和义务保护图片资源的规范和权利不受侵犯。若是AI生成的图片资源，则该图片无实际权利所有人，或按照生成该图片的AI机构认定权利归属。
2. 本产品永不用于任何商业用途。若有图片作者认为本系列产品侵犯了其正当权益，请与接口提供商和开源项目负责人联系和交涉，思锐工作室及其用户不承担任何责任。
3. 本产品所生成的任何图片资源均来源于接口提供商和开源项目，由接口提供商和开源项目通过爬取或代理（《Pixiv 生成器》除外）网络图片资源并返回给本产品。若图片有任何不规范的内容，思锐工作室及其用户不承担任何责任，所有图片资源均来自于网络。
4. 请所有用户遵守以上须知并严格遵守中华人民共和国法律，不得用本产品进行任何非法活动或侵犯他人权利的活动，不得试图使用本产品生成任何不符合法律或规范的图片。
5. 本产品仅供学习交流和娱乐使用，所有保存的图片请于24小时内删除。
6. 变更通知
若本《声明》的内容有任何变更，恕我们不另行通知，请用户每次更新本产品后及时阅读本《声明》以获得最新信息。
思锐工作室 2024.1.28 思锐工作室保留所有权和最终解释权"""
        # w = MessageDialog(title, content, self)   # Win10 style message box
        # w = MessageBox(title, content, self)
#         w.setStyleSheet(u"border-image: white;\n"
# "background: white;")
        # w = Dialog(title, content, self)

        # d = QApplication(sys.argv)
        # d_window = DialogWindow(None, title=title, content=content)
        # d_window.show()
        # print("Show dialog window.")
        # d.exec()

        BatchWindow = QDialog()
        ui1 = DialogUi.Ui_Form(title, content, "同意", "不同意", "False")
        ui1.setupUi(BatchWindow)
        BatchWindow.exec_()
        result = ui1.IsTF()
        print(result)

        if result != "T":
            sys.exit(0)

        print("Show dialog window.")

    def Pixiv_fetch_data(self, url):
        print("Pixiv_fetch_data")
        try:
            response = requests.get(url)
            self.pixiv_request = response.json()
        except:
            self.pixiv_request = "Failed\n" + traceback.format_exc()
        print(f"response: {self.pixiv_request}")

        # print(args)
        # print(kwargs)

    async def PixivStartGenerator(self):
        if not self.is_connected():
            msg_box = QMessageBox()
            msg_box.setWindowTitle("没有网络可供使用")
            msg_box.setText("壁纸生成器 无法生成壁纸，因为需要一个活动的网络连接，但您的电脑没有链接到任何可用的网络。\n\n解决方案：单击系统任务栏右下角的网络图标，更换网络后重试。或右键网络图标，选择“诊断网络问题”或“疑难解答”。")
            msg_box.setIcon(QMessageBox.Icon.Critical)
            msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg_box.show()
            msg_box.exec()

            self.ACGStart.setText("生成")

            self.ACGStart.setEnabled(True)
            self.ACGProgress.setVisible(False)
            self.TopMenu.setEnabled(True)

            Flyout.create(
                icon=InfoBarIcon.WARNING,
                title=f'生成未成功',
                content=r"请检查您的网络后重试 {{{(>_<)}}}",
                target=self.PixivStart,
                parent=self,
                isClosable=True,

            )
            return
        
        try:
            print("StartPixiv")

    #         view = FlyoutView('开始生成', "正在生成 100 张，请耐心等待( •̀ ω •́ )✧", None, None, True)
    #         BallonMessage = Flyout(view)
    #         BallonMessage.setStyleSheet("background: transparent;\n"
    # "border: none;")
            self.PixivStart.setEnabled(False)
            self.PixivProgress.setVisible(True)
            self.TopMenu.setEnabled(False)

            api = "https://api.lolicon.app/setu/v2?"

            if self.settings[1] != None:
                show_text = f'正在使用代理链接 Pixiv.net'
            else:
                show_text = f'正在链接 Pixiv.net'

            to_generate_num = self.PixivNumber.value()

            Flyout.create(
                icon=InfoBarIcon.INFORMATION,
                title=show_text,
                content=f"正在生成 {to_generate_num} 张，请耐心等待( •̀ ω •́ )✧",
                target=self.PixivStart,
                parent=self,
                isClosable=True,

            )

            print("Pixiv 拼接 Url")

            url_setted = api + "num=" + str(to_generate_num)

            tags = self.PixivTags.text().split("&")
            for TagIndex in range(len(tags)):
                url_setted = url_setted + "&tag=" + tags[TagIndex]

            url_setted = url_setted + "&uid=" + self.PixivUID.text()

            if self.PixivIsR18.isChecked() == True:
                url_setted = url_setted + "&r18=2"
            else:
                url_setted = url_setted + "&r18=0"

            if self.PixivIsAI.isChecked() == True:
                url_setted = url_setted + "&excludeAI=ture"
            else:
                url_setted = url_setted + "&excludeAI=false"

            match self.settings[1]:
                case "Insider":
                    # "&proxy=pixiv.t.sr-studio.top"
                    url_setted = url_setted + "&proxy=pixiv.t.sr-studio.top"
                case "None":
                    url_setted = url_setted + "&proxy=i.pximg.net"
                case _:
                    url_setted = url_setted + "&proxy=" + self.settings[1]

            print("GetPixiv")

            print(url_setted)
            self.pixiv_request: any = None

            threadR = threading.Thread(
                target=self.Pixiv_fetch_data, args=(url_setted,))
            threadR.start()

            while self.pixiv_request == None:
                QtCore.QCoreApplication.processEvents()

            if "Failed" in self.pixiv_request:
                raise ConnectionError(self.pixiv_request)

            outputurl = self.pixiv_request
            # outputurl = await self.Pixiv_fetch_data(url_setted)
            print(outputurl)
            data_normal = outputurl['data']
            print(data_normal)

            download_threads = []
            self.completed_threads = 0
            self.GeneratedPixiv = []

            print("进入生成循环")

            if len(data_normal) < to_generate_num:
                msg_box = QMessageBox()
                msg_box.setWindowTitle("筛选条件过于严格")
                msg_box.setText(
                    f"在该UID的作者的指定 Tags 下，图片数量不足指定的数量。最多生成 {len(data_normal)} 张。\n按 Enter 继续生成。")
                msg_box.setIcon(QMessageBox.Icon.Warning)
                msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
                msg_box.show()
                msg_box.exec()

            i = 0
            for data in data_normal:
                # data = data_normal[i]

                saved_file = self.clean_filename(data['title'])

                saved_filename = os.path.join(
                    self.settings[0], f"{saved_file}.png")
                s_n = 0

                while os.path.exists(saved_filename):
                    s_n += 1
                    saved_filename = os.path.join(
                        self.settings[0], f"{saved_file} (" + str(s_n) + ").png")

                info_dict = {
                    "pid": data['pid'],
                    "uid": data['uid'],
                    "title": data['title'],
                    "author": data['author'],
                    "width": data['width'],
                    "height": data['height'],
                    "tags": data['tags'],
                    "ext": data['ext'],
                    "aiType": data['aiType'],
                    # Convert timestamp to yyyy-mm-dd format
                    "uploadDate": datetime.fromtimestamp(data['uploadDate'] / 1000).strftime('%Y-%m-%d'),
                    "save": saved_filename
                }

                url = data['urls']['original']
                # 创建并启动一个新的下载线程
                print(saved_filename)
                thread = threading.Thread(
                    target=self.download_pixiv, args=(url, info_dict, i))
                thread.start()

                # 将下载线程添加到列表中
                download_threads.append(thread)
                i += 1

            while self.completed_threads < len(data_normal):
                self.PixivStart.setText(
                    f"正在生成 {self.completed_threads}/{len(data_normal)} 张")
                QtCore.QCoreApplication.processEvents()

            for thread in download_threads:
                thread.join()

            # self.GeneratedPixiv = ["E:\壁纸生成器\Wallpaper-generator\图像生成插件\generated_pixmap\8-2_17-31-2_白毛_(5).png"]

            self.PixivImages.clear()

            for m in range(len(self.GeneratedPixiv)):
                self.PixivImages.addImage(self.GeneratedPixiv[m]['save'])
                time.sleep(0.05)

            self.PixivShow.setPageNumber(self.PixivImages.count())
            self.update_background()

            self.PixivShowNumber.setMinimum(1)
            self.PixivShowNumber.setMaximum(len(self.GeneratedPixiv))
            self.PixivShowNumber.setValue(1)

            self.PixivStart.setText("生成")

            self.PixivStart.setEnabled(True)
            self.PixivProgress.setVisible(False)
            self.TopMenu.setEnabled(True)

            if len(self.GeneratedPixiv) < to_generate_num:
                msg_box = QMessageBox()
                msg_box.setWindowTitle("Pixiv 生成时发生部分丢失")
                msg_box.setText(
                    f"有 {to_generate_num - len(self.GeneratedPixiv)} 张图片在生成时发生警告。但如果您没有成功生成至少 1 张图片，请检查代理链接状态，或更换网络后重试。\n为保证图片的完整性，壁纸生成器 撤回了这些图片。最终生成 {len(self.GeneratedPixiv)} 张。")
                msg_box.setIcon(QMessageBox.Icon.Warning)
                msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
                msg_box.show()
                msg_box.exec()

                Flyout.create(
                    icon=InfoBarIcon.WARNING,
                    title=f'已生成，但存在警告',
                    content=f"图片生成完毕啦！在设置的保存路径中找到它们吧ο(=•ω＜=)ρ⌒☆",
                    target=self.PixivStart,
                    parent=self,
                    isClosable=True,

                )
            else:
                Flyout.create(
                    icon=InfoBarIcon.SUCCESS,
                    title=f'已生成',
                    content=f"所有图片生成完毕啦！在设置的保存路径中找到它们吧ο(=•ω＜=)ρ⌒☆",
                    target=self.PixivStart,
                    parent=self,
                    isClosable=True,

                )

        except IndexError as e:
            msg_box = QMessageBox()
            msg_box.setWindowTitle("没有图片")
            msg_box.setText(
                "在该UID的作者的指定 Tags 下，没有符合要求的图片。请检查指定的作者UID和标签是否正确。尝试在更换指定作者，或筛选条件后重试。")
            msg_box.setIcon(QMessageBox.Icon.Warning)
            msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg_box.show()
            msg_box.exec()

            self.PixivStart.setText("生成")

            self.PixivStart.setEnabled(True)
            self.PixivProgress.setVisible(False)
            self.TopMenu.setEnabled(True)

            Flyout.create(
                icon=InfoBarIcon.WARNING,
                title=f'我们尽力了',
                content=f"但是在 Pixiv.net 中确实找不到您要求的图片o(TヘTo)",
                target=self.PixivStart,
                parent=self,
                isClosable=True,

            )

        except (TimeoutError, ConnectionError, ConnectionRefusedError, ConnectionResetError, ConnectionAbortedError, requests.exceptions.ConnectionError) as e:

            e_list = str(e).split(
                "\nDuring handling of the above exception, another exception occurred:\n")
            msg_box = QMessageBox()
            msg_box.setWindowTitle("由于遇到错误，壁纸生成停止")
            msg_box.setText(
                "网络超时，请检查网络速度，或更换网络、重启网络适配器后再试。在尝试以上方法无果后，可将以下详细信息截图并反馈：\n\n" + e_list[0] + "\n" + e_list[len(e_list) - 1])
            msg_box.setIcon(QMessageBox.Icon.Warning)
            msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg_box.show()
            msg_box.exec()

            self.PixivStart.setText("生成")

            self.PixivStart.setEnabled(True)
            self.PixivProgress.setVisible(False)
            self.TopMenu.setEnabled(True)

            Flyout.create(
                icon=InfoBarIcon.WARNING,
                title=f'生成意外结束',
                content=f"检查弹出的窗口信息，并向我们反馈必要的内容，谢谢帮助o(TヘTo)",
                target=self.PixivStart,
                parent=self,
                isClosable=True,

            )

        except MemoryError as e:
            msg_box = QMessageBox()
            msg_box.setWindowTitle("由于遇到错误，壁纸生成停止")
            msg_box.setText("计算机中已无可用内存，无法保存或载入图片。")
            msg_box.setIcon(QMessageBox.Icon.Critical)
            msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg_box.show()
            msg_box.exec()

            self.PixivStart.setText("生成")

            self.PixivStart.setEnabled(True)
            self.PixivProgress.setVisible(False)
            self.TopMenu.setEnabled(True)

            Flyout.create(
                icon=InfoBarIcon.ERROR,
                title=f'生成意外结束',
                content=f"检查弹出的窗口信息，并向我们反馈必要的内容，谢谢帮助o(TヘTo)",
                target=self.PixivStart,
                parent=self,
                isClosable=True,

            )

        except SystemError as e:
            msg_box = QMessageBox()
            msg_box.setWindowTitle("由于遇到错误，壁纸生成停止")
            msg_box.setText(
                "您的系统发生错误，导致阻断了壁纸继续生成或载入，但这不是我们导致的。您可将以下详细信息截图并反馈我们或 Microsoft 工作人员：\n\n" + traceback.format_exc())
            msg_box.setIcon(QMessageBox.Icon.Critical)
            msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg_box.show()
            msg_box.exec()

            self.PixivStart.setText("生成")

            self.PixivStart.setEnabled(True)
            self.PixivProgress.setVisible(False)
            self.TopMenu.setEnabled(True)

            Flyout.create(
                icon=InfoBarIcon.ERROR,
                title=f'生成意外结束',
                content=f"检查弹出的窗口信息，并向我们反馈必要的内容，谢谢帮助o(TヘTo)",
                target=self.PixivStart,
                parent=self,
                isClosable=True,

            )

        except OverflowError as e:
            msg_box = QMessageBox()
            msg_box.setWindowTitle("由于遇到错误，壁纸生成停止")
            msg_box.setText(
                "这是一个巧合——因为生成的壁纸分辨率太高了，您的电脑发生了崩溃。请重新尝试生成壁纸，或前往保存路径查看已经生成的壁纸。\n如果多次生成均为这种情况，您可将以下详细信息反馈给我们：\n\n" + traceback.format_exc())
            msg_box.setIcon(QMessageBox.Icon.Warning)
            msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg_box.show()
            msg_box.exec()

            self.PixivStart.setText("生成")

            self.PixivStart.setEnabled(True)
            self.PixivProgress.setVisible(False)
            self.TopMenu.setEnabled(True)

            Flyout.create(
                icon=InfoBarIcon.WARNING,
                title=f'生成意外结束',
                content=f"检查弹出的窗口信息，并向我们反馈必要的内容，谢谢帮助o(TヘTo)",
                target=self.PixivStart,
                parent=self,
                isClosable=True,

            )

        except Exception as e:
            print(traceback.format_exc())
            msg_box = QMessageBox()
            msg_box.setWindowTitle("由于遇到错误，壁纸生成停止")
            msg_box.setText(
                "由于一个意外的错误，无法继续生成壁纸。可将以下详细信息截图并反馈：\n\n" + traceback.format_exc())
            msg_box.setIcon(QMessageBox.Icon.Critical)
            msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg_box.show()
            msg_box.exec()

            self.PixivStart.setText("生成")

            self.PixivStart.setEnabled(True)
            self.PixivProgress.setVisible(False)
            self.TopMenu.setEnabled(True)

            Flyout.create(
                icon=InfoBarIcon.ERROR,
                title=f'生成意外结束',
                content=f"检查弹出的窗口信息，并向我们反馈必要的内容，谢谢帮助o(TヘTo)",
                target=self.PixivStart,
                parent=self,
                isClosable=True,

            )

# ———————————————————————————————————————
# ————————————Interaction-AI—————————————
# ———————————————————————————————————————

    def updateWorkingList(self, L: list):

        if len(L) == 0:
            self.AIList.clear()
            self.AIProgress.setVisible(False)
        else:
            self.AIList.clear()
            self.AIProgress.setVisible(True)
            for i, Info in enumerate(L):
                for j in range(2):
                    self.AIList.setItem(i, j, QTableWidgetItem(Info[j]))

        self.AIList.setHorizontalHeaderLabels(['标签', '进度'])
        if len(L) != 0:
            self.AIList.resizeColumnsToContents()

    def DoInterval(self):
        self.interval = 0  # 调试时为0，发布时为60————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
        while self.interval > 0:
            self.interval -= 1
            time.sleep(1)

    def ShowSetBackgroundAI(self, target: HorizontalFlipView):
        self.AICommandBar = CommandBarView(self)
        # self.AICommandBar.setObjectName(u"AICommandBar")
        # self.AICommandBar.setMinimumSize(QSize(1, 34))
        # self.AICommandBar.setLayoutDirection(Qt.LeftToRight)
        # self.AICommandBar.setAutoFillBackground(False)
        # self.AICommandBar.setFrameShape(QFrame.NoFrame)
        # self.AICommandBar.setFrameShadow(QFrame.Plain)
        self.AICommandBar.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        # self.AICommandBar.addAction(Action(FluentIcon.IMAGE_EXPORT, "设为壁纸", self))
        action = Action(FluentIcon.PHOTO, os.path.basename(
            self.GeneratedAI[self.AIImages.currentIndex()]), self)
        action.triggered.connect(lambda: os.startfile(
            self.GeneratedAI[self.AIImages.currentIndex()]))
        self.AICommandBar.addAction(action=action)

        action = Action(FluentIcon.IMAGE_EXPORT, "设为壁纸", self)
        action.triggered.connect(self.AISetBackground)
        self.AICommandBar.addAction(action=action)

        action = Action(FluentIcon.FOLDER, "在资源管理器中打开", self)
        # os.system(f'explorer /select, {os.path.realpath(self.GeneratedAI[self.AIImages.currentIndex()])}')
        action.triggered.connect(lambda: os.startfile(
            os.path.dirname(self.GeneratedAI[self.AIImages.currentIndex()])))
        self.AICommandBar.addAction(action=action)

        action = Action(FluentIcon.CLOSE, "清空图片列表 (不会删除图片)", self)
        # os.system(f'explorer /select, {os.path.realpath(self.GeneratedAI[self.AIImages.currentIndex()])}')
        action.triggered.connect(self.clean_AIImages)
        self.AICommandBar.addAction(action=action)

        self.AICommandBar.resizeToSuitableWidth()
        Flyout.make(self.AICommandBar, target, self,
                    FlyoutAnimationType.DROP_DOWN)

    def clean_AIImages(self):
        self.AIImages.clear()
        self.GeneratedAI = []
        self.AIShow.setPageNumber(self.AIImages.count())
        self.AIShowNumber.setValue(0)
        self.AIShowNumber.setMaximum(0)

    def AISetBackground(self):
        new_wall: str = '"{}"'.format(self.GeneratedAI[self.AIImages.currentIndex()])
        # ctypes.windll.user32.SystemParametersInfoW(20, 0, new_wall, 3)
        # os.startfile("Set_Wallpaper.exe", arguments=new_wall)
        # 调用可执行文件并传入参数
        process = subprocess.Popen(f"Set_Wallpaper.exe {new_wall}")
        process.wait()

        Flyout.create(
            icon=InfoBarIcon.SUCCESS,
            title=f'壁纸已设置o(*≧▽≦)ツ',
            content=os.path.basename(new_wall),
            target=self.AIImages,
            parent=self,
            isClosable=True,

        )

        print("AISetBackground: " + new_wall)

    def AI_I_IndexChanged(self):
        print("方向改变页面")
        self.AIShowNumber.setValue(self.AIImages.currentIndex() + 1)
        self.AIShow.setCurrentIndex(self.AIShowNumber.value() - 1)

    def AI_S_IndexChanged(self):
        print("显示器改变页面")
        self.AIShowNumber.setValue(self.AIShow.currentIndex() + 1)
        self.AIImages.setCurrentIndex(self.AIShowNumber.value() - 1)

    def AI_Ssp_ValueChanged(self):
        print("数值改变页面")
        self.AIShow.setCurrentIndex(self.AIShowNumber.value() - 1)
        self.AIImages.setCurrentIndex(self.AIShow.currentIndex())

    def GetAIGenerated(self, ToURL, payload):

        try:
            nice = payload['prompt']

            self.AIWorkingList.append([nice, "等待中"])

            self.updateWorkingList(self.AIWorkingList)

            print(self.AIWorkingList)

            while True:
                if self.AIWorkingList[0][0] == nice:
                    self.AIWorkingList[0][1] = "正在进行"
                    break
                time.sleep(0.1)

            self.updateWorkingList(self.AIWorkingList)
            print(self.AIWorkingList)

            print(f"{ToURL}sdapi/v1/txt2img")
            response = requests.post(
                url=f"{ToURL}sdapi/v1/txt2img", json=payload)
            r = response.json()
            print(r)

            s_n = 0

            if payload['prompt'] == None or payload['prompt'] == "":
                filename = "no_prompt"
            else:
                filename = self.clean_filename(payload['prompt'])

            saved_filename = os.path.join(self.settings[0], f"{filename}.png")

            while os.path.exists(saved_filename):
                s_n += 1
                saved_filename = os.path.join(
                    self.settings[0], f"{filename} (" + str(s_n) + ").png")

            # Decode and save the image.
            with open(saved_filename, 'wb') as f:
                f.write(base64.b64decode(r['images'][0]))

            with open("output.txt", 'w') as f:
                f.write(str(r))

            self.AIWorkingList.pop(0)

            self.updateWorkingList(self.AIWorkingList)

            print(self.AIWorkingList)

            self.update_AIsignal.emit(saved_filename)
        except (TimeoutError, ConnectionError, ConnectionRefusedError, ConnectionResetError, ConnectionAbortedError, requests.exceptions.ConnectionError) as e:

            self.error_AIsignal.emit(f"c⅒{traceback.format_exc()}")

        except MemoryError as e:

            self.error_AIsignal.emit(f"m⅒{traceback.format_exc()}")

        except SystemError as e:
            self.error_AIsignal.emit(f"s⅒{traceback.format_exc()}")

        except OverflowError as e:
            self.error_AIsignal.emit(f"o⅒{traceback.format_exc()}")

        except requests.exceptions.JSONDecodeError as e:
            self.error_AIsignal.emit(f"j⅒{traceback.format_exc()}")

        except KeyError as e:
            self.error_AIsignal.emit(f"k⅒{r}")

        except Exception as e:
            self.error_AIsignal.emit(f"e⅒{traceback.format_exc()}")

    def GetAICompleted(self, saved_filename):
        self.AIImages.addImage(saved_filename)
        self.GeneratedAI.append(saved_filename)

        self.AIShow.setPageNumber(self.AIImages.count())
        self.update_background()

        self.AIShowNumber.setMinimum(1)
        self.AIShowNumber.setMaximum(self.AIImages.count())
        self.AIShowNumber.setValue(1)

    def GetAIFailed(self, em):
        print("receive GetAIFailed")
        em = em.split("⅒")
        print(em)
        e = em[0]

        try:
            match e:
                case "c":
                    raise ConnectionError()
                case "m":
                    raise MemoryError()
                case "s":
                    raise SystemError()
                case "o":
                    raise OverflowError()
                case "j":
                    raise requests.exceptions.JSONDecodeError()
                case "k":
                    raise KeyError()
                case "e":
                    raise Exception()

        except (TimeoutError, ConnectionError, ConnectionRefusedError, ConnectionResetError, ConnectionAbortedError, requests.exceptions.ConnectionError) as e:

            e_list = str(em[1]).split(
                "\nDuring handling of the above exception, another exception occurred:\n")
            msg_box = QMessageBox()
            msg_box.setWindowTitle("由于遇到错误，壁纸生成停止")
            msg_box.setText(
                "网络超时，请检查网络速度，或更换网络、重启网络适配器后再试。在尝试以上方法无果后，可将以下详细信息截图并反馈：\n\n" + e_list[0] + "\n" + e_list[len(e_list) - 1])
            msg_box.setIcon(QMessageBox.Icon.Warning)
            msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg_box.show()
            msg_box.exec()

            self.AIStart.setText("生成")

            self.AIStart.setEnabled(True)
            self.AIProgress.setVisible(False)
            self.TopMenu.setEnabled(True)

            Flyout.create(
                icon=InfoBarIcon.WARNING,
                title=f'生成意外结束',
                content=f"检查弹出的窗口信息，并向我们反馈必要的内容，谢谢帮助o(TヘTo)",
                target=self.AIStart,
                parent=self,
                isClosable=True,

            )
            # pass

        except MemoryError as e:
            msg_box = QMessageBox()
            msg_box.setWindowTitle("由于遇到错误，壁纸生成停止")
            msg_box.setText("计算机中已无可用内存，无法保存或载入图片。")
            msg_box.setIcon(QMessageBox.Icon.Critical)
            msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg_box.show()
            msg_box.exec()

            self.AIStart.setText("生成")

            self.AIStart.setEnabled(True)
            self.AIProgress.setVisible(False)
            self.TopMenu.setEnabled(True)

            Flyout.create(
                icon=InfoBarIcon.ERROR,
                title=f'生成意外结束',
                content=f"检查弹出的窗口信息，并向我们反馈必要的内容，谢谢帮助o(TヘTo)",
                target=self.AIStart,
                parent=self,
                isClosable=True,

            )

        except SystemError as e:
            msg_box = QMessageBox()
            msg_box.setWindowTitle("由于遇到错误，壁纸生成停止")
            msg_box.setText(
                "您的系统发生错误，导致阻断了壁纸继续生成或载入，但这不是我们导致的。您可将以下详细信息截图并反馈我们或 Microsoft 工作人员：\n\n" + em[1])
            msg_box.setIcon(QMessageBox.Icon.Critical)
            msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg_box.show()
            msg_box.exec()

            self.AIStart.setText("生成")

            self.AIStart.setEnabled(True)
            self.AIProgress.setVisible(False)
            self.TopMenu.setEnabled(True)

            Flyout.create(
                icon=InfoBarIcon.ERROR,
                title=f'生成意外结束',
                content=f"检查弹出的窗口信息，并向我们反馈必要的内容，谢谢帮助o(TヘTo)",
                target=self.AIStart,
                parent=self,
                isClosable=True,

            )

        except OverflowError as e:
            msg_box = QMessageBox()
            msg_box.setWindowTitle("由于遇到错误，壁纸生成停止")
            msg_box.setText(
                "这是一个巧合——因为生成的壁纸分辨率太高了，您的电脑发生了崩溃。请重新尝试生成壁纸，或前往保存路径查看已经生成的壁纸。\n如果多次生成均为这种情况，您可将以下详细信息反馈给我们：\n\n" + em[1])
            msg_box.setIcon(QMessageBox.Icon.Warning)
            msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg_box.show()
            msg_box.exec()

            self.AIStart.setText("生成")

            self.AIStart.setEnabled(True)
            self.AIProgress.setVisible(False)
            self.TopMenu.setEnabled(True)

            Flyout.create(
                icon=InfoBarIcon.WARNING,
                title=f'生成意外结束',
                content=f"检查弹出的窗口信息，并向我们反馈必要的内容，谢谢帮助o(TヘTo)",
                target=self.AIStart,
                parent=self,
                isClosable=True,

            )

        except requests.exceptions.JSONDecodeError as e:
            msg_box = QMessageBox()
            msg_box.setWindowTitle("生成已超时")
            msg_box.setText("一张图片的生成时间超出了我们的预期，或生成了无法被读取的内容。请您稍后再试。\n若全部图片均出现此类错误，请反馈给我们，因为这有可能是我们的服务器出现了以外的错误。")
            msg_box.setIcon(QMessageBox.Icon.Warning)
            msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg_box.show()
            msg_box.exec()

            self.AIStart.setText("生成")

            self.AIStart.setEnabled(True)
            self.AIProgress.setVisible(False)
            self.TopMenu.setEnabled(True)

            Flyout.create(
                icon=InfoBarIcon.WARNING,
                title=f'生成意外结束',
                content=f"检查弹出的窗口信息，并向我们反馈必要的内容，谢谢帮助o(TヘTo)",
                target=self.AIStart,
                parent=self,
                isClosable=True,

            )

        except KeyError as e:
            msg_box = QMessageBox()
            msg_box.setWindowTitle("由于遇到错误，壁纸生成停止")
            msg_box.setText(
                "我们的模型服务器发生了错误，可能是因为生成质量超标。建议降低分辨率或超分倍数以避免此问题。\n若多次发生此类错误，可将以下详细信息截图并反馈：\n\n" + em[1])
            msg_box.setIcon(QMessageBox.Icon.Critical)
            msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg_box.show()
            msg_box.exec()

            self.AIStart.setText("生成")

            self.AIStart.setEnabled(True)
            self.AIProgress.setVisible(False)
            self.TopMenu.setEnabled(True)

            Flyout.create(
                icon=InfoBarIcon.ERROR,
                title=f'生成意外结束',
                content=f"检查弹出的窗口信息，并向我们反馈必要的内容，谢谢帮助o(TヘTo)",
                target=self.AIStart,
                parent=self,
                isClosable=True,

            )


        except Exception as e:
            msg_box = QMessageBox()
            msg_box.setWindowTitle("由于遇到错误，壁纸生成停止")
            msg_box.setText(
                "由于一个意外的错误，无法继续生成壁纸。可将以下详细信息截图并反馈：\n\n" + em[1])
            msg_box.setIcon(QMessageBox.Icon.Critical)
            msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg_box.show()
            msg_box.exec()

            self.AIStart.setText("生成")

            self.AIStart.setEnabled(True)
            self.AIProgress.setVisible(False)
            self.TopMenu.setEnabled(True)

            Flyout.create(
                icon=InfoBarIcon.ERROR,
                title=f'生成意外结束',
                content=f"检查弹出的窗口信息，并向我们反馈必要的内容，谢谢帮助o(TヘTo)",
                target=self.AIStart,
                parent=self,
                isClosable=True,

            )

        self.AIWorkingList.pop(0)

        self.updateWorkingList(self.AIWorkingList)

        print(self.AIWorkingList)

    def AISStartGenerator(self):
        if not self.is_connected():
            msg_box = QMessageBox()
            msg_box.setWindowTitle("没有网络可供使用")
            msg_box.setText("壁纸生成器 无法生成壁纸，因为需要一个活动的网络连接，但您的电脑没有链接到任何可用的网络。\n\n解决方案：单击系统任务栏右下角的网络图标，更换网络后重试。或右键网络图标，选择“诊断网络问题”或“疑难解答”。")
            msg_box.setIcon(QMessageBox.Icon.Critical)
            msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg_box.show()
            msg_box.exec()

            self.ACGStart.setText("生成")

            self.ACGStart.setEnabled(True)
            self.ACGProgress.setVisible(False)
            self.TopMenu.setEnabled(True)

            Flyout.create(
                icon=InfoBarIcon.WARNING,
                title=f'生成未成功',
                content=r"请检查您的网络后重试 {{{(>_<)}}}",
                target=self.AIStart,
                parent=self,
                isClosable=True,

            )
            return

        try:
            text = self.GeneratedAI[0]
        except:
            self.GeneratedAI = []

        if len(self.AIWorkingList) == 3:

            Flyout.create(
                icon=InfoBarIcon.ERROR,
                title='无法生成',
                content=f"生成队列已满（3/3），请等待正在队列中的图片完成以腾出空位，继续生成 ::>_<::",
                target=self.AIStart,
                parent=self,
                isClosable=True,

            )

        elif self.interval > 0:

            Flyout.create(
                icon=InfoBarIcon.WARNING,
                title='无法生成',
                content=f"请等待 {self.interval} 秒后重试ヾ(≧へ≦)〃",
                target=self.AIStart,
                parent=self,
                isClosable=True,

            )

        else:
            if os.path.exists("testEd.yaml"):
                with open("testEd.yaml", "r") as file:
                    ToURL = file.read()
            else:
                if not os.path.exists("EndPoint.yaml"):
                    msg_box = QMessageBox()
                    msg_box.setWindowTitle("找不到可信接口")
                    msg_box.setText(
                        "因为接口结束端点不存在。尝试重新安装本程序以解决此问题。")
                    msg_box.setIcon(QMessageBox.Icon.Warning)
                    msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
                    msg_box.show()
                    msg_box.exec()
                    ToURL = "http://127.0.0.1:7860/"
                else:
                    with open("EndPoint.yaml", "r") as file:
                        ToURL = file.read()

            ToURL = ToURL + ("" if ToURL.endswith('/') else "/")

            nice = self.AIGoodTags.toPlainText()

            had_items = False
            for geneating_item in self.AIWorkingList:
                if geneating_item[0] == nice:
                    had_items = True
                    break

            if not had_items:
                not_nice = self.AIBadTags.toPlainText()

                payload = {
                    "prompt": nice,
                    "negative_prompt": not_nice,
                    "styles": [],
                    "seed": -1,  # 使用随机种子
                    "subseed": -1,
                    "subseed_strength": 0,
                    "seed_resize_from_h": -1,
                    "seed_resize_from_w": -1,
                    "sampler_name": "Euler a",  # 采样方法
                    # "scheduler": "string",  #你可以指定具体的调度器名称
                    "batch_size": 1,
                    "n_iter": 1,
                    "steps": 20,  # 迭代步数
                    "cfg_scale": self.AIObey.value(),  # 提示词引导系数
                    "width": 640,  # 你可以根据需要设置更高的分辨率
                    "height": 640,  # 你可以根据需要设置更高的分辨率
                    "restore_faces": False,  # True
                    "tiling": False,  # 设置为False，如果不需要平铺模式
                    "do_not_save_samples": False,
                    "do_not_save_grid": False,
                    "eta": 0,
                    "denoising_strength": 0.5,  # 重绘幅度
                    "s_min_uncond": 0,
                    "s_churn": 0,
                    "s_tmax": 0,
                    "s_tmin": 0,
                    "s_noise": 0,
                    "override_settings": {},
                    "override_settings_restore_afterwards": True,
                    # "refiner_checkpoint": "string",
                    "refiner_switch_at": 0,
                    "disable_extra_networks": False,
                    # "firstpass_image": "string",
                    "comments": {},
                    "enable_hr": True,  # 启用高清修复 True
                    "firstphase_width": self.AISize.text(),  # 高清修复的第一阶段宽度
                    "firstphase_height": self.AISize.text(),  # 高清修复的第一阶段高度
                    "hr_scale": self.AISteps.value(),  # 通常设置为1.25，表示图像放大两倍
                    "hr_upscaler": "Lanczos",  # 高清修复算法
                    "hr_second_pass_steps": self.AIFix.text(),  # 高清修复步数
                    "hr_resize_x": 0,
                    "hr_resize_y": 0,
                    # "hr_checkpoint_name": "string",
                    # "hr_sampler_name": "string",
                    # "hr_scheduler": "string",
                    "hr_prompt": "",
                    "hr_negative_prompt": "",
                    # "force_task_id": "string",
                    "sampler_index": "Euler a",  # 指定采样器名称
                    # "script_name": "string",
                    "script_args": [],
                    "send_images": True,
                    "save_images": False,
                    "alwayson_scripts": {},
                    # "infotext": "string"
                }

                print(nice)
                print(not_nice)
                print(" ")
                print(payload)

                # print("Before append:", self.AIWorkingList)
                # self.AIWorkingList.append([nice, "等待中"])
                # print("After append:", self.AIWorkingList)
                self.updateWorkingList(self.AIWorkingList)

                thread = threading.Thread(
                    target=self.GetAIGenerated, args=(ToURL, payload))
                thread.start()

                thread1 = threading.Thread(
                    target=self.DoInterval)
                thread1.start()

                Flyout.create(
                    icon=InfoBarIcon.INFORMATION,
                    title='开始生成！',
                    content=f"前往生成队列查看生成进度(≧∇≦)ﾉ",
                    target=self.AIStart,
                    parent=self,
                    isClosable=True,
                )

            else:
                Flyout.create(
                    icon=InfoBarIcon.WARNING,
                    title='心急吃不了热豆腐哒',
                    content=f"已经有完全相同的标签在队列中生成了，请改变标签再试噢(≧∇≦)ﾉ",
                    target=self.AIStart,
                    parent=self,
                    isClosable=True,
                )
