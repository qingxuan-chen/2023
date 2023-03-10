import urllib3
import json


def test_HTTP():
    # 创建线程池
    pm = urllib3.PoolManager()
    url = "http://httpbin.org/get"
    headers = {'school': 'Test'}
    fields = {'school': 'test'}
    resp = pm.request(method='GET', url=url, headers=headers, fields=fields)
    # print(type(resp))
    # print(resp.status)
    # print(resp.headers)
    # print(resp.data)
    content = resp.data.decode('utf-8')
    print(content)
    obj = json.loads(content)
    print(obj)
    print(obj['headers'])
