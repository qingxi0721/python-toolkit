import contextlib
import functools
import logging
import os
import sys
from typing import Literal


# 日志类
class Logger:
    def __init__(self, logger_level: str, logger_name: str = ""):
        self.logger = logging.getLogger(logger_name)
        self.logger.setLevel(logger_level)

    # 创建stdout/stderr处理器
    def add_stream_handler(self, handler_type: Literal['stdout', 'stderr'],
                           handler_level: Literal['INFO', 'DEBUG', 'ERROR', 'CRITICAL', 'WARNING'],
                           handler_formatter: str = "") -> logging.Handler:

        # 格式化
        if handler_formatter == "":
            handler_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        else:
            handler_formatter = logging.Formatter(handler_formatter)

        # 设置类型
        if handler_type == "stdout":
            handler = logging.StreamHandler(sys.stdout)
        elif handler_type == "stderr":
            handler = logging.StreamHandler(sys.stderr)
        else:
            raise ValueError("Invalid handler type")

        # 设置级别
        handler.setLevel(handler_level)

        # 格式化
        handler.setFormatter(handler_formatter)

        # 添加处理器
        self.logger.addHandler(handler)

        return handler

    # 创建file处理器，将日志输出到指定文件路径中
    def add_file_handler(self, file_path: str, file_mode: str = "a", handler_level: str = "DEBUG",
                         file_encoding: str = "UTF-8", delay: bool = False,
                         handler_formatter: str = "") -> logging.Handler:
        # 没有文件的话创建文件
        if not os.path.exists(file_path):
            open(file_path, "w")

        file_handler = logging.FileHandler(file_path, file_mode, file_encoding, delay)

        # 设置级别
        file_handler.setLevel(handler_level)

        # 格式化
        if handler_formatter == "":
            handler_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        else:
            handler_formatter = logging.Formatter(handler_formatter)
        file_handler.setFormatter(handler_formatter)

        # 加入logger中
        self.logger.addHandler(file_handler)
        return file_handler

    # 移除处理器
    def remove_handler(self, handler: logging.Handler) -> None:
        self.logger.removeHandler(handler)

    # 控制台输出日志信息
    def info(self, message: str):
        self.logger.info(message)

    def debug(self, message: str):
        self.logger.debug(message)

    def error(self, message: str):
        self.logger.error(message)

    def critical(self, message: str):
        self.logger.critical(message)

    def warning(self, message: str):
        self.logger.warning(message)

    # 创建函数打印装饰器
    """
        打印整个函数中的日志以及返回值
        @logger.logging_function
        def test_function():
            return 1
    """

    def logging_function(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                self.logger.info(f"调用函数名: {func.__name__};参数：{args};关键字参数：{kwargs}")
                result = func(*args, **kwargs)
                self.logger.info(f"函数{func.__name__}的结果为：{result}")
                return result
            except Exception as e:
                self.logger.error(f"函数{func.__name__}抛出异常：{e}")

        return wrapper

    # 收集上下文中所有的日志并输出
    """
        打印整个上下文中日志并输出（迭代器）
        with logger.logging_context(test_function):
            ......
            pass
    """

    @contextlib.contextmanager
    def logging_context(self, message):
        self.info(f"进入上下文：{message}")
        try:
            yield
        except Exception as e:
            self.error(f"上下文{message}中出现异常：{e}")
        finally:
            self.info(f"退出上下文：{message}")

    # def set_interval_remover(self, interval:int,path:str)->None
