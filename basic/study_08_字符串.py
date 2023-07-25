# v独有；x公共

v1 = '这一天天的，真烦呀'
# startswith判断字符串以***开始，返回布尔类型
# endswith判断字符串以***结束，返回布尔类型
v1_result1 = v1.startswith('这一天天的')
v1_result2 = v1.endswith('哈哈哈')
print(v1_result1)
print(v1_result2)

v2 = '123456'
# isdecimal判断字符串是否为数值；isdigit也可判断，但范围太广，不适合
v2_result1 = v2.isdecimal()
print(v2_result1)

v3 = '  好开心啊   '
# strip去除字符串两边的空格，换行符（/n），制表符（/t），得到一个新的字符串
v3_result1 = v3.strip()
print(v3_result1)
v3_result2 = v3.lstrip()
v3_result3 = v3.rstrip()
print(v3_result2 + "," + v3_result3)
# 去除指定内容  strip("****")

v4 = 'my name is Mekio'
# upper 使全部英文变成大写
v4_result1 = v4.upper()
print(v4_result1)
# lower，英文变小写
v4_result2 = v4.lower()
print(v4_result2)

v5 = '我今天好开心啊！'
# replace字符串指定内容的替换
v5_result = v5.replace('开心', '生气')
print(v5_result)

v6 = '开心|ha|156|com'
# split 字符串切割，生成切割后的列表
v6_result1 = v6.split('|')
# split('', 2)，从左开始，切几次
v6_result2 = v6.split('|', 2)
# rsplit 从右开始切割
v6_result3 = v6.rsplit('|', 2)
print(v6_result1)
print(v6_result2)
print(v6_result3)

data_list = ['我', '是', '大帅哥']
# join 字符串的拼接
v7 = '0'.join(data_list)
print(v7)

v8 = '嫂子'
# encode 字符串转换为字节类型
v8_result1 = v8.encode('utf-8')  # b'\xe5\xab\x82\xe5\xad\x90'
v8_result2 = v8.encode('gbk')  # b'\xc9\xa9\xd7\xd3'
print(v8_result1)
print(v8_result2)
# decode 字节类型转换为字符串
v8_result3 = v8_result1.decode('utf-8')
print(v8_result3)

v9 = '张老汉'
# center(总长,'填充内容')居中显示
v9_result1 = v9.center(20, '*')
print(v9_result1)
# ljust()居左显示 rjust()居右显示
v9_result2 = v9.ljust(20, '*')
print(v9_result2)

v10 = '1010'
# zfill 用0填充至多少位
v10_result = v10.zfill(10)
print(v10_result)

print('*' * 20)

x1 = '开心' + '每一天'
print(x1)

x2 = 'hello'
print(x2 * 5)

x3 = '开心每一天，开开心心快快乐乐'
x3_result = len(x3)
print(x3_result)

# 切片[头:尾:步长]前取后不取
x3_result1 = x3[0:2]
print(x3_result1)
x3_result2 = x3[3:-1]
print(x3_result2)
x3_result3 = x3[::-1]
print(x3_result3)

# range(头:尾:步长)前取后不取创建一系列数字
# range(10)
# range(1, 5)
# range(1, 10, 2)
# range(10, 1, -1)

