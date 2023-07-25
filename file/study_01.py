import os

# 读文本内容
# 打开文件
file_object = open('../info', mode='rt', encoding='utf-8')  # rb读取二进制，rt读取文本
# 读取内容
data = file_object.read()
# 关闭文件
file_object.close()

print(data)
# 内容解码
# text = data.decode('utf-8')
# print(text)


# 判断路径是否存在
exists = os.path.exists('../info')
print(exists)

# 写文件
file_object1 = open('../info', mode='wb')  # wb要求写入内容是字节 wt写入文本内容 
# 写入内容
file_object1.write('开开心心'.encode('utf-8'))  # 首先写入系统缓冲区，定时刷新至文件中，并非实时
# f.flush()将缓存立即刷新至文件中
file_object1.flush()  # 将缓存立即刷新至文件中
file_object1.close()



