import random
import pytest


# sum1 = 0
# for i in range(0, 101, 2):
#     sum1 = sum1 + i
# print(sum1)

# i = 0
# while i <= 100:
#     sum1 = sum1 + i
#     i += 1
# print(sum1)

# c_num = random.randint(1, 10)
# while True:
#     p_num = int(input("请输入数字： "))
#
#     if p_num > c_num:
#         print("太大了")
#     elif p_num < c_num:
#         print("太小了")
#     else:
#         print("猜对了,游戏结束")
#         break

# result = []
# for i in range(1, 11):
#     if i % 2 == 0:
#         result.append(i**2)
# print(result)

# result = [i**2 for i in range(1, 11) if i % 2 == 0]
# print(result)

# tuple1 = (1, )
# print(type(tuple1), tuple1)
# tuple2 = tuple('testmessage')
# print(tuple2)

# dict1 = {k: v for k, v in [('name', 'chen'), ('age', 18)]}
# print(dict1)
#
# dict2 = {'a': 1, 'b': 2, 'c': 3, 'd': 3}
# print(dict2.items())
# dict3 = {k: v **2 for k, v in dict2.items() if v >1}
# print(dict3)
# dict4 = {v: k for k, v in dict2.items()}
# print(dict4)

def setup_module():
    print('全局模块——开始')


def teardown_module():
    print('全局模块——结束')


# def setup_class():
#     print('类模块——开始')
#
#
# def teardown_class():
#     print('类模块——结束')


# def teardown_function():
#     print('方法——结束')
#
#
# def setup_function():
#     print('方法——开始')


class TestDemo1:

    def setup_class(self):
        print('类模块——开始')

    def teardown_class(self):
        print('类模块——结束')

    def teardown(self):
        print('方法——结束')

    def setup(self):
        print('方法——开始')

    def test_func(self):
        a = 1
        b = 2
        expect = 3
        assert a + b == expect, '测试结果'

    def test_func2(self):
        print('case2')


class TestDemo2:

    def test_func3(self):
        a = 1
        b = 2
        expect = 3
        assert a + b == expect, '测试结果'

    def test_func4(self):
        print('case2')


namelist = ['name1', 'name2', 'name3']


@pytest.mark.parametrize('name', namelist, ids=['第一', '第二', '第三'])
def test_name(name):
    print(f"名字是{name}")


@pytest.mark.parametrize('test_input, expected', [('1+2', 3), ('3+4', 8), ('5+6', 11)])
def test_mark_more(test_input, expected):
    assert eval(test_input) == expected


@pytest.mark.parametrize('name', ['小明', '小红', '大壮'])
@pytest.mark.parametrize('food', ['面条', '米饭', '屎'])
@pytest.mark.food
def test_dkej(name, food):
    print(f"{name}喜欢{food}")
