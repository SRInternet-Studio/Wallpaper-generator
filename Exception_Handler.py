import sys, os
import traceback
import logging
from types import TracebackType
from typing import Optional, Type, Union, Any, Callable

class GlobalExceptionHandler:
    """全局异常捕获器"""
    def __init__(self, 
                 log_file: str = "errors.log", 
                 console_output: bool = True,
                 exit_on_error: bool = False,
                 custom_handler: Optional[Callable] = None):
        """
        :param log_file: 错误日志文件路径
        :param console_output: 是否在控制台显示错误信息
        :param exit_on_error: 发生未处理异常后是否退出程序
        :param custom_handler: 自定义异常处理函数，格式: func(exc_type, exc_value, exc_traceback)
        """

        self.log_file = os.path.abspath(log_file)
        self.console_output = console_output
        self.exit_on_error = exit_on_error
        self.custom_handler = custom_handler
        self.original_excepthook = sys.excepthook
        
        self.logger = logging.getLogger('SR-Underlying ExceptionHandler') # 独立于 Logger 的日志系统使其更稳定
        self.logger.setLevel(logging.ERROR)
        
        if not any(isinstance(h, logging.FileHandler) for h in self.logger.handlers):
            print(f"Logging to file: {self.log_file}")
            file_handler = logging.FileHandler(self.log_file, encoding='utf-8')
            file_handler.setFormatter(logging.Formatter(
                '%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
            self.logger.addHandler(file_handler)
            
        if os.path.exists(self.log_file):
            try: 
                os.remove(self.log_file)
            except: 
                pass
        
        self.register() # 注册全局
        
    def exception_handler(self, 
                          exc_type: Type[BaseException], 
                          exc_value: BaseException, 
                          exc_traceback: Optional[TracebackType]) -> None:
        """默认的异常处理"""
        if issubclass(exc_type, KeyboardInterrupt):
            if self.original_excepthook:
                self.original_excepthook(exc_type, exc_value, exc_traceback)
            return
        
        # -> 日志文件
        try:
            error_msg = "".join(traceback.format_exception(exc_type, exc_value, exc_traceback))
            error_msg = error_msg.encode('utf-8', 'replace').decode('utf-8')
        except UnicodeEncodeError:
            error_msg = traceback.format_exception_only(exc_type, exc_value)[0]
            error_msg = error_msg.encode('utf-8', 'replace').decode('utf-8')
            error_msg += "\n[完整的回溯信息包含非UTF8字符]"
        self.logger.error(f'''Unhandled exception:\n{error_msg}    
Error capture originated from: SR-Underlying ExceptionHandler for Python v1
Can contact us here: http://github.com/SRInternet-Studio/
**This capture program may circulate in multiple program distributions, so please indicate the PROGRAM NAME and VERSION when providing feedback**\n\n''')
        
        # -> 控制台
        if self.console_output:
            # sys.stderr.write(f"\n{'-'*50}\n")
            # sys.stderr.write("!!! CRITICAL ERROR !!!\n")
            sys.stderr.write(f"\n\n")
            sys.stderr.write("An unhandled exception occurred:\n")
            sys.stderr.write(f"Type: {exc_type.__name__}\n")
            sys.stderr.write(f"Message: {str(exc_value)}\n")
            sys.stderr.write(f"Traceback saved to: {self.log_file}\n")
            sys.stderr.write(f"\n\n")
            # sys.stderr.write(f"{'-'*50}\n\n")
        
        if self.custom_handler:
            try:
                safe_exc_value = str(exc_value).encode('utf-8', 'replace').decode('utf-8')
                self.custom_handler(exc_type, safe_exc_value, exc_traceback)
            except Exception as e:
                try:
                    safe_error = f"Custom handler failed: {str(e)}".encode('utf-8', 'replace').decode('utf-8')
                    self.logger.error(safe_error)
                except:
                    self.logger.error("Custom handler failed with unencodable error")
        
        if self.exit_on_error: # 是否致命
            sys.exit(1)
    
    def register(self) -> None:
        """注册全局异常处理钩子"""
        sys.excepthook = self.exception_handler
        
    def unregister(self) -> None:
        """恢复原始异常处理钩子"""
        sys.excepthook = self.original_excepthook
        
    def __enter__(self) -> 'GlobalExceptionHandler':
        """支持上下文管理器"""
        return self
        
    def __exit__(self, 
                 exc_type: Optional[Type[BaseException]], 
                 exc_value: Optional[BaseException], 
                 exc_traceback: Optional[TracebackType]) -> bool:
        """离开上下文时恢复原始钩子"""
        self.unregister()
        # 如果上下文中有异常发生，返回True表示已处理
        return exc_type is not None


def setup_global_exception_handler(
    log_file: str = "errors.log", 
    console_output: bool = True,
    exit_on_error: bool = True,
    custom_handler: Optional[Callable] = None
) -> GlobalExceptionHandler:
    """
    自定义全局异常处理器
    
    使用示例:
    handler = setup_global_exception_handler(
        log_file="my_app_errors.log",
        console_output=False,
        custom_handler=my_error_handler
    )
    """
    return GlobalExceptionHandler(
        log_file=log_file,
        console_output=console_output,
        exit_on_error=exit_on_error,
        custom_handler=custom_handler
    )