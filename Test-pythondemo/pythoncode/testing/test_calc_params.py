"""
coding:utf-8
@Author:大轩
"""
import pytest
import yaml

from pythoncode.coding.calculator import Calculator


def get_datas(level):
    with open('./datas.yml', encoding="utf-8") as f:
        result = yaml.safe_load(f)
        # print(result['add']['P0']['datas'])
        add_datas = result.get('add').get(level).get('datas')
        add_ids = result.get('add').get(level).get('ids')
    return [add_datas, add_ids]


class TestCalculator:
    add_datas_P0 = get_datas('P0')[0]
    add_ids_P0 = get_datas('P0')[1]
    add_datas_P1_1 = get_datas('P1_1')[0]
    add_ids_P1_1 = get_datas('P1_1')[1]
    add_datas_P1_2 = get_datas('P1_2')[0]
    add_ids_P1_2 = get_datas('P1_2')[1]

    def setup(self):
        print("开始计算")

    def teardown(self):
        print("结束计算")

    def setup_class(self):
        print("开始测试")
        self.calc = Calculator()

    def teardown_class(self):
        print("测试结束")

    @pytest.mark.run(order=2)
    @pytest.mark.p0
    @pytest.mark.parametrize('a, b,expect', add_datas_P0, ids=add_ids_P0)
    def test_add0(self, a, b, expect):
        # calc = Calculator()
        result = self.calc.add(a, b)
        assert result == expect

    @pytest.mark.run(order=1)
    @pytest.mark.p1
    @pytest.mark.parametrize('a, b, errortype', add_datas_P1_2, ids=add_ids_P1_2)
    def test_add1(self, a, b, errortype):
        with pytest.raises(eval(errortype)) as e:
            result = self.calc.add(a, b)
