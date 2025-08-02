import shlex
import traceback
import platform
from pathlib import Path
from functools import wraps
from Kernel.OsKernal import os
from Kernel.Logger import logger
    
class StartupManager:
    def __init__(self, startup_path, value, value_name=None):
        # Remove surrounding quotes if present
        clean_path = startup_path.strip("'\"")
        abs_path = os.path.abspath(clean_path)
        self.startup_command = f'"{abs_path}" {value}'
        self.value_name = value_name if value_name else os.path.basename(clean_path)
        self.executable = abs_path
        self.arguments = value
        self.platform = platform.system().lower()
        
    def usermethod(func):
        @wraps(func)
        def wrapper(instance, *args, **kwargs):
            try:
                logger.debug(f"StartupManager: {instance.value_name} - {instance.startup_command} **{func.__name__}** on {instance.platform}")
                result = func(instance, *args, **kwargs)
                return result
            except Exception as e:
                raise
        return wrapper
        
    @usermethod
    def AddToStartup(self) -> str:
        try:
            if self.platform == "windows":
                return self._add_windows()
            elif self.platform == "darwin":
                return self._add_macos()
            elif self.platform == "linux":
                return self._add_linux()
            else:
                return f"Unsupported platform: {self.platform}"
        except:
            raise

    @usermethod
    def RemoveFromStartup(self) -> str:
        try:
            if self.platform == "windows":
                return self._remove_windows()
            elif self.platform == "darwin":
                return self._remove_macos()
            elif self.platform == "linux":
                return self._remove_linux()
            else:
                return f"Unsupported platform: {self.platform}"
        except:
            raise

    @usermethod
    def IsAddedToStartup(self) -> bool:
        if self.platform == "windows":
            return self._is_added_windows()
        elif self.platform == "darwin":
            return self._is_added_macos()
        elif self.platform == "linux":
            return self._is_added_linux()
        return False

    # ===== Windows 实现 =====
    def _add_windows(self) -> str:
        import winreg
        key_path = r"Software\Microsoft\Windows\CurrentVersion\Run"
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_SET_VALUE) as reg_key:
            winreg.SetValueEx(reg_key, self.value_name, 0, winreg.REG_SZ, self.startup_command)
        return "True"

    def _remove_windows(self) -> str:
        import winreg
        key_path = r"Software\Microsoft\Windows\CurrentVersion\Run"
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_SET_VALUE) as reg_key:
            winreg.DeleteValue(reg_key, self.value_name)
        return "True"

    def _is_added_windows(self) -> bool:
        import winreg
        key_path = r"Software\Microsoft\Windows\CurrentVersion\Run"
        try:
            with winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path) as reg_key:
                value, _ = winreg.QueryValueEx(reg_key, self.value_name)
                return value == self.startup_command
        except FileNotFoundError:
            return False
        except OSError:
            return False

    # ===== macOS 实现 =====
    def _get_macos_plist_path(self) -> Path:
        return Path.home() / "Library" / "LaunchAgents" / f"{self.value_name}.plist"

    def _add_macos(self) -> str:
        args = [self.executable]
        if self.arguments:
            args.extend(shlex.split(self.arguments))
            
        args_xml = "\n".join([f"        <string>{arg}</string>" for arg in args])
        plist_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>{self.value_name}</string>
    <key>ProgramArguments</key>
    <array>
{args_xml}
    </array>
    <key>RunAtLoad</key>
    <true/>
</dict>
</plist>"""

        plist_path = self._get_macos_plist_path()
        plist_path.parent.mkdir(parents=True, exist_ok=True)
        plist_path.write_text(plist_content)
        return "True"

    def _remove_macos(self) -> str:
        plist_path = self._get_macos_plist_path()
        if plist_path.exists():
            plist_path.unlink()
        return "True"

    def _is_added_macos(self) -> bool:
        return self._get_macos_plist_path().exists()

    # ===== Linux 实现 =====
    def _get_linux_desktop_path(self) -> Path:
        return Path.home() / ".config" / "autostart" / f"{self.value_name}.desktop"

    def _add_linux(self) -> str:
        desktop_content = f"""[Desktop Entry]
Type=Application
Name={self.value_name}
Exec={self.startup_command}
X-GNOME-Autostart-enabled=true
"""
        desktop_path = self._get_linux_desktop_path()
        desktop_path.parent.mkdir(parents=True, exist_ok=True)
        desktop_path.write_text(desktop_content)
        return "True"

    def _remove_linux(self) -> str:
        desktop_path = self._get_linux_desktop_path()
        if desktop_path.exists():
            desktop_path.unlink()
        return "True"

    def _is_added_linux(self) -> bool:
        return self._get_linux_desktop_path().exists()