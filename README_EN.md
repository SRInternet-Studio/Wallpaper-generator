# <div align="center">✨ Wallpaper Generator NEXT</div>

<img width="2560" height="1440" alt="Production" src="https://github.com/user-attachments/assets/be589274-a587-44ec-a965-6e898f5c4850" />

<p></p>

<p align="center">
  <img src="https://img.shields.io/static/v1?label=LICENSE&message=MIT&color=coral" alt="Badge">
  <img src="https://img.shields.io/github/languages/top/SRInternet-Studio/Wallpaper-generator" alt="Language">
  <img src="https://img.shields.io/badge/FREE-100%25-brightgreen" alt="FREE">
  <img src="https://img.shields.io/github/stars/SRInternet-Studio/Wallpaper-generator" alt="Stars">
  <img alt="GitHub Downloads (all assets, all releases)" src="https://img.shields.io/github/downloads/SRInternet-Studio/Wallpaper-generator/total?style=social&logo=github&label=Downloads">
</br><img alt="GitHub Release" src="https://img.shields.io/github/v/release/SRInternet-Studio/Wallpaper-generator?label=Stable">
  <img alt="GitHub Release" src="https://img.shields.io/github/v/release/SRInternet-Studio/Wallpaper-generator?include_prereleases&label=Preview">
</p>
 <div align="center">
 
**「 Imagine It. Generate It.​ 」**<br/>

Wallpaper Generator is a personalized aggregated image generation platform that can automatically change wallpapers at scheduled times, supporting Windows and Linux.
   
#### [💬 SR Studio User QQ Group](https://qm.qq.com/q/f3QGDkdp6M)｜[🛍️ Image Source Market](https://github.com/IntelliMarkets/Wallpaper_API_Index/)

#### [🌐 APP Center ](https://app.sr-studio.cn)｜[🛠️ Plugin Development ](https://github.com/SRON-org/APICORE/wiki/Create-a-New-APICORE-Configuration-File)｜[💖 Support Us ](https://afdian.com/a/srinternet)｜[📝 Report Issues](https://github.com/SRInternet-Studio/Wallpaper-generator/issues)

###### [Watch the flash introduction to learn about disruptive innovation →](https://b23.tv/BV1xp81zFE3H)

###### [切换到简体中文](README.md) </div>

> [!NOTE]  
 > For Android version, please visit: [Wallpaper Generator NEXT - Mobile Version](https://github.comesRInternet-Studio/Wallpaper-generator-Mobile).
>
> **Wallpaper Generator NEXT is currently not compatible with English.**

## Details

### Features
- ✨ Asynchronous frontend and backend, fast startup, multi-threaded wallpaper generation
- ✨ Plugin market integration, including AI drawing, Pixiv, furry... and many more types
- ✨ Self-developed [APICORE](https://github.com/SRON-org/APICORE) specification, making image generation simpler
- ✨ Support manually creating gradient wallpapers
- ✨ Support setting time intervals and automatic wallpaper change at startup
- ✨ Daily recommended wallpapers

### Compatibility
- Supports Windows10-Windows11 X64 operating systems

> Requires .NET Framework (can be downloaded [here](https://download.microsoft.com/download/6/e/4/6e483240-dd87-40cd-adf4-0c47f5695b49/NDP481-Web.exe))

### Follow us on:

 - [Douyin](https://www.douyin.com/user/MS4wLjABAAAATzdjtBBrLLCn69TtPMeseuEUzztbNZzw-9f13adrfiM?relation=0&vid=7143257533807873316)

 - [Bilibili](https://space.bilibili.com/1969160969)

 - [Xiaohongshu](https://www.xiaohongshu.com/user/profile/6427cf87000000002901166e)
  
 - [Youtube](https://www.youtube.com/channel/UCEPXlJTTAoKun8cYY1ix3ew)

[Buy us a coffee!](https://afdian.com/a/srinternet)

## How to Use

### Installation
1. Read the [Disclaimer](https://github.com/SRInternet-Studio/Wallpaper-generator/blob/NEXT-PREVIEW/DISCLAIMER.md)
2. Download the latest **Pre-release** installer (.exe) from [Releases](https://github.com/SRInternet-studio/Wallpaper-generator/releases);
3. Double-click to install, follow the prompts step by step;
4. Launch the software.

### Generate Wallpapers
1. In the navigation bar at the top of the main interface, you can switch between different image types to enter different generation modes;
2. If there are no available image types or no types you like, you can switch to the **Image Source Market** tab, add your favorite image types, then restart Wallpaper Generator;
3. For first-time generation, it is recommended to go to the **Settings** tab and select a preferred path for saving images to avoid excessive system space usage;
4. Return to the generation page, adjust parameters such as generation quantity and type, then click generate;
5. Wait for the generation completion prompt, and you will see the generated images on the right;
6. Click on the generated images on the right to open a floating menu, supporting functions like setting as wallpaper, opening with system image viewer, opening with file explorer, and information query;
7. Click the page indicator at the bottom right to scroll through images.

### How to Enable Auto-start and Automatic Change
1. Click on "Tray program for automatic wallpaper change" in the **Welcome** tab;
2. In the **Automatic Wallpaper Change** window, enable automatic change, then set the change interval, whether to start at boot, etc.;
3. After successfully enabling automatic wallpaper change, you will see a countdown to the next automatic change in the window;
4. In the system tray at the bottom right of the taskbar, you can right-click and select "Change Wallpaper Now" to skip the current countdown and change the wallpaper immediately (if not visible, it may be hidden - click the upward arrow icon *^* on the far left of the tray area to expand hidden tray icons);
5. Click "Apply" to save settings, close the window to return to the welcome page.

### How to Provide Feedback
You can submit an Issue [here](https://github.com/SRInternet-studio/Wallpaper-generator/issues/new). You can also provide feedback via our email srinternet@qq.com.

## How to Deploy Source Code
> Wallpaper Generator 5.0.0 mostly uses Python [^1], which requires your computer to have Python>=3.10 standard environment and required dependencies [(requirements.txt)](requirements.txt)

### Configure Required Python Environment
1. Go to the [official website](https://www.python.org) to download Python 3.10 or higher, Python 3.12 is recommended;
2. Install Python following the installer's instructions;
3. Create a Python virtual environment
   ```bash
   python -m venv wpg_next
   ```
4. Download required third-party libraries;
   ```bash
   python -m pip install -r requirements.txt
   ```
5. Start the program `MainWindow.py`
   ```bash
   python ./MainWindow.py
   ```

[^1]: The code mainly uses Python for the main interface and most core components, while Visual Basic.NET is used for the "Gradient Wallpaper Generator", so the "Gradient Wallpaper Generator" currently only supports Windows systems.
