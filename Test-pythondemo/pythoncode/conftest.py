"""
coding:utf-8
@Author:大轩
"""
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