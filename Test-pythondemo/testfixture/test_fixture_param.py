"""
coding:utf-8
@Author:大轩
"""
import logging

import pytest


@pytest.fixture(params=['name1', 'name2', 'name3'])
def login(request):
    print(f"用户名是:{request.param}")
    yield request.param


def test_demo1(login):
    logging.info("这是一条测试日志信息")
    print(f"demo1 case数据是{login}")