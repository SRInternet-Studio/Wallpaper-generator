import sys
import requests
import json
from skimage import io
from tkinter import *
import matplotlib.pyplot as plt
import os
import win32gui,win32con
import pystray
from PIL import Image
from pystray import MenuItem
from threading import Thread

def notify(icon):
    icon.notify("壁纸刷新成功", "AI画图 - 新壁纸")

def error(icon):
    icon.notify("壁纸刷新失败，请多次重试", "AI画图 - 未能刷新壁纸")

def handrefresh():
    global icon
    icon.notify("请等待，壁纸即将刷新", "开始")
    refresh()


def refresh():
    global icon
    
    api = "https://dev.iw233.cn/api.php?sort=xing"
    parameters = {
        "type": "json",
        'num': 1
    }
    response = requests.get(api, params=parameters)
    try:
        # print(response.text())
        outputurl = json.dumps(response.json())
        print(outputurl)
        output = outputurl[10:-3]

        image = io.imread(output)
        io.imsave('wallpaper.png', image)
        img = plt.imread('wallpaper.png')
        path = os.path.abspath('.\\wallpaper.png')
        win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER,path, win32con.SPIF_SENDWININICHANGE)
        print(path)
        notify(icon)
    except:
        error(icon)


def end():
    sys.exit(0)

thr = Thread(target=refresh)
thr.start()
menu = (MenuItem('生成并刷新壁纸',action=handrefresh), MenuItem('退出', action=end))
image = Image.open("ico.ico")
icon = pystray.Icon("minmenu", image, "AI画图 - 每日自动刷新壁纸", menu)
icon.run()
