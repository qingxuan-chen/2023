import datetime

nowtime = datetime.datetime.now()

# print(nowtime)
# print(nowtime.day)
# print(nowtime.month)
# print(nowtime.year)
# print(nowtime.timestamp())
# result = nowtime.strftime('%A %B %d %H %M')
# print(result)
# s = '2023-03-03 16:45:35'
# s1 = datetime.datetime.strptime(s, '%Y-%m-%d %H:%M:%S')
# print(s1)
# s2 = nowtime.timestamp()
# print(s2)
# s3 = datetime.datetime.fromtimestamp(s2)
# print(s3)

str_time = datetime.datetime.strftime(nowtime, '%Y%m%d_%H%M%S')
# print(str_time)
log_name = str_time + '.log'
with open(log_name, 'w+', encoding='utf-8') as f:
    # datetime [level] line: 11 this is a log message
    message = f"{nowtime} [info] line: 12 this is a message"
    f.write(message)
