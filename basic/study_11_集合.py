# 集合无序，无法通过索引取值
# 可变，可以添加/删除元素
# 不允许重复
# 定义空集合：v = set{}
# int/list/tuple/dict 都可以转换为集合
# 存储原理：利用哈希函数将元素转换为数值》》取余数》》将元素放入哈希表中  （元素必须是可哈希的）
# int/bool/str/tuple是可哈希的，list/set不可哈希：集合的元素只能是int/bool/str/tuple
set1 = {11, 22, 'ajax'}

# 添加
set1.add(999)
print(set1)

# 删除
set1.discard(11)
print(set1)

s1 = {'刘能', '赵四', '张德柱'}
s2 = {'刘能', '赵四', '哈哈哈'}
# 交集
s3 = s1 & s2
# s3 = s1.intersection(s2)   同上
print(s3)

# 并集
s4 = s1 | s2
# s4 = s1.union(s2)  同上
print(s4)

# 差集
s5 = s1 - s2
# s5 = s1.difference(s2)  同上
print(s5)
