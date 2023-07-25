"""
用户注册时，新注册的用户要写入csv文件中，输入Q/q退出
用户登录时，逐行读取csv文件中的用户信息进行校验
提示：文件路径需使用os模块构造的绝对路径的方式
"""
import os
from openpyxl import load_workbook
# 获取当前绝对路径
path = os.path.abspath(__file__)
# 返回上一级
ini_path = os.path.dirname(path)
# 构造用户信息文件路径
file_path = os.path.join(ini_path, 'Login.csv')
# 新建用户信息文件
if not os.path.exists(file_path):
    with open(file_path, mode='w', encoding='utf-8') as f:
        f.write('用户名 密码')

while True:
    print('1.注册')
    print('2.登录')
    Input = input('请输入指令（Q/q退出）：')
    if Input == '1':
        with open(file_path, mode='a', encoding='utf-8') as reg_f:
            while True:
                username = input('请输入用户名(Q/q退出)：')
                if username.upper() == 'Q':
                    break
                pwd = input('请输入密码：')
                reg_f.write('{} {}\n'.format(username, pwd))
                reg_f.flush()
                print('注册成功!')
        break

    elif Input == '2':
        with open(file_path, mode='rt', encoding='utf-8') as log_f:

            username = input('请输入用户名(Q/q退出)：')
            if username.upper() == 'Q':
                break
            pwd = input('请输入密码：')
            for line in log_f:
                user_info = line.strip().split(' ')
                if username == user_info[0] or pwd == user_info[1]:
                    print('登录成功！')
                    break
            else:
                print('用户名或密码错误！')
    elif Input.upper() == 'Q':
        print('结束')
        break
    else:
        print('无此操作，请重新选择')