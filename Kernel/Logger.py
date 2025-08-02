import logging
import inspect

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
handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
handler.addFilter(QAsyncFilter())
root_logger.addHandler(handler)

# 保持向后兼容
logger = get_logger()

__all__ = ['logger', 'get_logger']
