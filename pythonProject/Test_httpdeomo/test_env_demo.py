"""
coding:utf-8
@Author:大轩
"""
import os

import requests
import yaml


class TestEnv:
    def setup_class(self):
        # self.base_url = "https://www.baidu.com/"
        path_env = os.getenv("interface_env", default='test')
        env = yaml.safe_load(open(f"{path_env}.yml", encoding='utf-8'))
        self.base_url = env["base_url"]

    def test_testenv(self):
        r = requests.get(self.base_url)
        print(r.text)

    def test_devenv(self):
        r = requests.get(self.base_url)
        print(r.text)
