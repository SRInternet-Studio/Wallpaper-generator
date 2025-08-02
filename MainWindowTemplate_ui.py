# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindowTemplate.ui'
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
from PySide6.QtWidgets import (QApplication, QSizePolicy, QVBoxLayout, QWidget)

from qfluentwidgets import (OpacityAniStackedWidget, Pivot, SegmentedWidget)
import V4Resources_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1070, 650)
        Form.setStyleSheet(u"border-image: url(:/PNG/PNG/oyama-mahiro-ai~1.png);")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget_3 = QWidget(Form)
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

        self.OpacityAniStackedWidget = OpacityAniStackedWidget(Form)
        self.OpacityAniStackedWidget.setObjectName(u"OpacityAniStackedWidget")
        self.OpacityAniStackedWidget.setStyleSheet(u"border-image: transparent;\n"
"background: transparent;")

        self.verticalLayout.addWidget(self.OpacityAniStackedWidget)


        self.retranslateUi(Form)

        self.OpacityAniStackedWidget.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
    # retranslateUi

