# 🥳Wallpaper generator
 从此个性化你的电脑。
 
快速了解我们：[观看 壁纸生成器 宣传片](https://www.bilibili.com/video/BV1yF411k7Rm/?spm_id_from=333.999.0.0)
 
 *本系列产品包含 [Android 版](https://github.com/SRInternet/Wallpaper-generator/) 和 [Android 版独立分支](https://github.com/SRInternet/Pixiv-generator/)。

## 详细信息

### 功能/特点
- ✨快速生成壁纸，支持多种类型
- ✨支持手搓渐变色壁纸
- ✨支持开机自启动，托盘程序低占用
- ✨可批量生成

### 兼容性
- 支持 Windows7 SP1-Windows11 X64 操作系统

> 需要.NET Framework (可以在这里[下载](https://download.microsoft.com/download/6/e/4/6e483240-dd87-40cd-adf4-0c47f5695b49/NDP481-Web.exe))


[Buy us a coffee!](https://afdian.net/a/srinternet)

[Follow us（Douyin）](https://www.douyin.com/user/MS4wLjABAAAATzdjtBBrLLCn69TtPMeseuEUzztbNZzw-9f13adrfiM?relation=0&vid=7143257533807873316)

[Follow us（Bilibili）](https://space.bilibili.com/1969160969?spm_id_from=333.1007.0.0)

[Follow us（Youtube）](https://www.youtube.com/channel/UCEPXlJTTAoKun8cYY1ix3ew)

## 如何使用

### 安装
1. 下载 [Releases](https://github.com/SRInternet/Wallpaper-generator/releases) 中的最新版安装程序（.exe）
2. 双击安装，跟着提示一步步来
3. 启动软件

### 生成壁纸
1. 在软件主界面点击 图像生成
2. 在弹出的新窗口（不是命令行窗口）中选择你想生成的壁纸类型，点击按钮
3. 选择保存的路径和文件名
4. 等待提示生成结束（单张生成在结束后会弹出壁纸，批量生成在结束后会弹出壁纸的保存路径）

### 如何开机自启
1. 在软件主界面点击 自动更换壁纸的托盘程序
2. 首次使用加载时间较长，请等待托盘程序的设置界面的弹出（若不是首次使用托盘程序则跳过此步）
3. 您会看到在任务栏右下方托盘处多出一个图标，图标中是一个动漫人物的头像（若您没有看到则可能被隐藏起来了，请点击托盘处最左侧的向上的箭头的图标 *^* 以展开被隐藏的托盘图标）
4. 右键托盘图标，点击 打开设置 以打开设置界面（首次使用会直接弹出设置界面）
5. 勾选 开机自启动 和 启动后自动更换壁纸
6. 点击 保存并关闭 即可完成开机自启

### 如何反馈
您可以在[这里](https://github.com/SRInternet/Wallpaper-generator/issues/new)提交Issuse。您也可以通过我们的邮箱 srinternet@qq.com 进行反馈。

## 如何部署源代码
> 壁纸生成器 3.0.0 采用了 Python 和 Visual Basic.NET 双代码结合[^1]的方式进行编写，这要求你的电脑中需要包含 Python 3.9 的标准环境和所需环境[^2] 以及 Blend for Visual Studio 2019 。

### 配置所需 Python 环境
1. 前往[官网](https://www.python.org)下载 Python 3.9 及以上版本，推荐 Python 3.11
2. 根据安装程序的提示安装 Python
3. 下载所需的第三方库
   ```
   python -m pip install -r requirements.txt
   ```


### 配置所需 VB.NET 环境
1. 前往[官网](https://visualstudio.microsoft.com)下载并安装 Visual Studio Installer。
2. 打开 Visual Studio Installer ，在安装配置界面勾选上 .NET 桌面开发、通用 Windows 平台开发 或 Visual Studio 扩展开发。
3. 安装好 Visual Studio 后，检查是否包含 Blend for Visual Studio，若包含则完成此步。

### 如何使用源代码
源代码的目录结构层次如下：
源代码中的根目录下都是安装程序的存档，请使用 Advanced Installer 20.9 打开 壁纸生成器_Setup_File.aip ，剩下的 aip 文件都是备份文件。
#### 1. Wallpapers 批量（核心部分）
这个文件夹没什么用，主要内容是 图像生成插件 的批量生成核心代码，当初用来打草稿的。
#### 2. 壁纸生成器主程序
这个文件夹内包含 壁纸生成器 的主界面，使用 Blend for Visual Studio 打开其中的 .sln 文件。
#### 3. 壁纸生成器-自动壁纸设置界面
这个文件夹内包含 壁纸生成器 的 自动更换壁纸托盘程序 的设置界面，使用 Blend for Visual Studio 打开其中的 .sln 文件。
#### 4. 插件-自动换壁纸
这个文件夹内包含 壁纸生成器 的 自动更换壁纸托盘程序 的核心部分，包括托盘图标和右键菜单，使用 Python IDLE 或其他 Python 编辑器打开。
#### 5. 图像生成插件
这个文件夹内包含 壁纸生成器 的 图像生成插件 的全部，使用 Python IDLE 或其他 Python 编辑器打开。
#### 6. 源代码中的根目录下都是安装程序的存档，请使用 Advanced Installer 20.9 打开 壁纸生成器_Setup_File.aip ，剩下的 aip 文件都是备份文件。

[^1]: 指部分代码采用了 Python 编写核心部分代码，Visual Basic.NET 编写 UI 的形式，例如 自动更换壁纸的托盘程序 。
[^2]: 所需环境包括以下内置库和第三方库：PyQt5, sys, requests, json, tkinter, scikit-image, matplotlib, pyperclip, os, time, asyncio, easygui, threading, queue, random, pywin32, ctypes, webbrowser, wxpython, psutil 等。
