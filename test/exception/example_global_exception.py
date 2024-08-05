from src.pmtoolkit.exception.GlobalException import GlobalException
from src.pmtoolkit.log.Log import Logger

# 创建一个日志处理器
exception_logger = Logger('DEBUG', 'exception_logger')
exception_logger.add_stream_handler('stderr', "ERROR")

# 创建一个全局异常处理器
global_exception_handler = GlobalException(exception_logger)
# 注册这个处理器
global_exception_handler.register()


def test_global_exception():
    return 1 / 0


test_global_exception()
