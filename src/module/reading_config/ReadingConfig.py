import configparser
import json
from typing import Any

import xmltodict
import yaml


class ReadingConfig:
    def __init__(self, input_file: str):
        self.input_file = input_file
        self.file_type = input_file.split('.')[-1]

    def get(self) -> Any:
        # 读取ini
        if self.file_type == 'ini':
            return self._get_ini()

        # 读取json
        elif self.file_type == 'json':
            return self._get_json()

        # 读取yaml
        elif self.file_type == 'yaml':
            return self._get_yaml()

        # 读取xml
        elif self.file_type == 'xml':
            return self._get_xml()
        else:
            raise ValueError(f"Unsupported file type: {self.file_type}")

    def _get_ini(self) -> dict[str, dict[str, str]]:
        # 创建配置解析器 区分大小写
        config = configparser.RawConfigParser()
        config.optionxform = lambda option: option
        config.read(self.input_file)

        # 递归返回字典类型
        return {section: dict(config.items(section)) for section in config.sections()}

    def _get_json(self) -> Any:
        with open(self.input_file, 'r') as f:
            return json.load(f)

    def _get_yaml(self) -> Any:
        with open(self.input_file, 'r') as f:
            return yaml.load(f, Loader=yaml.FullLoader)

    def _get_xml(self) -> Any:
        with open(self.input_file) as f:
            return xmltodict.parse(f.read())
