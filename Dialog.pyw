# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Dialog.ui'
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
    QPalette, QPixmap, QRadialGradient, QTransform, QTextOption)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QSizePolicy, QTableWidgetItem, QVBoxLayout,
    QWidget, QDialog)

from qfluentwidgets import (BodyLabel, CardWidget, PrimaryPushButton, PushButton,
    SimpleCardWidget, TitleLabel, TextEdit, TableWidget)

class Ui_Form(QDialog):
    def __init__(self, title, content, TrueText, FalseText, Editable, Lists=None):
        super().__init__()
        #super().__init__()
        self.title = f"{title}"
        self.content = f"{content}"
        self.TrueText = f"{TrueText}"
        self.FalseText = f"{FalseText}"
        self.Editable = f"{Editable}"
        self.Lists = f"{Lists}"
        self.returned = "F"


    def setupUi(self, Form: QDialog):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.setFixedSize(908, 448)
        Form.setStyleSheet(u"QWidget {\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"}")
        Form.setWindowFlags(Qt.WindowTitleHint)
        Form.setWindowIcon(QIcon("./None.ico"))

        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.SimpleCardWidget = SimpleCardWidget(Form)
        self.SimpleCardWidget.setObjectName(u"SimpleCardWidget")
        self.horizontalLayout_2 = QHBoxLayout(self.SimpleCardWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.widget_2 = QWidget(self.SimpleCardWidget)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_2 = QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.TitleLabel = TitleLabel(self.widget_2)
        self.TitleLabel.setObjectName(u"TitleLabel")
        self.TitleLabel.setMaximumSize(QSize(16777215, 50))
        font = QFont()
        font.setFamilies([u"HarmonyOS Sans SC"])
        font.setPointSize(21)
        font.setBold(True)
        self.TitleLabel.setFont(font)

        self.verticalLayout_2.addWidget(self.TitleLabel)

        if self.Editable == "True":
            self.BodyLabel = TextEdit(self.widget_2)
        else:
            self.BodyLabel = BodyLabel(self.widget_2)

        self.BodyLabel.setObjectName(u"BodyLabel")
        self.BodyLabel.setAutoFillBackground(False)
        self.BodyLabel.setAlignment(Qt.AlignJustify|Qt.AlignTop)

        if self.Editable == "True":
            self.BodyLabel.setWordWrapMode(QTextOption.WrapMode.WordWrap)
            self.BodyLabel.setReadOnly(True)
        else:
            self.BodyLabel.setWordWrap(True)

        # self.tableView = TableWidget(self)
        # self.tableView.setBorderVisible(True)
        # self.tableView.setBorderRadius(8)

        # self.tableView.setWordWrap(False)
        # self.tableView.setRowCount(60)
        # self.tableView.setColumnCount(2)

        # self.Lists += self.Lists
        # for i, songInfo in enumerate(self.Lists):
        #     for j in range(2):
        #         self.tableView.setItem(i, j, QTableWidgetItem(songInfo[j]))

        # self.tableView.verticalHeader().hide()
        # self.tableView.setHorizontalHeaderLabels(['名称', '信息'])
        # self.tableView.resizeColumnsToContents()
        # 下个版本启用

        self.verticalLayout_2.addWidget(self.BodyLabel)


        self.horizontalLayout_2.addWidget(self.widget_2)


        self.verticalLayout.addWidget(self.SimpleCardWidget)

        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.PrimaryPushButton = PrimaryPushButton(self.widget)
        self.PrimaryPushButton.setObjectName(u"PrimaryPushButton")
        self.PrimaryPushButton.clicked.connect(lambda k: self.AClose(Form))

        self.horizontalLayout.addWidget(self.PrimaryPushButton)

        self.PushButton = PushButton(self.widget)
        self.PushButton.setObjectName(u"PushButton")
        self.PushButton.clicked.connect(lambda k: self.NClose(Form))

        self.horizontalLayout.addWidget(self.PushButton)


        self.verticalLayout.addWidget(self.widget)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", self.title, None))
        self.TitleLabel.setText(QCoreApplication.translate("Form", self.title, None))
        self.BodyLabel.setText(QCoreApplication.translate("Form", self.content, None))
        self.PrimaryPushButton.setText(QCoreApplication.translate("Form", self.TrueText, None))
        self.PushButton.setText(QCoreApplication.translate("Form", self.FalseText, None))

    def AClose(self, Form):
        self.returned = "T"
        Form.close()

    def NClose(self, Form):
        Form.close()

    def IsTF(self):
        return self.returned
    # retranslateUi

