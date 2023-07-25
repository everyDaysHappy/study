import os

file_object = open('../info', mode='r+')
# seek 移动到指定字节处
# file_object.seek(4)

file_object.write('abcd')

file_object.close()


# f.tell()获取现在光标所在位置
file_object1 = open('../info', mode='r+')

p1 = file_object1.tell()
print(p1)

file_object1.read(3)

p2 = file_object1.tell()
print(p2)

file_object1.close()

