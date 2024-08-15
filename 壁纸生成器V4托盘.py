# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'V4-NewMinsizeIwdhon.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

import traceback
import winreg
import struct
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QGroupBox, QHBoxLayout, QMainWindow, QMessageBox,
    QSizePolicy, QSpacerItem, QStatusBar, QVBoxLayout,
    QWidget)

from qfluentwidgets import (BodyLabel, CheckBox, PrimaryPushButton, PushButton,
    RadioButton, StrongBodyLabel, TitleLabel)
import my_resources_rc

import sys, os
from PySide6.QtWidgets import QApplication, QMainWindow  

# os.chdir(os.path.dirname(os.path.realpath(sys.argv[0])))

class Ui_MainWindow(QMainWindow):
    def setupUi(self, MainWindow: QMainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
            
        MainWindow.resize(473, 767)
        MainWindow.setMaximumSize(QSize(473, 767))
        MainWindow.setStyleSheet(u"#MainWindow {\n"
" background-image: url(:/bg/CFCAB3C0EB852B1A3E648F454A2527D7.jpg);\n"
"   \n"
"    background-repeat: no-repeat; /* \u7981\u6b62\u5e73\u94fa */\n"
"    background-position: center; /* \u56fe\u7247\u5c45\u4e2d */\n"
"    background-attachment: fixed; /* \u56fe\u7247\u56fa\u5b9a\u4e0d\u6eda\u52a8 */\n"
"    background-size: cover; /* \u62c9\u4f38\u56fe\u7247\u4ee5\u586b\u5145\u6574\u4e2a\u80cc\u666f */\n"
"}\n"
"")
        MainWindow.setWindowIcon(QIcon(".\\Minsize.ico"))

        self.action1 = QAction(MainWindow)
        self.action1.setObjectName(u"action1")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(0, 130))
        self.groupBox.setMaximumSize(QSize(16777215, 130))
        self.groupBox.setStyleSheet(u"QGroupBox {\n"
"    background-color: rgba(255, 255, 255, 175);\n"
"    border: none; /* \u53bb\u6389\u8fb9\u6846 */\n"
"    border-radius: 15px;\n"
"    margin-top: 20px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center;\n"
"    padding: 0 3px;\n"
"    background-color: #2E3440;\n"
"    color: white;\n"
"}\n"
"")
        self.groupBox.setAlignment(Qt.AlignCenter)
        self.verticalLayout_3 = QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalSpacer_4 = QSpacerItem(20, 15, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_3.addItem(self.verticalSpacer_4)

        self.TitleLabel_5 = TitleLabel(self.groupBox)
        self.TitleLabel_5.setObjectName(u"TitleLabel_5")
        self.TitleLabel_5.setStyleSheet(u"QLabel {  \n"
"	font: 24pt \"\u9489\u9489\u8fdb\u6b65\u4f53\";\n"
"    background-color: transparent;  \n"
"}")
        self.TitleLabel_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.TitleLabel_5)

        self.TitleLabel_6 = TitleLabel(self.groupBox)
        self.TitleLabel_6.setObjectName(u"TitleLabel_6")
        self.TitleLabel_6.setStyleSheet(u"QLabel {  \n"
"	font: 24pt \"\u9489\u9489\u8fdb\u6b65\u4f53\";\n"
"    background-color: transparent;  \n"
"}")
        self.TitleLabel_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.TitleLabel_6)


        self.verticalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setStyleSheet(u"QGroupBox {\n"
"    background-color: rgba(255, 255, 255, 175);\n"
"    border: none; /* \u53bb\u6389\u8fb9\u6846 */\n"
"    border-radius: 15px;\n"
"    margin-top: 20px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center;\n"
"    padding: 0 3px;\n"
"    background-color: #2E3440;\n"
"    color: white;\n"
"}\n"
"")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(20, -1, -1, 20)
        self.verticalSpacer_3 = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)

        self.CheckBox_5 = CheckBox(self.groupBox_2)
        self.CheckBox_5.setObjectName(u"CheckBox_5")
        self.CheckBox_5.setStyleSheet(u"CheckBox {\n"
"    color: black;\n"
"    font: 14px 'Segoe UI', 'Microsoft YaHei', 'PingFang SC';\n"
"    background-color: transparent;  \n"
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
"    border: 1px solid #009faa;\n"
"    background-color: #009faa;\n"
"}\n"
"\n"
"\n"
"CheckBox::indicator:checked:hover,\n"
"CheckBox::indicator:indeterminate:hover {\n"
"    border: 1px solid #00a"
                        "7b3;\n"
"    background-color: #00a7b3;\n"
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

        self.verticalLayout_2.addWidget(self.CheckBox_5)

        self.CheckBox_6 = CheckBox(self.groupBox_2)
        self.CheckBox_6.setObjectName(u"CheckBox_6")
        self.CheckBox_6.setStyleSheet(u"CheckBox {\n"
"    color: black;\n"
"    font: 14px 'Segoe UI', 'Microsoft YaHei', 'PingFang SC';\n"
" background-color: transparent;  \n"
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
"    border: 1px solid #009faa;\n"
"    background-color: #009faa;\n"
"}\n"
"\n"
"\n"
"CheckBox::indicator:checked:hover,\n"
"CheckBox::indicator:indeterminate:hover {\n"
"    border: 1px solid #00a7b3"
                        ";\n"
"    background-color: #00a7b3;\n"
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
        
        self.verticalLayout_2.addWidget(self.CheckBox_6)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.BodyLabel_3 = BodyLabel(self.groupBox_2)
        self.BodyLabel_3.setObjectName(u"BodyLabel_3")
        self.BodyLabel_3.setMinimumSize(QSize(0, 20))
        self.BodyLabel_3.setMaximumSize(QSize(16777215, 20))
        self.BodyLabel_3.setStyleSheet(u"QLabel {  \n"
"	font: 700 14pt \"HarmonyOS Sans SC\";\n"
"    background-color: transparent;  \n"
"}")

        self.verticalLayout_2.addWidget(self.BodyLabel_3)

        self.RadioButton_9 = RadioButton(self.groupBox_2)
        self.RadioButton_9.setObjectName(u"RadioButton_9")

        self.verticalLayout_2.addWidget(self.RadioButton_9)

        self.RadioButton_10 = RadioButton(self.groupBox_2)
        self.RadioButton_10.setObjectName(u"RadioButton_10")

        self.verticalLayout_2.addWidget(self.RadioButton_10)

        self.RadioButton_11 = RadioButton(self.groupBox_2)
        self.RadioButton_11.setObjectName(u"RadioButton_11")

        self.verticalLayout_2.addWidget(self.RadioButton_11)

        self.RadioButton_12 = RadioButton(self.groupBox_2)
        self.RadioButton_12.setObjectName(u"RadioButton_12")
        self.RadioButton_12.setStyleSheet(u"PushButton, ToolButton, ToggleButton, ToggleToolButton {\n"
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
"    background-color: #009faa;\n"
"    border: 1px solid #00a7b3;\n"
"    border-bottom: 1px solid #007780;\n"
"}\n"
"\n"
"PrimaryPushButton:hover,\n"
"PrimaryToolButton:hover,\n"
"ToggleButton:checked:hover,\n"
"ToggleToolButton:checked:hover {\n"
"    background-color: #00a7b3"
                        ";\n"
"    border: 1px solid #2daab3;\n"
"    border-bottom: 1px solid #007780;\n"
"}\n"
"\n"
"PrimaryPushButton:pressed,\n"
"PrimaryToolButton:pressed,\n"
"ToggleButton:checked:pressed,\n"
"ToggleToolButton:checked:pressed {\n"
"    color: rgba(255, 255, 255, 0.63);\n"
"    background-color: #3eabb3;\n"
"    border: 1px solid #3eabb3;\n"
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
"    border-bottom: 1px solid #007780;\n"
"}\n"
"\n"
"#primarySplitPushButton, #primarySplitToolButton {\n"
"    border-right: 1px solid #3eabb3;\n"
"}\n"
"\n"
"#primarySplitPushButton:pressed, #primarySplitToolButton:pressed {\n"
"    border-bottom: 1px solid #007780;\n"
"}\n"
"\n"
"HyperlinkButton {\n"
"    /* font: 14px 'Segoe UI', 'Microsoft YaHei'; */\n"
"    padding: 6px 12px 6px 12px;\n"
"    color: #009faa;\n"
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
"    color: #009faa;\n"
"    background-color: rgba(0, 0, 0, 10);\n"
"    border: none;\n"
"}\n"
"\n"
"HyperlinkButton:pressed {\n"
"    color: #009faa;\n"
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
"            stop:0.6 #009faa,\n"
"            stop:1 #009faa);\n"
"}\n"
"\n"
"RadioButton::indicator:checked:hover {\n"
"    background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5,\n"
"            stop:0 rgb(255, 255, 255),\n"
"            stop:0.6 rgb(255, 255, 255),\n"
"            stop:0.7 #009faa,\n"
"            stop:1 #009faa);\n"
"}\n"
"\n"
"RadioButton::indicator:checked:pressed {\n"
"    background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5,\n"
"            stop:0 rgb(255, 255, 255),\n"
"            stop:0.5 rgb(255, 255, 255),\n"
"            stop:0.6 #0"
                        "09faa,\n"
"            stop:1 #009faa);\n"
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

        self.verticalLayout_2.addWidget(self.RadioButton_12)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.StrongBodyLabel_3 = StrongBodyLabel(self.groupBox_2)
        self.StrongBodyLabel_3.setObjectName(u"StrongBodyLabel_3")
        self.StrongBodyLabel_3.setStyleSheet(u"QLabel {  \n"
"    background-color: transparent;  \n"
"font-weight: bold;\n"
"}")
        self.StrongBodyLabel_3.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.verticalLayout_2.addWidget(self.StrongBodyLabel_3)


        self.verticalLayout.addWidget(self.groupBox_2)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.PushButton = PushButton(self.widget)
        self.PushButton.setObjectName(u"PushButton")
        self.PushButton.setMaximumSize(QSize(70, 16777215))
        self.PushButton.clicked.connect(self.About)

        self.horizontalLayout.addWidget(self.PushButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.PushButton_2 = PushButton(self.widget)
        self.PushButton_2.setObjectName(u"PushButton_2")
        self.PushButton_2.clicked.connect(self.ConfirmToClose)

        self.horizontalLayout.addWidget(self.PushButton_2)

        self.PrimaryPushButton = PrimaryPushButton(self.widget)
        self.PrimaryPushButton.setObjectName(u"PrimaryPushButton")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PrimaryPushButton.sizePolicy().hasHeightForWidth())
        self.PrimaryPushButton.setSizePolicy(sizePolicy)
        self.PrimaryPushButton.clicked.connect(self.saveSettings)

        self.horizontalLayout.addWidget(self.PrimaryPushButton)


        self.verticalLayout.addWidget(self.widget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        
        self.r()

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u58c1\u7eb8\u751f\u6210\u5668 - \u6258\u76d8\u7a0b\u5e8f\u8bbe\u7f6e", None))
        self.action1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.groupBox.setTitle("")
        self.TitleLabel_5.setText(QCoreApplication.translate("MainWindow", u"\u58c1\u7eb8\u751f\u6210\u5668 ", None))
        self.TitleLabel_6.setText(QCoreApplication.translate("MainWindow", u"\u81ea\u52a8\u58c1\u7eb8 \u2014 \u6258\u76d8\u7a0b\u5e8f\u8bbe\u7f6e", None))
        self.groupBox_2.setTitle("")
        self.CheckBox_5.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u673a\u81ea\u542f\u52a8", None))
        self.CheckBox_6.setText(QCoreApplication.translate("MainWindow", u"\u7a0b\u5e8f\u81ea\u52a8\u540e\u66f4\u6362\u58c1\u7eb8", None))
        self.BodyLabel_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">\u5237\u65b0\u7684\u58c1\u7eb8\u7c7b\u578b</span></p></body></html>", None))
        self.RadioButton_9.setText(QCoreApplication.translate("MainWindow", u"\u7535\u8111\u58c1\u7eb8", None))
        self.RadioButton_10.setText(QCoreApplication.translate("MainWindow", u"\u661f\u7a7a\u58c1\u7eb8 (\u53ef\u80fd\u5305\u542b\u4e0d\u5408\u9002\u7684\u5c3a\u5bf8)", None))
        self.RadioButton_11.setText(QCoreApplication.translate("MainWindow", u"\u968f\u673a\u58c1\u7eb8 (\u53ef\u80fd\u5305\u542b\u4e0d\u5408\u9002\u7684\u5c3a\u5bf8)", None))
        self.RadioButton_12.setText(QCoreApplication.translate("MainWindow", u"AI\u63a8\u8350 (\u53ef\u80fd\u5305\u542b\u4e0d\u5408\u9002\u7684\u5c3a\u5bf8)", None))
        self.StrongBodyLabel_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">\u66f4\u591a\u529f\u80fd\u656c\u8bf7\u671f\u5f85...</span></p></body></html>", None))
        self.PushButton.setText(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e", None))
        self.PushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u4e0d\u4fdd\u5b58\u5173\u95ed", None))
        self.PrimaryPushButton.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58\u5e76\u5173\u95ed", None))
        
        
    # retranslateUi

    def saveSettings(self):
        configs: str = ""
        autochange = self.CheckBox_6
        PC_Button = self.RadioButton_9
        Starry = self.RadioButton_10
        Top = self.RadioButton_12
        Ran = self.RadioButton_11

        if os.path.exists(".\\limit.ini") == True and (self.RadioButton_9.isChecked == True or self.RadioButton_11.isChecked == True or self.RadioButton_12.isChecked == True):
            msg_box = QMessageBox()
            msg_box.setWindowTitle("R18 限制")
            msg_box.setText(
                "您所选择的选项包含可能会生成包含限制级的壁纸，管理员已禁止 壁纸生成器 自动生成此类壁纸，请您取消勾选【电脑壁纸】、【随机壁纸】或【AI 推荐】选项。")
            msg_box.setIcon(QMessageBox.Icon.Warning)
            msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg_box.show()
            msg_box.exec()
        elif os.path.exists(".\\Wallpaper_Generator.exe") == False:
            print(os.path.abspath(".\\Wallpaper_Generator.exe"))
            msg_box = QMessageBox()
            msg_box.setWindowTitle("找不到入口程序")
            msg_box.setText(
                "壁纸生成器 很可能已经损坏，因为丢失重要文件 Wallpaper_Generator.exe 。请尝试重新安装本程序以解决此问题。")
            msg_box.setIcon(QMessageBox.Icon.Warning)
            msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg_box.show()
            msg_box.exec()
        else:
            
            if self.CheckBox_5.isChecked():
                print("self.CheckBox_5 chkecked")
                if not self.IsAddedToStartup():
                    IsAddCompletly = self.AddToStartup()
                    if IsAddCompletly == "True" and self.IsAddedToStartup():
                        print("allowed autostart")
                        configs += "AutoStart\n"
                    else:
                        self.CheckBox_5.setChecked(False)
                        msg_box = QMessageBox()
                        msg_box.setWindowTitle("无法添加到启动项")
                        msg_box.setText(
                            "请检查权限是否给予。若已给予管理员权限，请截图并反馈以下错误：\n\n" + IsAddCompletly)
                        msg_box.setIcon(QMessageBox.Icon.Critical)
                        msg_box.setStandardButtons(
                            QMessageBox.StandardButton.Ok)
                        msg_box.show()
                        msg_box.exec()
                else:
                    print("allowed autostart")
                    configs += "AutoStart\n"
            else:
                 print("self.CheckBox_5 not chkecked")
                 if self.IsAddedToStartup():
                      IsDelCompletly = self.RemoveFromStartup()
                      if IsDelCompletly == "True" and not self.IsAddedToStartup():
                           pass
                      else:
                        print("allowed autostart")
                        configs += "AutoStart\n"
                        self.CheckBox_5.setChecked(True)
                        msg_box = QMessageBox()
                        msg_box.setWindowTitle("无法删除启动项")
                        msg_box.setText('''请检查权限是否给予。若已给予管理员权限，您可以尝试以下方法：
    1. 使用 Win+R 快捷键，输入并打开 Regedit （注册表编辑器）
    2. 打开 HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Run 文件夹路径
    3. 删除，并确认删除名为 WallpaperGenerator 的文件，即可删除启动项。
    4. 请截图并反馈以下错误：\n\n''' + IsAddCompletly)
                        msg_box.setIcon(QMessageBox.Icon.Critical)
                        msg_box.setStandardButtons(
                            QMessageBox.StandardButton.Ok)
                        msg_box.show()
                        msg_box.exec()

            if autochange.isChecked():
                 configs += "AutoChange\n"

            if PC_Button.isChecked():
                configs += "PC"
            elif Starry.isChecked():
                configs += "Starry"
            elif Top.isChecked():
                configs += "Top"
            elif Ran.isChecked():
                configs += "Ran"
            else:
                configs += "Starry"

            print(configs)
            with open(".\\RefreshSetting.Sr", "w") as c:
                c.write(configs)
                c.close()

            msg_box = QMessageBox()
            msg_box.setWindowTitle("已成功保存配置")
            msg_box.setText(
                "成功保存所有配置到本地。更改将会立即生效ヾ(≧▽≦*)o")
            msg_box.setIcon(QMessageBox.Icon.Information)
            msg_box.setStandardButtons(
                QMessageBox.StandardButton.Ok)
            msg_box.show()
            msg_box.exec()
            self.close()

            
    def AddToStartup(self) -> str:
        try:
            exe_path = os.path.abspath(".\\Wallpaper_Generator.exe")
            startup_command = f'"{exe_path}" --AutoStartup'

            is_64bits = struct.calcsize("P") * 8 == 64

            if is_64bits:
                key_path = r"SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Run"
            else:
                key_path = r"Software\Microsoft\Windows\CurrentVersion\Run"

            print(startup_command)
                # 打开注册表，路径为 HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Run
            with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path, 0, winreg.KEY_SET_VALUE) as reg_key:
                        # 将WallpaperGenerator.exe添加到注册表
                winreg.SetValueEx(reg_key, "WallpaperGenerator", 0, winreg.REG_SZ, startup_command)
            return "True"
        except:
            return traceback.format_exc()

    def RemoveFromStartup(self) -> str:
        try:
              is_64bits = struct.calcsize("P") * 8 == 64

              if is_64bits:
                 key_path = r"SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Run"
              else:
                 key_path = r"Software\Microsoft\Windows\CurrentVersion\Run"

              with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path, 0, winreg.KEY_SET_VALUE) as reg_key:
                # 删除 WallpaperGenerator 启动项
                winreg.DeleteValue(reg_key, "WallpaperGenerator")
              return "True"
        except:
              return traceback.format_exc()

    def IsAddedToStartup(self) -> bool: 
        exe_path = os.path.abspath(".\\Wallpaper_Generator.exe")
        startup_command = f'"{exe_path}" --AutoStartup'
        print(startup_command)

        is_64bits = struct.calcsize("P") * 8 == 64

        if is_64bits:
            key_path = r"SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Run"
        else:
            key_path = r"Software\Microsoft\Windows\CurrentVersion\Run"

        value_name = "WallpaperGenerator"

        try:
                # 打开注册表项
                with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path) as reg_key:
                # 获取指定值
                        value, regtype = winreg.QueryValueEx(reg_key, value_name)
                        script_path = os.path.abspath(sys.argv[0])
                        expected_value = startup_command
                        
                # 检查值是否匹配
                return value is not None and value == expected_value
        except FileNotFoundError:
                return False
        except Exception as e:
                return False
        
    def About(self):
        string = '''壁纸生成器 V4 托盘程序
插件版本：AutoWpChange_V4
使用API：MirlKoi API
版权：思锐工作室'''
        msg_box = QMessageBox()
        msg_box.setWindowTitle("关于本程序")
        msg_box.setWindowIcon(QIcon(".\\NewIcon.ico"))
        msg_box.setText(string)
        msg_box.setIcon(QMessageBox.Icon.Information)
        msg_box.setStandardButtons(
            QMessageBox.StandardButton.Ok)
        msg_box.show()
        msg_box.exec()

    def ConfirmToClose(self):
        msg_box = QMessageBox()
        msg_box.setWindowTitle("确认不保存配置？")
        msg_box.setWindowIcon(QIcon(".\\NewIcon.ico"))
        msg_box.setText("如果您的配置已经进行了更改，那么在您点 “Yes” 后这些设置将不会生效。若要更新您的设置，请点击 “No” ，并点击“保存并关闭”。")
        msg_box.setIcon(QMessageBox.Icon.Information)
        msg_box.setStandardButtons(
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        msg_box.show()
        
        if msg_box.exec() == QMessageBox.StandardButton.Yes:
            self.close()
            pass
        
    def r(self):
         if os.path.exists(".\\RefreshSetting.Sr"):
            print("reads")
            with open(".\\RefreshSetting.Sr", "r") as file:
                user_setting = file.read()

            #user_setting = user_setting.split("\n")
            # s = ""
            # for u in user_setting:
            #     s += u
            # user_setting = s

            print(user_setting)
            
            if "AutoStart" in user_setting:
                print(-1)
                self.CheckBox_5.setChecked(True)

            if "AutoChange" in user_setting:
                print(-2)
                self.CheckBox_6.setChecked(True)

            if "PC" in user_setting:
                print(1)
                self.RadioButton_9.setChecked(True)
            elif "Starry" in user_setting:
                print(2)
                self.RadioButton_10.setChecked(True)
            elif "Top" in user_setting:
                print(3)
                self.RadioButton_12.setChecked(True)
            else:
                print(4)
                self.RadioButton_11.setChecked(True)
  
if __name__ == "__main__":  
    app = QApplication(sys.argv)  
    window = Ui_MainWindow()  
    window.setupUi(window)
    window.show()
    sys.exit(app.exec())
