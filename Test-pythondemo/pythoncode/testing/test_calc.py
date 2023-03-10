"""
coding:utf-8
@Author:大轩
"""
import pytest

from pythoncode.coding.calculator import Calculator


class TestCalculator:
    def setup(self):
        print("开始计算")

    def teardown(self):
        print("结束计算")

    def setup_class(self):
        print("开始测试")
        self.calc = Calculator()

    def teardown_class(self):
        print("测试结束")

    @pytest.mark.p0
    @pytest.mark.parametrize('a, b ,expect', [(1, 2, 3), (-1, -2, -3), (0.01, 0.02, 0.03)],
                             ids=('整数', '负数', '小数'))
    def test_add0(self, a, b, expect):
        # calc = Calculator()
        result = self.calc.add(a, b)
        assert result == expect

    @pytest.mark.p1
    @pytest.mark.parametrize('a, b ,expect', [(1, 100, "参数大小超出范围"), (-100, -2, "参数大小超出范围"), (-100.001, 0.02, "参数大小超出范围")],
                             ids=('越界1', '越界2', '越界3'))
    def test_add1(self, a, b, expect):
        # calc = Calculator()
        result = self.calc.add(a, b)
        assert result == expect

    @pytest.mark.p1
    @pytest.mark.parametrize('a, b ,errortype', [(1, "数字", TypeError), (-5, 'abc', TypeError), (' ', 0.02, TypeError)],
                             ids=('中文', '字符', '空格'))
    def test_add1(self, a, b, errortype):
        with pytest.raises(errortype) as e :
            result = self.calc.add(a, b)

    @pytest.mark.p0
    def test_div0(self):
        # calc = Calculator()
        result = self.calc.div(6, 2)
        assert result == 3
