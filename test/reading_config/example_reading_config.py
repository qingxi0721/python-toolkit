from src.pmtoolkit.log.Log import Logger
from src.pmtoolkit.reading_config.ReadingConfig import ReadingConfig

# 日志
reading_logger = Logger('DEBUG', 'reading_logger')
reading_logger.add_stream_handler('stdout', "INFO")

# 创建读取配置示例
config_reader = ReadingConfig()

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

# 读取xlsx
reading_logger.info('------------------读取xlsx文件开始------------------')
reading_logger.info(config_reader.get_xlsx('test.xlsx', 'array', 1))  # 返回字典类型
reading_logger.info(config_reader.get_xlsx('test.xlsx', 'dict', header=1))  # 返回字典类型
reading_logger.info('------------------读取xlsx文件结束------------------')

# 读取csv
reading_logger.info('------------------读取csv文件开始------------------')
reading_logger.info(config_reader.get_csv('test.csv', 'dict'))  # 返回字典类型
reading_logger.info(config_reader.get_csv('test.csv', 'array', 1))  # 返回字典类型
reading_logger.info('------------------读取csv文件结束------------------')
