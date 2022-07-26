import os, sys
import configparser

SrcRoot = r'E:\PY\PROJECT\untitled111111\JiaZ\config_ok.ini'
DstRoot = r'E:\PY\PYTHON_ENV\tongyong\dist\config_test.ini'

# configparser初始化
config = configparser.ConfigParser()
# config.read(file, encoding="utf-8")
config.read(DstRoot, encoding="utf-8-sig")


# 1. 获取节点sections
# ConfigParserObject.sections()
# 以列表形式返回configparser对象的所有节点信息
# 获取所有节点
all_sections = config.sections()
print('sections: ', all_sections)   # 结果sections:  ['user', 'connect']

# 2. 获取指定节点的的所有配置信息
# ConfigParserObject.items(section)
# 以列表形式返回某个节点section对应的所有配置信息

# 获取指定节点的配置信息
items = config.items('user')
print(items)            # 结果 [('user_name', "'Mr,X'"), ('password', "'222'")]

# 3. 获取指定节点的options
# ConfigParserObject.options(section)
# 以列表形式返回某个节点section的所有key值

# 获取指定节点的options信息
options = config.options('user')
print(options)          # 结果 ['user_name', 'password']

# 4. 获取指定节点下指定option的值
# ConfigParserObject.get(section, option)
# 返回结果是字符串类型
# ConfigParserObject.getint(section, option)
# 返回结果是int类型
# ConfigParserObject.getboolean(section, option)
# 返回结果是bool类型
# ConfigParserObject.getfloat(section, option)
# 返回结果是float类型

# 获取指定节点指定option的值
name = config.get('user', 'user_name')
print(name, type(name))            # 结果 'Mr,X' <class 'str'>

port = config.getint('connect', 'port')
print(port, type(port))           # 结果  4723 <class 'int'>
input('--'*10)
# 5. 检查section或option是否存在
# ConfigParserObject.has_section(section)
# ConfigParserObject.has_option(section, option)
# 返回bool值，若存在返回True，不存在返回False
# 检查section是否存在
result = config.has_section('user')
print(result)   # 结果 True
result = config.has_section('user1')
print(result)   # 结果 False

# 检查option是否存在
result = config.has_option('user', 'user_name')
print(result)   # 结果 True
result = config.has_option('user', 'user_name1')
print(result)   # 结果 False
result = config.has_option('user1', 'user_name')
print(result)   # 结果 False

# 6. 添加section
# ConfigParserObject.add_section(section)
# 如果section不存在，则添加节点section；
# 若section已存在，再执行add操作会报错configparser.DuplicateSectionError: Section XX already exists
# 添加section
if not config.has_section('remark'):
    config.add_section('remark')
config.set('remark', 'info', 'ok')
config.write(open(DstRoot, 'w'))
remark = config.items('remark')
print(remark)    # 结果 [('info', 'ok')]

# 7. 修改或添加指定节点下指定option的值
# ConfigParserObject.set(section, option, value)
# 若option存在，则会替换之前option的值为value；
# 若option不存在，则会创建optiion并赋值为value

# 修改指定option的值
config.set('user', 'user_name', 'Mr L')
config.set('user', 'isRemember', 'True')
config.write(open(DstRoot, 'w'))
# 重新查看修改后节点信息
items = config.items('user')
print(items)    # 结果 [('user_name', 'Mr L'), ('password', '222'), ('isremember', 'True')]


# 8.删除section或option
# ConfigParserObject.remove_section(section)
# 若section存在，执行删除操作；
# 若section不存在，则不会执行任何操作
# ConfigParserObject.remove_option(section, option)
# 若option存在，执行删除操作；
# 若option不存在，则不会执行任何操作；
# 若section不存在，则会报错configparser.NoSectionError: No section: XXX  ###实际没有报错###
# 删除section
config.remove_section('remark')         # section存在
config.remove_section('no_section111')     # section不存在

# 删除option
config.remove_option('user', 'isremember')  # option存在
config.remove_option('user', 'no_option')   # option不存在
config.write(open(DstRoot, 'w'))

all_sections = config.sections()
print(all_sections)     # 结果 ['user', 'connect']
options = config.options('user')
print(options)      # 结果 ['user_name', 'password']

# 9.写入内容
# ConfigParserObject.write(open(DstRoot, 'w'))
# 对configparser对象执行的一些修改操作，必须重新写回到文件才可生效
config.write(open(DstRoot, 'w'))

# 作者：rr1990
# 链接：https://www.jianshu.com/p/417738fc9960
# 来源：简书
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。