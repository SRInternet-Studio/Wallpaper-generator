import logging
import inspect

COLORS = {
    'DEBUG': '\033[92m',    # 绿色 # '\033[36m',     # 青色
    'INFO': '\033[34m',      # 蓝色
    'WARNING': '\033[33m',   # 黄色
    'ERROR': '\033[31m',     # 红色
    'CRITICAL': '\033[31;1m' # 红色加粗
}
RESET = '\033[0m'

class ColoredFormatter(logging.Formatter):
    def format(self, record):
        # 获取原始日志消息
        message = super().format(record)
        # 根据日志级别添加颜色
        levelname = record.levelname
        color = COLORS.get(levelname, '')
        
        colored_levelname = f"{color}{levelname}{RESET}"
        message = message.replace(levelname, colored_levelname)
        
        return message
    
class QAsyncFilter(logging.Filter):
    def filter(self, record):
        # 屏蔽qasync的DEBUG日志
        if record.name.startswith('qasync') and record.levelno <= logging.DEBUG:
            return False
        return True

def get_logger():
    # 获取调用栈信息
    frame = inspect.currentframe().f_back.f_back
    module = inspect.getmodule(frame)
    # 获取调用模块的名称
    module_name = module.__name__ if module else '__main__'
    logger = logging.getLogger(module_name)
    
    # 为qasync设置更高的日志级别
    if module_name.startswith('qasync'):
        logger.setLevel(logging.WARNING)
    
    return logger

root_logger = logging.getLogger()
root_logger.setLevel(logging.DEBUG)

# 移除所有现有处理器
for handler in root_logger.handlers[:]:
    root_logger.removeHandler(handler)

handler = logging.StreamHandler()
formatter = ColoredFormatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s') # datefmt='%Y-%m-%d %H:%M:%S'
handler.setFormatter(formatter)
handler.addFilter(QAsyncFilter())
root_logger.addHandler(handler)

# 保持向后兼容
logger = get_logger()

__all__ = ['logger', 'get_logger']
