class Human:
    # 类属性
    message = “这是类属性”
    population = 0

    # 构造方法
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("这是构造方法")

    # 类方法  @classmethod装饰  参数cls
    @classmethod
    def bron(cls):
        print("这是类方法")
        cls.population += 1

    # 实例方法
    def study(self, course):
        print(f"正在学习{course}")

    # 静态方法
    @staticmethod
    def grow_up():
        print("这是静态方法")


person = Human("大轩", 35)
