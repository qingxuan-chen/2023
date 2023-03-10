import yaml

# data = {
#     "client": {"default-character-set": "utf-8"},
#     "mysql": {"user": 'root', "password": 123456},
#     "custom": {
#         "user1": {"user": "张三", "pwd": 666},
#         "user2": {"user": "李四", "pwd": 999}
#     }
# }
#
#
# with open('my.yml', 'w', encoding='utf-8') as f:
#     yaml.dump(data, f, allow_unicode= True)


with open('my.yml', 'r', encoding='utf-8') as f:
    data2 = yaml.safe_load(f)
    print(data2)
