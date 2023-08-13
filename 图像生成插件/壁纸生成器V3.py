# -*- coding: utf-8 -*-


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap, QPalette, QColor
import sys
import requests
import json
import tkinter
from skimage import io
from tkinter import *
from tkinter import messagebox
import matplotlib.pyplot as plt
import pyperclip
import os
import time
import asyncio
import easygui
import threading
import queue
import random

root = Tk()
root.withdraw()

download_queue = queue.Queue()

class Ui_MainWindow(object):
    def  __init__(self):
        self.completed_threads = 0
        

    def setupUi(self, MainWindow):

        root_directory = "./Wallpapers"
        file_list = []

        for root, dirs, files in os.walk(root_directory):
            for file in files:
                file_path = os.path.join(root, file)
                file_list.append(file_path)
        print("读取壁纸:", file_list)

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(440, 780)
        MainWindow.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        MainWindow.setAutoFillBackground(False)
        random_image_path = random.choice(file_list)
        random_image_path = random.choice(file_list)
        random_image_path = random.choice(file_list)
        random_image_path = random.choice(file_list)
        random_image_path = random.choice(file_list)
        print("设置壁纸:", random_image_path)
        #stylesheet = f"#centralwidget {{ image: url({random_image_path}); }}"
        #normalized_path = os.path.normpath(random_image_path)
        #stylesheet = "#centralwidget {{ background-image: url({}); }}".format(normalized_path.replace('\\', '/'))
        # 获取窗口的宽度和高度

        # stylesheet = "#centralwidget {{ \
        #         background-image: url({}); \
        #         background-position: center; \
        #         background-size: contain; \
        #         background-repeat: no-repeat; \
        #       }}".format(normalized_path.replace('\\', '/'))
        # MainWindow.setStyleSheet(stylesheet)

        # 创建一个 QPixmap 对象来加载图片
        pixmap = QPixmap(random_image_path)

        # 获取窗口的高度
        window_height = MainWindow.height()

        # 计算调整后的高度和宽度
        scaled_height = window_height
        scaled_width = int(pixmap.width() * (scaled_height / pixmap.height()))

        # 缩放图片
        pixmap = pixmap.scaled(scaled_width, scaled_height, aspectRatioMode=QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)

        # 创建一个 QPalette 对象，并设置背景图片
        palette = QPalette()
        palette.setBrush(QPalette.Background, QtGui.QBrush(pixmap))

        # 设置主窗口的调色板
        MainWindow.setPalette(palette)

        #MainWindow.setStyleSheet("#centralwidget{image: url(BACKIMG.png);}")
        # MainWindow.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)
        MainWindow.setFixedSize(MainWindow.width(), MainWindow.height());
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
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(270, 580, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.checkBox.setFont(font)
        self.checkBox.setText("")
        self.checkBox.setTristate(False)
        self.checkBox.setObjectName("checkBox")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(290, 580, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.label_2.raise_()
        self.checkBox.raise_()
        self.checkBox.stateChanged.connect(self.checked)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def checked(self):
        pass

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "壁纸生成器 3.0 - 图像生成"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">壁纸生成器 - 图像生成</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "在线生成 - 电脑壁纸"))
        self.pushButton_2.setText(_translate("MainWindow", "在线生成 - 手机壁纸"))
        self.pushButton_3.setText(_translate("MainWindow", "在线生成 - 兽控"))
        self.pushButton_4.setText(_translate("MainWindow", "在线生成 - 星空"))
        self.pushButton_5.setText(_translate("MainWindow", "在线生成 - 随机图片\n"
"（可能包含未过审图片！）"))
        self.pushButton_6.setText(_translate("MainWindow", "关于"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt; color:#FC0303;\">批量生成（新）</span></p></body></html>"))

    def closeEvent(self, event):
        sys.exit(0)

    def PC(self):
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">请等待……</span></p></body></html>"))
        api = "https://api.iw233.cn/api.php?sort=pc"

        g_type = '电脑壁纸'

        self.ReadPicture(api, g_type)

    def Phone(self):
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">请等待……</span></p></body></html>"))
        api = "https://api.iw233.cn/api.php?sort=mp"

        g_type = '手机壁纸'

        self.ReadPicture(api, g_type)
        
    def Cat(self):
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">请等待……</span></p></body></html>"))
        api = "https://api.iw233.cn/api.php?sort=cat"

        g_type = '兽控壁纸'

        self.ReadPicture(api, g_type)

    def Starry(self):
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">请等待……</span></p></body></html>"))
        api = "https://api.iw233.cn/api.php?sort=xing"

        g_type = '星空壁纸'

        self.ReadPicture(api, g_type)

    def Ran(self):
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">请等待……</span></p></body></html>"))
        api = "https://api.iw233.cn/api.php?sort=random"

        g_type = '随机壁纸'

        self.ReadPicture(api, g_type)

    def download_image(self, url, save, i):
        print('Thread {} started'.format(i))
        image = io.imread(url)
        io.imsave(save, image)
        print(save + " 结束")
        
        self.completed_threads += 1
        download_queue.put(save)
        

    def ReadPicture(self,api,g_type):
        self.completed_threads = 0
        self.pushButton.setEnabled(False)
        self.pushButton_2.setEnabled(False)
        self.pushButton_3.setEnabled(False)
        self.pushButton_4.setEnabled(False)
        self.pushButton_5.setEnabled(False)
        self.pushButton_6.setEnabled(False)
        self.checkBox.setEnabled(False)
        
                #选择保存路径
        self.number = 1
        self.choosed = False

        if self.checkBox.isChecked() == True:
            import batch_window
            BatchWindow = QtWidgets.QDialog()
            ui1 = batch_window.Ui_Dialog(g_type)
            ui1.setupUi(BatchWindow)
            result = BatchWindow.exec_()
            
            if result == QtWidgets.QDialog.Accepted:
                self.number = batch_window.number
                self.choosed = True

        save = None
        if (self.checkBox.isChecked() == True and self.choosed == True) or self.checkBox.isChecked() == False:
            save = easygui.filesavebox(msg="*.PNG",title="图片保存位置",filetypes=["*.PNG"])
            start_time = time.time()

        _translate = QtCore.QCoreApplication.translate
        if save != None:
            parameters = {
                "type": "json",
                'num': self.number
            }
            response = requests.get(api, params=parameters)
            # try:
                # print(response.text())
            
            outputurl = response.json()
            print('拉取 ' + str(outputurl))
            output = outputurl["pic"]
            if int(self.number) == 1:
                print('开始下载……')
                save = save + ".png"
                image = io.imread(output[0])
                io.imsave(save, image)
                img = plt.imread(save)
                fig = plt.figure('生成的图片(正在在线查看，保存后查看效果更佳)')
                ax = fig.add_subplot(111)
                plt.axis('off')
                pyperclip.copy(output[0])
                os.startfile(save)
                end_time = time.time()
                spend_time = end_time - start_time
                print('结束\n')
                messagebox.showinfo('生成完毕','花费了 {} 秒钟，图片已保存。'.format(spend_time))
            else:
                print('开始下载……')
                file_name = save
                import progress
                ProgressWindow = QtWidgets.QDialog()
                ui2 = progress.Ui_Dialog(len(output))
                ui2.setupUi(ProgressWindow)
                ProgressWindow.show()
                # for i in range(len(output)):
                #     url = output[i]
                #     image = io.imread(url)
                #     if i != 0:
                #         save =  file_name + ' (' + str(i) + ").png"
                #     else:
                #         save =  file_name + ".png"
                #     save = os.path.abspath(save)
                #     io.imsave(save, image)
                #     print(save + " 结束")
                #     ui2.progress(i+1)
                download_threads = []
                
                times = 0
                for i in range(len(output)):
                    times += 1
                    url = output[i]
                    if i != 0:
                        save =  file_name + ' (' + str(i) + ").png"
                    else:
                        save =  file_name + ".png"
                    save_1 = os.path.abspath(save)

                    # 创建并启动一个新的下载线程
                    thread = threading.Thread(target=self.download_image, args=(url, save_1, i))
                    thread.start()

                    # 将下载线程添加到列表中
                    download_threads.append(thread)

                    # completed_threads = 0
                    # while completed_threads < len(output):
                        # 检查是否有线程下载完成
                    # if not download_queue.empty():
                        # completed_threads += 1
                        

                    # 继续处理 UI 事件
                    

                    # 更新进度条
                    
                    # while completed_threads < len(output):
                    #     print(download_queue)
                    #     print(completed_threads)
                    #     # 检查是否有线程下载完成
                    #     if not download_queue.empty():
                    #         completed_threads += 1
                    #         ui2.progress(completed_threads)
                            
                    while self.completed_threads < len(output):
                        if not download_queue.empty():
                            ui2.progress(self.completed_threads, os.path.basename(download_queue.get()) + " 完成")
                            download_queue.queue.clear()
                        # 继续处理 UI 事件
                            
                            break

                        QtCore.QCoreApplication.processEvents()

                    # v3.1更新多线程下载，把while下的所有代码向左缩进一次并把break删掉即可实现
                    

                # 等待所有下载线程完成
                for thread in download_threads:
                    thread.join()

                ProgressWindow.hide()
                end_time = time.time()
                spend_time = end_time - start_time
                print('全部结束\n')
                os.startfile(os.path.dirname(save))
                messagebox.showinfo('生成完毕','一共花费了 {} 秒钟，图片均已保存。'.format(spend_time))
            # except:
            #     messagebox.showwarning("Error",response)


        self.pushButton.setEnabled(True)
        self.pushButton_2.setEnabled(True)
        self.pushButton_3.setEnabled(True)
        self.pushButton_4.setEnabled(True)
        self.pushButton_5.setEnabled(True)
        self.pushButton_6.setEnabled(True)
        self.checkBox.setEnabled(True)
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">壁纸生成器 - 图像生成</span></p></body></html>"))
    
    def about(self):
        messagebox.showinfo('关于','名称：壁纸生成器 3.0 图片生成插件\n依赖API：MirlKoiAPI\n        API源：https://api.iw233.cn/api.php?\n        本地化：思锐工作室\n\ntips：生成壁纸时出现程序未响应属于正常现象，请耐心等待。\n         若发现点击按钮后的10分钟内程序没有弹出壁纸，请多试几次或隔日再试，这可能是由于服务器维护导致的。')


# import 2.0资源_rc
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
