# 字典无序，键不重复，且元素只能是键值对的可变的容器
# python3.6+的字典就是有序了，之前的都是无序的
# 键：必须可哈希  int/bool/str/tuple；值可为任意类型

info = {'name': '张三', 'age': 22, 'pwd': 666666}
# 获取值
data1 = info.get('name')
data2 = info.get('用户名')  # 键不存在，默认返回none
print(data1)
print(data2)
data3 = info.get('住址', 666)
print(data3)  # 键不存在，不返回none，返回666

# 获取所有的键
data4 = info.keys()  # python2中，keys()直接获取的是列表，python3中返回的是高仿列表
print(data4)

# 获取所有的值
data5 = info.values()  # python2中，keys()直接获取的是列表，python3中返回的是高仿列表
print(data5)

# 获取所有的键值对
data6 = info.items()
print(data6)

# 设置值 setdefault(键,值) 若键不存在，设置新的键值对，若键存在，则不设置
info.setdefault('颜色', 'blue')
print(info)
info.setdefault('name', 'hello')
print(info)

# 更新键值对 update 键不存在直接添加，键存在则更新
info.update({'大小': 12, 'name': '李四'})
print(info)

# 移除键值对 pop
data7 = info.pop('颜色')
print(info)
print(data7)

# 按顺序移除（先进先出）popitem:python3.6之后，移除最后的值，之前随机删除
data8 = info.popitem()
print(info)
print(data8)

# 转换为字典
v = dict([{'k1', 'v1'}])
print(v)

