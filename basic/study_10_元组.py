# 只有字符串和列表可以转换为元组
# 元组不可修改，但元组内部嵌套的列表可以修改
tuple1 = ('123', 666, [11, 22, 33], ('alax', 'zhangsan', [999, 666, (66, 55, 99)]))
tuple1[2][0] = 99
print(tuple1)
tuple1[3][2].pop()
print(tuple1)
