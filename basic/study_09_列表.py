list1 = ['*']
# append 在列表尾部添加元素
name = 'zhangsan'
list1.append(name)
print(list1)

# extend 批量追加，将一个列表的元素添加到另一个列表中
tools = ['菜刀', '案板', '碗']
list2 = ['***']
list2.extend(tools)
print(list2)

# insert 插入：在指定索引处插入值
list3 = ['*', 123, 'hello']
list3.insert(1, 'int')
print(list3)

# remove 删除：从左至右，找到第一个删除(删除的数据不存在，就会报错)
list4 = ['*', 123, 'hello']
list4.remove(123)
print(list4)

# pop 根据索引删除，默认删除最后一个,可将删除的值赋给其他
list5 = ['*', 'int', 123, 'hello']
item = list5.pop(2)
print(list5, item)

# clear 清空列表
list6 = ['*', 123, 'hello']
list6.clear()
print(list6)

# index 根据值获取索引(列表中无值，会报错)
list7 = ['*', 'int', 123, 'hello']
x = list7.index(123)
print(x)

# sort 数字排序:默认从小到大排序
list8 = [12, 34, 5, 7, 62, 10]
# list8.sort()  从小到大排序
list8.sort(reverse=True)  # 从大到小排序
# list8.sort(key=函数)
print(list8)

# reverse 列表数据反转
list9 = ['*', 'int', 123, 'hello']
list9.reverse()
print(list9)

print('*'*20)

data = ['张三', '里斯'] + [1, 2, 3]
print(data)

data1 = ['张三', '里斯'] * 3
print(data1)

name1 = '张三丰'
name_list = list(name1)
print(name_list)