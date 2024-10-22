# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'progress.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
import sys


class Ui_Dialog(object):
    def __init__(self, progress_num):
        self.progress_num = progress_num
        print("排队 " + str(progress_num) + " 线程")

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(539, 158)
        Dialog.setWindowFlags(Dialog.windowFlags() & ~Qt.WindowContextHelpButtonHint)
        Dialog.setFixedSize(Dialog.width(), Dialog.height());
        Dialog.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)
        Dialog.setModal(True)
        Dialog.setWindowIcon(QtGui.QIcon("bikini60s_cloud-download.ico"))
        self.progressBar = QtWidgets.QProgressBar(Dialog)
        self.progressBar.setGeometry(QtCore.QRect(10, 70, 531, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(11)
        self.progressBar.setFont(font)
        self.progressBar.setMaximum(self.progress_num)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(180, 20, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 120, 511, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "生成进度"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p>正在生成（共 {} 个）</p></body></html>").format(self.progress_num))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p>进度：</p></body></html>"))

    def progress(self, add_num, progress_str):
        _translate = QtCore.QCoreApplication.translate
        #print("完成 " + str(add_num) + "%")
        self.progressBar.setValue(add_num)
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p>进度：{}</p></body></html>").format(progress_str))

    def reject(self):
        pass  # 忽略关闭事件

    def closeEvent(self, event):
        event.ignore()  # 忽略关闭事件
