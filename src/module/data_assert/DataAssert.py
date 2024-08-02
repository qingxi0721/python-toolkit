import json
import os
import uuid
from typing import Literal


class DataAssert:
    def __init__(self):
        self.data_assert_set = []

    # 添加数据校验
    def add_assert(self, result: Literal['success', 'failed', 'skipped'], content: str) -> uuid.UUID:
        data_id = uuid.uuid4()
        self.data_assert_set.append({"result": result, "content": content, "id": data_id})
        return data_id

    # 删除数据校验
    def delete_assert(self, assert_id: uuid.UUID) -> dict[str, str]:
        try:
            for data in self.data_assert_set:
                if data["id"] == assert_id:
                    self.data_assert_set.remove(data)
                    return data
        except Exception as e:
            print(f'需要删除的数据验证信息不存在:{e}')

    # 清空所有数据校验
    def clear_assert(self) -> None:
        self.data_assert_set = []

    # 获取数据校验
    def get_assert(self) -> list[dict[str, str]]:
        return self.data_assert_set

    # 将数据校验写入文件
    def write_assert_file(self, path: str) -> str:
        try:
            with open(path, 'w', encoding="utf-8") as file:
                result = [
                    {"result": data["result"], "content": data["content"]}
                    for data in self.data_assert_set
                ]
                json.dump(result, file, ensure_ascii=False)
            return os.path.abspath(path)

        except Exception as e:
            print(f"数据写入失败：{e}")
