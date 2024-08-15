# -*- coding: utf-8 -*-
from tkinter import messagebox
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import requests
from skimage import io
import matplotlib.pyplot as plt
import pyperclip
import os
import time
import easygui


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(440, 780)
        MainWindow.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("#centralwidget{image: url(BACKIMG.png);}")
        MainWindow.setFixedSize(MainWindow.width(), MainWindow.height())
        MainWindow.setWindowIcon(QtGui.QIcon("ico.ico"))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 50, 301, 51))
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(60, 250, 311, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.PC)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(60, 310, 311, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.Phone)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(60, 370, 311, 51))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.Cat)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(60, 430, 311, 51))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.Starry)
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(60, 490, 311, 61))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.Ran)
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(310, 730, 121, 41))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.clicked.connect(self.about)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "壁纸生成器 2.0 - AI画图"))
        self.label.setText(_translate("MainWindow",
                                      "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">壁纸生成器 - AI 画图</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "在线生成 - 电脑壁纸"))
        self.pushButton_2.setText(_translate("MainWindow", "在线生成 - 手机壁纸"))
        self.pushButton_3.setText(_translate("MainWindow", "在线生成 - 兽控"))
        self.pushButton_4.setText(_translate("MainWindow", "在线生成 - 星空"))
        self.pushButton_5.setText(_translate("MainWindow", "在线生成 - 随机图片\n"
                                                           "（可能包含未审核图片）"))
        self.pushButton_6.setText(_translate("MainWindow", "关于"))

    def PC(self):  # PC壁纸请求
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("MainWindow",
                                      "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">请等待……</span></p></body></html>"))
        start_time = time.time()
        api = "https://dev.iw233.cn/api.php?sort=pc"

        self.ReadPicture(api, start_time)

    def Phone(self):  # 移动端壁纸请求
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("MainWindow",
                                      "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">请等待……</span></p></body></html>"))
        start_time = time.time()
        api = "https://dev.iw233.cn/api.php?sort=mp"

        self.ReadPicture(api, start_time)

    def Cat(self):  # 兽控壁纸请求
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("MainWindow",
                                      "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">请等待……</span></p></body></html>"))
        start_time = time.time()
        api = "https://dev.iw233.cn/api.php?sort=cat"

        self.ReadPicture(api, start_time)

    def Starry(self):  # 星空壁纸请求
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("MainWindow",
                                      "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">请等待……</span></p></body></html>"))
        start_time = time.time()
        api = "https://dev.iw233.cn/api.php?sort=xing"

        self.ReadPicture(api, start_time)

    def Ran(self):  # 随机壁纸请求
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("MainWindow",
                                      "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">请等待……</span></p></body></html>"))
        start_time = time.time()
        api = "https://dev.iw233.cn/api.php?sort=random"

        self.ReadPicture(api, start_time)

    def ReadPicture(self, api, start_time):
        # 选择保存路径
        save = easygui.filesavebox(msg="*.PNG", title="图片保存位置", filetypes=["*.PNG"])
        _translate = QtCore.QCoreApplication.translate
        if save != None:
            save = save + ".png"
            parameters = {
                "type": "json",
                'num': 1
            }
            try:
                try:
                    response = requests.get(api, params=parameters)  # 尝试请求API，获取壁纸
                except:
                    response = "网络错误"
                    raise "网络错误"
                download_url = response.json()["pic"][0]  # 生成图片下载直链
                image = io.imread(download_url)
                io.imsave(save, image)  # 保存图片
                img = plt.imread(save)
                fig = plt.figure('生成的图片(正在在线查看，保存后查看效果更佳)')
                ax = fig.add_subplot(111)
                plt.axis('off')
                pyperclip.copy(download_url)
                os.startfile(save)  # 提供预览
                end_time = time.time()
                spend_time = end_time - start_time
                messagebox.showinfo('生成完毕', '花费了 {} 秒钟，图片已保存。'.format(int(spend_time)))
            except Exception as err:  # 发生错误时发送消息
                messagebox.showwarning("Error " + str(response), str(err))

        self.label.setText(_translate("MainWindow",
                                      "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">壁纸生成器 - AI 画图</span></p></body></html>"))

    def about(self):
        messagebox.showinfo('关于',
                            '名称：壁纸生成器 2.0 AI画图插件\n依赖API：MirlKoiAPI\n        API源：https://dev.iw233.cn/api.php?\n        exe封装：思锐工作室\n\ntips：生成壁纸时出现程序未响应属于正常现象，请耐心等待。\n         若发现点击按钮后的10分钟内程序没有弹出壁纸，请多试几次或隔日再试，这可能是由于服务器维护导致的。')



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
