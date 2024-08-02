from src.module.data_assert.DataAssert import DataAssert
from src.module.log.Log import Logger

# 日志
assert_logger = Logger('DEBUG', 'assert_logger')
assert_logger.add_stream_handler('stdout', "INFO")

# 数据验证
data_assert = DataAssert()


@assert_logger.logging_function
def test_data_assert(input_password: str):

    # 添加数据校验
    if input_password == '<PASSWORD>':
        success_id = data_assert.add_assert('success', f'输入值：{input_password},校验成功')
        assert_logger.info(f'数据校验ID为：{success_id}')
    else:
        failed_id = data_assert.add_assert('failed', f'输入值：{input_password},校验失败')
        assert_logger.info(f'数据校验ID为：{failed_id}')

        # 删除某条数据校验
        # data_assert.delete_assert(failed_id)

    assert_logger.info(str(data_assert.get_assert()))


test_data_assert(input_password='<PASSWORD>')
# 数据校验写入指定路径文件
data_assert.write_assert_file('data_success.json')
# 清空所有数据校验
data_assert.clear_assert()

test_data_assert(input_password='PASSWORD')
data_assert.write_assert_file('data_fail.json')
