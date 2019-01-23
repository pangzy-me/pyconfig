'''
  基本的读取操作：
    -read(filename)         直接读取文件内容
    -sections()             得到所有的section，并以列表的形式返回
    -options(section)       得到该section的所有option
    -items(section)         得到该section的所有键值对
    -get(section,option)    得到section中option的值，返回为string类型
    -getint(section,option) 得到section中option的值，返回为int类型，还有相应的getboolean()和getfloat()函数

  基本的写入操作：
    -write(fp)                  将config对象写入至某个 .init 格式的文件
                                Write an .ini-format representation of the configuration state.
    -add_section(section)       添加一个新的section
    -set(section,option,value   对section中的option进行设置，需要调用write将内容写入配置文件
    -remove_section(section)    删除某个 section
    -remove_option(section,option)
'''
# 读操作
import configparser
#
# cf = configparser.ConfigParser()
# cf.read("config.ini")
#
# print(cf.sections())
# print(cf.options('config'))
# print(cf.items('config'))
# print(cf.get("config","explorer"))
# print(cf.get("database","url"))

# 写操作
cf = configparser.ConfigParser()
cf.read("config.ini", encoding="utf-8")

# 修改section中key对应的value值
cf.set("config", "host", "127.1.1.1") #使用set直接修改指定字段值
with open('config.ini', "w+") as fw:
    cf.write(fw)  # 使用write将修改内容写到文件中，替换原来config文件中内容

# 删除某个section
# cf.remove_section('config')
# with open('config.ini', "w") as fw:
#     cf.write(fw) # 使用write将修改内容写到文件中，替换原来config文件中内容






# 使用with自动关闭文件
# a = 'hello'
# with open('config.ini','w') as fout:
#     fout.write(a)
