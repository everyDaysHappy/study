# 转换后为字符串
v1 = bin(22)  # 十进制转换为二进制
v2 = oct(22)  # 十进制转换为八进制
v3 = hex(22)  # 十进制转换为十六进制
print('22的二进制：{}、八进制：{}、十六进制：{}'.format(v1, v2, v3))

# 转换为十进制
x1 = int('10110', base=2)
x2 = int('26', base=8)
x3 = int('16', base=16)
print(x1, x2, x3)