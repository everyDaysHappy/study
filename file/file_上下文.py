f = open('../info', mode='rb')
data = f.read()
print(data)
f.close()

# with f 自动关闭文件
with open('../info', mode='rt', encoding='utf-8') as f:
    data1 = f.read()
    print(data1)

# 支持打开多个文件
# with open('../info', mode='rt', encoding='utf-8') as f1, open('../info', mode='rt', encoding='utf-8') as f2:
#     pass

