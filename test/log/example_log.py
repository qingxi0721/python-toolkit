from src.pmtoolkit.log.Log import Logger

# 创建测试日志
test_logger = Logger('DEBUG', 'test-logger')
# 输出到std
test_logger.add_stream_handler('stdout', "DEBUG")
test_logger.add_stream_handler('stderr', "ERROR")
# 输出到文件
test_logger.add_file_handler('test-log.log', file_mode='w')


test_logger.info('-----------------------函数装饰器示例开始-----------------------')


# 函数装饰器用法（正常返回）
@test_logger.logging_function
def test_function():
    return 2


# 函数装饰器用法（捕捉错误）
@test_logger.logging_function
def test_function_error():
    try:
        open('test.txt')
    except Exception as e:
        print(e)


test_function()
test_function_error()

test_logger.info('-----------------------函数装饰器示例结束-----------------------')


test_logger.info('-----------------------上下文日志捕捉示例开始-----------------------')

with test_logger.logging_context("test_context"):
    test_logger.info('这是一些上下文信息')
    test_function()

test_logger.info('-----------------------上下文日志捕捉示例结束-----------------------')
