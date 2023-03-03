import datetime

nowtime = datetime.datetime.now()
print(nowtime)
print(nowtime.day)
print(nowtime.month)
print(nowtime.year)
print(nowtime.timestamp())

result = nowtime.strftime('%A %B %d %H %M')
print(result)

s = '2023-03-03 16:45:35'
s1 = datetime.datetime.strptime(s, '%Y-%m-%d %H:%M:%S')
print(s1)