from src.pmtoolkit.log.Log import Logger
from src.pmtoolkit.reading_config.ReadingConfig import ReadingConfig

# 日志
reading_logger = Logger('DEBUG', 'reading_logger')
reading_logger.add_stream_handler('stdout', "INFO")

# 创建读取配置示例
config_reader = ReadingConfig()

with reading_logger.logging_context('reading_context'):
    # 读取ini
    reading_logger.info('------------------读取ini文件开始------------------')
    reading_logger.info(config_reader.get('test.ini'))  # 返回字典类型
    reading_logger.info('------------------读取ini文件结束------------------')

    # 读取json
    reading_logger.info('------------------读取json文件开始------------------')
    reading_logger.info(config_reader.get('test.json'))  # 返回字典/字典数组类型
    reading_logger.info('------------------读取json文件结束------------------')

    # 读取yaml
    reading_logger.info('------------------读取yaml文件开始------------------')
    reading_logger.info(config_reader.get('test.yaml'))  # 返回字典类型
    reading_logger.info('------------------读取yaml文件结束------------------')

    # 读取xml
    reading_logger.info('------------------读取xml文件开始------------------')
    reading_logger.info(config_reader.get('test.xml'))  # 返回字典类型
    reading_logger.info('------------------读取xml文件结束------------------')
