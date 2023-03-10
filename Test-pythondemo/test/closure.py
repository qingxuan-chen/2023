# """
# 闭包函数:霍格沃茨开学啦，要求打印每个学生的姓名、性别和年级
# """
#
#
# def student_grade(grade):
#     def print_student(name, gender):
#         print(f"霍格沃茨开学啦，学生姓名是{name}，性别是{gender}，年级是{grade}年级")
#     return print_student
#
#
# student_info = student_grade(2)
# student_info('大头', '男')

def test_demo1():
    print("这是测试函数1")


def test_demo2():
    print("这是测试函数2")


def function_tips(func):
    print("开始执行")
    func()
    print("执行完毕")


function_tips(test_demo1)
function_tips(test_demo2)
