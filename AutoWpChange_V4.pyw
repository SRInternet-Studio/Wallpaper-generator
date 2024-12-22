# -*- coding: utf-8 -*-
# coding=utf-8

import sys
from PySide6.QtWidgets import QApplication, QDialog, QMainWindow, QMessageBox
import requests
import json
import tkinter
import matplotlib.pyplot as plt
import os
from threading import Thread
import easygui
import time
import ctypes #这个库将会用到
import webbrowser as web
import wx.adv
import psutil
from tkinter import messagebox
from V4TrayIcon import Ui_MainWindow 

# 获取程序所在的目录
# script_path = sys.executable
# script_directory = os.path.dirname(script_path)
app_dir = os.path.dirname(os.path.realpath(sys.argv[0]))
# 修改当前工作目录为程序所在的目录
os.chdir(app_dir)
print(app_dir)

user_setting = []
script_path = sys.argv[0]
script_directory = os.path.dirname(script_path)
root_path = script_directory + os.sep


    # def closeEvent(self, event):
    #     # 忽略关闭事件
    #     event.ignore()
    #     msg_box = QMessageBox()
    #     msg_box.setWindowTitle("确认您的配置")
    #     msg_box.setText(
    #         "在配置好自动更换壁纸的设置后，请点击窗口下方的 “不保存关闭” 或 “保存并关闭” 按钮以关闭设置界面。")
    #     msg_box.setIcon(QMessageBox.Icon.Warning)
    #     msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
    #     msg_box.show()
    #     msg_box.exec()

def ifAdmin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
    
def is_process_running(process_name):
    for proc in psutil.process_iter(['name']):
        if proc.info['name'] == process_name:
            return True
    return False

root = tkinter.Tk()
root.withdraw()

def settings():
        
        window = Ui_MainWindow()  
        window.setupUi(window)
        window.show()
        app.exec()

    # if is_process_running('自动更换壁纸.exe'):
    #     pass
    # else:
    #     os.startfile('自动更换壁纸.exe')
    
def notify():
    print("5")
    
    # self.icon.notify("壁纸刷新成功", "AI画图 - 新壁纸")
    notification2.Close()
    notification3.Close()
    notification1.Show()

def error():
    
    notification1.Close()
    notification3.Close()
    notification2.Show()
    # global icon
    # self.icon.notify("壁纸刷新失败，请多次重试", "AI画图 - 未能刷新壁纸")

def handrefresh():

    notification1.Close()
    notification2.Close()
    notification3.Show()
    #notification.Close
    # global icon
    # self.icon.notify("请等待，壁纸即将刷新", "开始")

    refresh()


def end():
    os._exit(0)

#def tray_process_func():
def refresh():
    print('3')
    global user_setting

    with open(root_path + "RefreshSetting.Sr", "r") as file:
            user_setting = file.read()
            
    if 'PC' in user_setting:
        api = "https://api.iw233.cn/api.php?sort=pc"
    elif 'Starry' in user_setting:
        api = "https://api.iw233.cn/api.php?sort=xing"
    elif 'Top' in user_setting:
        api = "https://api.iw233.cn/api.php?sort=top"
    else:
        api = "https://api.iw233.cn/api.php?sort=random"

    print(api)

    parameters = {
        "type": "json",
        'num': 1
    }
    try:
        print('4')
        response = requests.get(api, params=parameters)
        # print(response.text())
        outputurl = json.dumps(response.json())
        print(outputurl)
        output = outputurl[10:-3]

        image = requests.get(output)

        with open(root_path + 'wallpaper.bmp', 'wb') as f:
                f.write(image.content)  # 保存图片

        img = plt.imread(root_path + 'wallpaper.bmp')
        path = os.path.abspath(root_path + 'wallpaper.bmp')
        # win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER,path, win32con.SPIF_SENDWININICHANGE)
        ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 3)
        print(path)
        notify()
    except:
        print('5')
        time.sleep(1)
        error()
        easygui.exceptionbox()

class MyTaskBarIcon(wx.adv.TaskBarIcon):
    def __init__(self):
        super().__init__()
        self.SetIcon(wx.Icon(root_path + 'NewIcon.ico'), '壁纸生成器 - 托盘程序')
        self.Bind(wx.adv.EVT_TASKBAR_LEFT_DCLICK, self.on_left_click)
        # self.tray_app = icon_set(MainWindow, ui, open_window)

    def CreatePopupMenu(self):
        # 创建弹出菜单
        menu = wx.Menu()
        menu.Append(1, '立刻生成并刷新壁纸')
        menu.Append(2, '打开生成设置')
        menu.AppendSeparator()
        menu.Append(3, '退出(若设定了开机启动，下次开机仍会启动)')
        menu.AppendSeparator()
        menu.Append(4, '捐赠几行代码，助力我们高效开发')
        self.Bind(wx.EVT_MENU, self.on_menu_1_select, id=1)
        self.Bind(wx.EVT_MENU, self.on_menu_2_select, id=2)
        self.Bind(wx.EVT_MENU, self.on_menu_3_select, id=3)
        self.Bind(wx.EVT_MENU, self.juanzeng, id=4)
        return menu

    def on_left_click(self, event):
        handrefresh()
        

    def on_menu_1_select(self, event):
        if os.path.isfile(root_path + "RefreshSetting.Sr") == False:
            settings()
            messagebox.showinfo("提示", "你还没有刷新壁纸的配置，请进行配置")
        else:
            handrefresh()
        

    def on_menu_2_select(self, event):
        settings()

    def on_menu_3_select(self, event):
        end()

    def juanzeng(self, event):
        web.open('https://afdian.com/a/srinternet')


if __name__ == '__main__':

    if ifAdmin():
        app = QApplication(sys.argv)
        thr = Thread(target=refresh)
        
        if os.path.isfile(root_path + "RefreshSetting.Sr") == False:
            settings()
        else:
            with open(root_path + "RefreshSetting.Sr", "r") as file:
                user_setting = file.read()
            print('1')
            print(user_setting)
            if 'AutoChange' in user_setting:
                thr.start()
                print('2')

        app1 = wx.App(False)

        # 创建任务栏图标对象
        task_bar_icon = MyTaskBarIcon()

        notification1 = wx.adv.NotificationMessage(
            title="ACG生成 - 新壁纸",
            message="壁纸刷新成功",
            parent=None,
            flags=wx.ICON_INFORMATION
        )
        notification2 = wx.adv.NotificationMessage(
            title="ACG生成 - 未能刷新壁纸",
            message="壁纸刷新失败，错误报告已生成",
            parent=None,
            flags=wx.ICON_WARNING
        )
        notification3 = wx.adv.NotificationMessage(
            title="开始",
            message="请等待，壁纸即将刷新",
            parent=None,
            flags=wx.ICON_INFORMATION
        )

        app1.MainLoop()

    else:
        messagebox.showinfo("提示", "请以管理员身份运行本程序，否则可能会出现错误。")
