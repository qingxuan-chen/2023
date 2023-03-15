"""
coding:utf-8
@Author:大轩
"""
import requests
import xmltodict
from jsonpath import jsonpath


class TestDemo:
    def test_get(self):
        r = requests.get('https://httpbin.ceshiren.com/get')
        print(r.json())
        print(r.status_code)
        print(r.text)
        assert r.status_code == 200

    def test_query(self):
        payload = {
            "name": 'testname',
            "password": '123456a'
        }
        r = requests.get('https://httpbin.ceshiren.com/get', params=payload)
        print(r.text)
        assert r.status_code == 200

    def test_post_form(self):
        payload = {
            "name": 'testname',
            "password": '123456a'
        }
        r = requests.post('https://httpbin.ceshiren.com/post', data=payload)
        print(r.text)
        assert r.status_code == 200

    def test_header(self):
        r = requests.get('https://httpbin.ceshiren.com/get', headers={"h": "header_demo"})
        print(r.json())
        print(r.status_code)
        print(r.text)
        assert r.status_code == 200
        assert r.json()['headers']['H'] == "header_demo"

    def test_post_json(self):
        payload = {
            "name": 'testname',
            "password": '123456a'
        }
        r = requests.post('https://httpbin.ceshiren.com/post', json=payload)
        print(r.text)
        assert r.status_code == 200
        assert r.json()['json']['name'] == 'testname'

    def test_hogwars_json(self):
        r = requests.get('https://ceshiren.com/categories.json')
        # print(r.json())
        print(r.status_code)
        print(r.text)
        # assert r.status_code == 200
        # assert r.json()['category_list']['categories'][0]['name'] == '提问区'
        assert jsonpath(r.json(), '$..name')[0] == '提问区'
        print(jsonpath(r.json(), '$..name'))

    def test_cookies(self):
        headers = {
            # "Cookie": "hogwarts=school",
            'User-Agent': 'hogwarts'
        }
        cookie_data = {
            'hogwarts': 'school',
            'teacher': 'TEST'
        }
        r = requests.get('https://httpbin.ceshiren.com/cookies', headers=headers, cookies=cookie_data, timeout=3)
        print(r.request.headers)
        assert jsonpath(r.json(), 'cookies')[0] == {'hogwarts': 'school', 'teacher': 'TEST'}

    def test_case1(self):
        r = requests.get("https://www.baidu.com/")
        print(r.text)
        # print(xmltodict.parse(r.text))
