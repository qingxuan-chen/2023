"""
coding:utf-8
@Author:大轩
"""
import time

import pytest


# @pytest.fixture(scope='class', autouse=True)
# def login():
#     print("登录")
#     username = 'testname'
#     token = 'testtoken'
#     yield username, token
#     print("登出")
def pytest_collection_modifyitems(items) -> None:
    """
    用例中文ids转码
    """
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")


# 根据日期动态生成日志文件名称
@pytest.fixture(scope="session", autouse=True)
def manage_logs(request):
    """Set log file name same as test name"""
    now = time.strftime("%Y-%m-%d %H-%M-%S")
    log_name = 'output/log/' + now + '.logs'

    request.config.pluginmanager.get_plugin("logging-plugin").set_log_path(log_name)
