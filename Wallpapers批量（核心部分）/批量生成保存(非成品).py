from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import requests
import json
from skimage import io
from tkinter import *
from tkinter import messagebox
import matplotlib.pyplot as plt
import pyperclip
import os
import time
import easygui

frequency = 3

def main(api, parameters, frequency):
    response = requests.get(api, params=parameters)
    # print(response.text())
    outputurl = response.json()
    print(outputurl,'\n')
    print(type(outputurl),'\n')
    res = outputurl["pic"]
    for i in range(len(res)):
        output = res[i]
        image = io.imread(output)
        save =  str(i) + "-6.17生成" + str(frequency) + ".png"
        save = os.path.abspath(save)
        print(save)
        io.imsave(save, image)
    # img = plt.imread(save)
    # fig = plt.figure('生成的图片(正在在线查看，保存后查看效果更佳)')
    # ax = fig.add_subplot(111)
    # plt.axis('off')
    # pyperclip.copy(output)

api = "https://iw233.cn/api.php?sort=cat" #pc20, random30, cat20, mp50, top50
parameters = {
    "type": "json",
    'num': 20
}
main(api, parameters, frequency)
frequency += 1


api = "https://iw233.cn/api.php?sort=mp" #pc20, random30, cat20, mp50, top50
parameters = {
    "type": "json",
    'num': 50
}
main(api, parameters, frequency)
frequency += 1

api = "https://iw233.cn/api.php?sort=top" #pc20, random30, cat20, mp50, top50
parameters = {
    "type": "json",
    'num': 50
}
main(api, parameters, frequency)
frequency += 1

# for i in range(0,x):
#     Frequency = i 