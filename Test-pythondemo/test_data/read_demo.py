# f = open('data1.txt', 'r', encoding='utf-8')
#
# print(f.read(10))
#
# f.close()
# with关键字，可以自动关闭文件
with open('data1.txt', 'a+', encoding='utf-8') as f:
    f.write('\n这是修改内容')
    print(f.read())
