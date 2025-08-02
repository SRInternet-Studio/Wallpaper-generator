import winreg
import os
import sys
import struct
import traceback
from Kernel.OsKernal import os
from Kernel.Logger import logger

class StartupManager:
    def __init__(self, startup_path, value):
        self.startup_command = r"{}".format(os.path.abspath(startup_path)) + r" {}".format(value)
        self.value_name = os.path.basename(startup_path)
        
    def AddToStartup(self) -> str:
        try:
            startup_command = self.startup_command
            is_64bits = struct.calcsize("P") * 8 == 64

            if is_64bits:
                key_path = r"SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Run"
            else:
                key_path = r"Software\Microsoft\Windows\CurrentVersion\Run"

            print(startup_command)
                # 打开注册表，路径为 HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Run
            with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path, 0, winreg.KEY_SET_VALUE) as reg_key:
                        # 将WallpaperGenerator.exe添加到注册表
                winreg.SetValueEx(reg_key, self.value_name, 0, winreg.REG_SZ, startup_command)
            return "True"
        except:
            return traceback.format_exc()

    def RemoveFromStartup(self) -> str:
        try:
              is_64bits = struct.calcsize("P") * 8 == 64

              if is_64bits:
                 key_path = r"SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Run"
              else:
                 key_path = r"Software\Microsoft\Windows\CurrentVersion\Run"

              with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path, 0, winreg.KEY_SET_VALUE) as reg_key:
                # 删除 WallpaperGenerator 启动项
                winreg.DeleteValue(reg_key, self.value_name)
              return "True"
        except:
              return traceback.format_exc()

    def IsAddedToStartup(self) -> bool: 
        startup_command = self.startup_command
        logger.debug("startup_command: {}".format(startup_command))

        is_64bits = struct.calcsize("P") * 8 == 64

        if is_64bits:
            key_path = r"SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Run"
        else:
            key_path = r"Software\Microsoft\Windows\CurrentVersion\Run"

        value_name = self.value_name
        try:
                # 打开注册表项
                with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path) as reg_key:
                # 获取指定值
                        value, regtype = winreg.QueryValueEx(reg_key, value_name)
                        script_path = os.path.abspath(sys.argv[0])
                        expected_value = startup_command
                        
                # 检查值是否匹配
                return value is not None and value == expected_value
        except FileNotFoundError:
                return False
        except Exception as e:
                return False