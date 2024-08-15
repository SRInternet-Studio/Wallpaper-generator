# from PyQt5 import QtCore, QtGui, QtWidgets
# from PyQt5.QtCore import Qt
# import progress, sys, time
# app = QtWidgets.QApplication(sys.argv)
# ProgressWindow = QtWidgets.QDialog()
# ui2 = progress.Ui_Dialog(10)
# ui2.setupUi(ProgressWindow)
# ProgressWindow.show()

# def update_progress_bar():
#     for i in range(10):
#         ui2.progress(i + 1)
#         ProgressWindow.update()
#         time.sleep(0.5)

# # 创建计时器
# timer = QtCore.QTimer()
# timer.timeout.connect(update_progress_bar)
# timer.start(500)

# app.exec_()

import os

root_directory = "./Wallpapers"
file_list = []

for root, dirs, files in os.walk(root_directory):
    for file in files:
        file_path = os.path.join(root, file)
        file_list.append(file_path)

print("文件列表:", file_list)