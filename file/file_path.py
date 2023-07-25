import shutil
import os
"""
# 获取当前运行文件的路径
file_path = os.path.abspath(__file__)
print(file_path)

# 再往上找一级
path = os.path.dirname(file_path)
print(path)
"""

base_dir = os.path.dirname( os.path.abspath(__file__) )
# base_dir1 = os.path.dirname(__file__)
# print(base_dir1)  E:/pycharmproject3.0/study/file
print(base_dir)  # E:\pycharmproject3.0\study\file

file_path = os.path.join(base_dir, 'TestFile', 'logs')
print(file_path)

if os.path.exists(file_path):
    file_object = open(file_path, mode='r', encoding='utf-8')
    data = file_object.read()
    file_object.close()
    print(data)
else:
    print('文件不存在')

# 删除路径
# shutil.rmtree(路径)

# 拷贝文件夹
# shutil.copytree()

# 拷贝文件
# shutil.copy()

# 文件/文件夹的重命名
# shutil.move()