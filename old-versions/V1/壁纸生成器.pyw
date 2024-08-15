import requests
import json
from skimage import io
from tkinter import *
from tkinter import messagebox
import matplotlib.pyplot as plt
import pyperclip
import os
import time

def about():
    messagebox.showinfo('关于','依赖API：MirlKoiAPI\n    API源(电脑壁纸)：https://dev.iw233.cn/api.php?sort=random\n    API源(手机壁纸)：https://dev.iw233.cn/api.php?sort=mp\nexe封装：思锐工作室\n\ntips：启动该工具后的首次生成时间相对较长，大于需要5至60秒。')

def phone_background():
    start_time = time.time()
    label.configure(text = '记录：正在生成中…………………………………………')
    configuration.title('MirlKoi - AI画图(正在生成，请勿强行关闭程序)')
    configuration.update()
    api = "https://dev.iw233.cn/api.php?sort=mp"
    parameters = {
        "type": "json",
        'num': 1
    }
    print(type(parameters))
    response = requests.get(api, params=parameters)
    try:
        #print(response.text())
        outputurl = json.dumps(response.json())
        print(outputurl)
        output = outputurl[10:-3]

        image = io.imread(output)
        io.imsave('figure1.png', image)
        # img = plt.imread('figure1.png')
        # fig = plt.figure('生成的图片(正在在线查看，保存后查看效果更佳)')
        # ax = fig.add_subplot(111)
        # plt.axis('off')
        configuration.title('MirlKoi - AI画图')
        pyperclip.copy(output)
        os.startfile(r'figure1.png')
        end_time = time.time()
        spend_time = end_time - start_time
        label.configure(text = '记录：生成了，花费' + str(spend_time)[:-10] + '秒之多，缓存放在了程序根目录')
        messagebox.showinfo('生成完毕','图像链接已复制至粘贴板，请尽快另存为图像！')
    except:
        configuration.title('MirlKoi - AI画图')
        messagebox.showwarning("Error",response)

def pc_background():
    start_time = time.time()
    label.configure(text = '记录：正在生成中…………………………………………')
    configuration.title('MirlKoi - AI画图(正在生成，请勿强行关闭程序)')
    configuration.update()
    api = "https://dev.iw233.cn/api.php?sort=random"
    parameters = {
        "type": "json",
        'num': 1
    }
    response = requests.get(api, params=parameters)
    try:
        #print(response.text())
        outputurl = json.dumps(response.json())
        output = outputurl[10:-3]

        image = io.imread(output)
        io.imsave('figure1.png', image)
        # img = plt.imread('figure1.png')
        # fig = plt.figure('生成的图片(正在在线查看，保存后查看效果更佳)')
        # ax = fig.add_subplot(111)
        # plt.axis('off')
        configuration.title('MirlKoi - AI画图')
        pyperclip.copy(output)
        os.startfile(r'figure1.png')
        end_time = time.time()
        spend_time = end_time - start_time
        label.configure(text = '记录：生成了，花费' + str(spend_time)[:-10] + '秒之多，缓存放在了程序根目录')
        messagebox.showinfo('生成完毕','图像链接已复制至粘贴板，请尽快另存为图像！')
    except:
        configuration.title('MirlKoi - AI画图')
        messagebox.showwarning("Error",response)
    
configuration = Tk()
configuration.iconbitmap('ico.ico')
configuration.title('MirlKoi - AI画图')
configuration.geometry("383x220")
configuration.resizable(width=False, height=False)
label=Label(configuration,text="                     AI 画图",font=('微软雅黑', 15, 'bold'))
label.place(x=0,y=0)
button=Button(configuration, width=52,height=2, text='在线生成 - 电脑壁纸 (可能包含未过审图片！)', command=pc_background)
button.place(x=3,y=50)
button1=Button(configuration, width=52,height=2, text='在线生成 - 手机壁纸', command=phone_background)
button1.place(x=3,y=100)
label=Label(configuration,text="记录：还没有生成。",font=('微软雅黑', 10,))
label.place(x=3,y=170)
menubar=Menu(configuration)
menubar.add_command(label='关于',command=about)
configuration.config(menu=menubar)
configuration['menu']=menubar
configuration.mainloop()

# def jprint(obj):

#     # create a formatted string of the Python JSON object

#     text = json.dumps(obj, sort_keys=True, indent=4)
#     print(text)


#img = plt.imread(output)
#fig = plt.figure('获取的图像')
#ax = fig.add_subplot(111)
#ax.imshow(img)
