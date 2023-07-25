import configparser

config = configparser.ConfigParser()
config.read('TestFile/my.ini', encoding='utf-8')

# 1.获取所有的节点
result = config.sections()
print(result)

# 2.获取节点下的键值
result1 = config.items('ip')
print(result1)

# 3.获取某个节点下的键对应的值
result2 = config.get('ip', 'ip')
print(result2)

# 4.其他功能
# 4.1 是否存在节点
v1 = config.has_section('world')
print(v1)

# 4.2增加一个节点
# config.add_section('group')  # 添加节点，仅仅是写入缓存，并未写入文件
config.set('group', 'name', 'hello1')  # 添加键值对
config.set('ip', 'name', 'hello')  # 添加键值对
config.write(open('TestFile/my.ini', mode='w', encoding='utf-8'))

# 4.3删除
config.remove_section('group')
config.remove_option('ip', 'name')
config.write(open('TestFile/my.ini', mode='w', encoding='utf-8'))

