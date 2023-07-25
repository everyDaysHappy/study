# % 占位符
name = 'zhangyu'
age = 18
# test = '我叫%s，我今年18' % name

# 多个占位
test = '我叫%s，我今年%d' % (name, age)
print(test)

# 名称占位
test1 = '%(Name)s在哪呢？今天%(day)d号' % {'Name': 'hall', 'day': 18}
print(test1)

# 输出百分号
text = '%s,快来吧，已经90%%了' % '兄弟'
print(text)

# format
format_text = '我是{}，今年{}岁了'.format('zhangy', '24')
print(format_text)

# python3.6之后新引入的  f
action = '跑步'
day1 = '明天'
f_text = f'今天好累呀，{action}不容易，{day1}继续'
f_text1 = f'今年{2+1}岁了'
print(f_text)
print(f_text1)
# 3.8引入特殊功能
f_text2 = f'今年{2 + 1 = }岁了'
print(f_text2)

# f的进制转换
v1 = f'今年{22}岁'
print(v1)

v2 = f'今年{22:#b}岁'
print(v2)

v8 = f'今年{22:#0}岁'
print(v8)

v16 = f'今年{22:#o}岁'
print(v16)




