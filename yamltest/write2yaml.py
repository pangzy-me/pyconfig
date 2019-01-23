'''
    yaml文件写入(ruamel.yaml)
    https://www.cnblogs.com/yoyoketang/p/9255109.html
'''
import os
from ruamel import yaml
from pprint import pprint

# 将字典写入到yaml
desired_caps = {
                'platformName': 'Android',
                'platformVersion': '7.0',
                'unicodeKeyboard': True,
                'resetKeyboard': None,
                'noReset': True,
                'chromeOptions': {'androidProcess': 'com.tencent.mm:tools'},
                'listHASdict': [{'admin1': 11111, 'name': '列表中的字典1'},
                                {'admin2': 22222, 'name': '列表中的字典2'},
                                {'admin3': 33333, 'name': '列表中的字典3'}],
                }
curpath = os.path.dirname(os.path.realpath(__file__))
yamlpath = os.path.join(curpath, "write2yaml.yaml")

with open(yamlpath, "w", encoding="utf-8") as f:
    yaml.dump(desired_caps, f, Dumper=yaml.RoundTripDumper)

fopen = open(yamlpath, "r")
pprint(yaml.load(fopen.read(), Loader=yaml.Loader))
