import math

print(math.pi)
print(math.e)
print(math.nan)


class TestDemo1:
    def setup(self):
        print("begin")

    def teardown(self):
        print("stop")

    def test_case1(self):
        print("这是测试内容1")

    def test_case2(self):
        print("这是测试内容2")