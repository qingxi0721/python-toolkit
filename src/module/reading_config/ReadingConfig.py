import configparser
import json
import os
from typing import Any

import xmltodict
import yaml


class ReadingConfig:
    def get(self, input_file: str) -> Any:

        try:
            os.path.exists(input_file)
        except FileNotFoundError:
            return None
        else:
            file_type = input_file.split('.')[-1]
            # 读取ini
            if file_type == 'ini':
                return self._get_ini(input_file)

            # 读取json
            elif file_type == 'json':
                return self._get_json(input_file)

            # 读取yaml
            elif file_type == 'yaml':
                return self._get_yaml(input_file)

            # 读取xml
            elif file_type == 'xml':
                return self._get_xml(input_file)
            else:
                raise ValueError(f"Unsupported file type: {file_type}")

    @staticmethod
    def _get_ini(input_file: str) -> dict[str, dict[str, str]]:
        # 创建配置解析器 区分大小写
        config = configparser.RawConfigParser()
        config.optionxform = lambda option: option
        config.read(input_file)

        # 递归返回字典类型
        return {section: dict(config.items(section)) for section in config.sections()}

    @staticmethod
    def _get_json(input_file: str) -> Any:
        with open(input_file, 'r') as f:
            return json.load(f)

    @staticmethod
    def _get_yaml(input_file: str) -> Any:
        with open(input_file, 'r') as f:
            return yaml.load(f, Loader=yaml.FullLoader)

    @staticmethod
    def _get_xml(input_file: str) -> Any:
        with open(input_file) as f:
            return xmltodict.parse(f.read())
