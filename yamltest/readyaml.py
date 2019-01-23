# import yaml
from ruamel import yaml
import os
from pprint import pprint

'''
yaml基本语法规则：
    大小写敏感
    使用缩进表示层级关系
    缩进时不允许使用Tab键，只允许使用空格。
    缩进的空格数目不重要，只要相同层级的元素左侧对齐即可
    #表示注释，从这个字符一直到行尾，都会被解析器忽略，这个和python的注释一样
yaml支持的数据结构有三种：
    对象：键值对的集合，又称为映射（mapping）/ 哈希（hashes） / 字典（dictionary）
    数组：一组按次序排列的值，又称为序列（sequence） / 列表（list）
    纯量（scalars）：单个的、不可再分的值。字符串、布尔值、整数、浮点数、Null、时间、日期

'''

# 获取当前脚本所在文件夹路径
curdir = os.path.dirname(os.path.realpath(__file__))
# 获取yaml文件路径
yamlpath = os.path.join(curdir, "cfgyaml.yaml")
# print(yamlpath)

fopen = open(yamlpath, 'r', encoding='utf-8')
cfg = fopen.read()
# print(type(cfg))    # 此时读取出来的类型为字符串str
# print(cfg)

dict2 = yaml.load(cfg)  # 使用load方法转字典
# print(type(dict2))    # 此时读取出来的类型为字典dict
# print(dict2)
pprint(dict2)   # 打印输出格式美化

# 取值操作
print(dict2['dictINdict'])
print(dict2['dictINdict']['user'])
print(dict2['n1'])
print(dict2['listHASdict'][1]['name2'])    # 一层字典，二层列表，三次字典取值
print(dict2['listHASdict'][1].items())

# 另一种实现方式：
# 使用ruamel.yaml模块也能读yaml文件,yaml.load方法多加一个参数：Loader=yaml.Loader
# pprint(yaml.load(fopen.read(), Loader=yaml.Loader))
