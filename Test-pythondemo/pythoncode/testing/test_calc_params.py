"""
coding:utf-8
@Author:大轩
"""
import logging
from time import sleep

import allure
import pytest
import yaml

from pythoncode.coding.calculator import Calculator


def get_datas(func, level):
    with open('./datas.yml', encoding="utf-8") as f:
        result = yaml.safe_load(f)
        # print(result['add']['P0']['datas'])
        datas = result.get(func).get(level).get('datas')
        ids = result.get(func).get(level).get('ids')
    return [datas, ids]


@pytest.fixture(scope='class')
def get_calc():
    print("开始测试")
    calc = Calculator()
    yield calc
    print("结束测试")


@pytest.fixture(autouse=True)
def calc_fix():
    print("开始计算")
    yield
    print("结束计算")

@allure.feature("计算器功能")
class TestCalculator:
    add_datas_P0 = get_datas('add', 'P0')[0]
    add_ids_P0 = get_datas('add', 'P0')[1]
    add_datas_P1_1 = get_datas('add', 'P1_1')[0]
    add_ids_P1_1 = get_datas('add', 'P1_1')[1]
    add_datas_P1_2 = get_datas('add', 'P1_2')[0]
    add_ids_P1_2 = get_datas('add', 'P1_2')[1]
    div_datas_P0 = get_datas('div', 'P0')[0]
    div_ids_P0 = get_datas('div', 'P0')[1]


    # def setup(self):
    #     print("开始计算")
    #
    # def teardown(self):
    #     print("结束计算")
    #
    # def setup_class(self):
    #     print("开始测试")
    #     self.calc = Calculator()
    #
    # def teardown_class(self):
    #     print("测试结束")

    @pytest.mark.run(order=2)
    @pytest.mark.p0
    @pytest.mark.parametrize('a, b, expect', add_datas_P0, ids=add_ids_P0)
    @allure.story("加法功能")
    def test_add0(self, get_calc, a, b, expect):
        sleep(1)
        # calc = Calculator()
        # result = self.calc.add(a, b)
        with allure.step("相加操作"):
            result = get_calc.add(a, b)
        with allure.step("验证结果"):
            assert result == expect
        logging.info(f"参数：{a}, {b}, 期望结果：{expect}")
        logging.info(f"结果：{result}")

    @pytest.mark.run(order=1)
    @pytest.mark.p1
    @pytest.mark.parametrize('a, b, errortype', add_datas_P1_2, ids=add_ids_P1_2)
    @allure.story("加法功能")
    def test_add1(self, get_calc, a, b, errortype):
        sleep(1)
        with pytest.raises(eval(errortype)) as e:
            # result = self.calc.add(a, b)
            result = get_calc.add(a, b)
        logging.info(f"参数：{a}, {b}")
        # logging.info(f"结果：{result}")


    @pytest.mark.p0
    @pytest.mark.parametrize('a, b, expect', div_datas_P0, ids=div_ids_P0)
    @allure.story("除法功能")
    def test_div(self, get_calc, a, b, expect):
        sleep(1)
        result = get_calc.div(a, b)
        allure.attach.file("./image/test.jpg", name="截图", attachment_type=allure.attachment_type.JPG, extension=".jpg")
        assert result == expect
        logging.info(f"参数：{a}, {b}, 期望结果：{expect}")
        logging.info(f"结果：{result}")
