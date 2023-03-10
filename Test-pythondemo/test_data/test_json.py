import json

data1 = {
    'a': '中文字符',
    'b': ['2', '3'],
    'c': True,
    'd': False,
    'e': None
}
# 转换为json格式
json_data1 = json.dumps(data1, ensure_ascii=False)
print(json_data1)
print(type(json_data1))

# 转换为Python对象
data2 = json.loads(json_data1)
print(data2)
print(type(data2))

# 将数据写入json文件
with open('data2.json', 'w', encoding='utf-8') as f:
    json.dump(data2, f)

# 读取json文件，并转换为Python对象
with open('data2.json', 'r') as f:
    data3 = json.load(f)
    print(data3)
    print(type(data3))