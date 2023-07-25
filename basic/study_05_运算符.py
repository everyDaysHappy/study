# and逻辑：先判断前面，前面为真，取决于and后，输出 and后
v1 = 'hahaha' and 'world'
print(v1)  # 输出为world

# and逻辑：前面为假，无须判断后面，直接输出 and前
v2 = '' and 'world'
print(v2)  # 输出为空

# or逻辑
v3 = 1 or 3
print(v3)  # 1

v4 = '' or 'hello'
print(v4)  # hello

# 先计算not，在计算and，最后计算or
test1 = 0 or 4 and 3 or 7 and 6
test2 = 8 or 3 and 4 or 2 and 0 or 9 and 7
test3 = 0 or 2 and 3 and 4 or 6 and 0 or 3
test4 = not 8 or 3 and 4 or 2
print('csvTest={},test2={},test3={},test4={}'.format(test1, test2, test3, test4))
