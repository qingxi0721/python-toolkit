import sys

# 全局捕获异常类


class GlobalException(Exception):
    def __init__(self, logger):
        self.logger = logger

    # 处理全局异常
    def handle_exception(self, exception_type, value, traceback):
        print(traceback)
        self.logger.error(value)

    # 注册全局异常捕获器
    def register(self):
        sys.excepthook = self.handle_exception
