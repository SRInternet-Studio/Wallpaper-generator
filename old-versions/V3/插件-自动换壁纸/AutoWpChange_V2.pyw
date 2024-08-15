# -*- coding: utf-8 -*-
# coding=utf-8

import sys
import requests
import json
from skimage import io
import tkinter
import matplotlib.pyplot as plt
import os
import win32gui,win32con
from threading import Thread
import easygui
import time
import ctypes #这个库将会用到
import webbrowser as web
import wx.adv
import psutil
from tkinter import messagebox

# 获取程序所在的目录
script_path = sys.executable
script_directory = os.path.dirname(script_path)
app_dir = script_directory
# 修改当前工作目录为程序所在的目录
os.chdir(app_dir)
print(app_dir)

user_setting = []
script_path = sys.argv[0]
script_directory = os.path.dirname(script_path)
root_path = script_directory + os.sep

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
    if is_process_running('自动更换壁纸.exe'):
        pass
    else:
        os.startfile('自动更换壁纸.exe')
    
def notify():
    print("5")
    notification = wx.adv.NotificationMessage(
        title="ACG生成 - 新壁纸",
        message="壁纸刷新成功",
        parent=None,
        flags=wx.ICON_INFORMATION
    )
    # self.icon.notify("壁纸刷新成功", "AI画图 - 新壁纸")
    notification.Show()

def error():
    notification = wx.adv.NotificationMessage(
        title="ACG生成 - 未能刷新壁纸",
        message="壁纸刷新失败，错误报告已生成",
        parent=None,
        flags=wx.ICON_INFORMATION
    )
    notification.Show()
    # global icon
    # self.icon.notify("壁纸刷新失败，请多次重试", "AI画图 - 未能刷新壁纸")

def handrefresh():
    notification = wx.adv.NotificationMessage(
        title="开始",
        message="请等待，壁纸即将刷新",
        parent=None,
        flags=wx.ICON_INFORMATION
    )
    notification.Show()
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

        image = io.imread(output)
        io.imsave(root_path + 'wallpaper.bmp', image)
        img = plt.imread(root_path + 'wallpaper.bmp')
        path = os.path.abspath(root_path + 'wallpaper.bmp')
        win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER,path, win32con.SPIF_SENDWININICHANGE)
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
        self.SetIcon(wx.Icon(root_path + 'ico.ico'), '壁纸生成器 - 托盘程序')
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
        settings()
        

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
        web.open('https://afdian.net/a/srinternet')


if __name__ == '__main__':
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

    app1.MainLoop()
