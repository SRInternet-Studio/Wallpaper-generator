import os
import subprocess
import shlex
import sys

def _startfile(filepath):
    if sys.platform == 'win32':
        return os.startfile(filepath)

    try: # Linux/macOS
        subprocess.run(['xdg-open', filepath], check=True) # xdg-open
    except (subprocess.CalledProcessError, FileNotFoundError):
        try:
            subprocess.run(['mimeopen', '-d', filepath], check=True) # mimeopen
        except (subprocess.CalledProcessError, FileNotFoundError):
            if os.path.isdir(filepath):
                subprocess.run(['xdg-open', os.path.dirname(filepath)]) # 打开目录
            else:
                editor = os.getenv('EDITOR', 'nano')
                subprocess.run(shlex.split(f"{editor} {shlex.quote(filepath)}")) # 使用编辑器打开文件

if not hasattr(os, 'startfile'):
    os.startfile = _startfile

__all__ = ['os']