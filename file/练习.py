# 日志计数
ip = '22.99.85.66'
total_count = 0
with open('TestFile/logs', mode='r', encoding='utf-8') as file_object:
    # 遍历每一行
    for line in file_object:
        if not line.startswith(ip):
            continue
        total_count += 1
print(total_count)


# 日志升级版
user_dict = {}
with open('TestFile/logs', mode='r', encoding='utf-8') as file_object:
    for line in file_object:
        user_ip = line.split(' ')[0]
        if user_ip in user_dict:
            user_dict[user_ip] += 1
        else:
            user_dict[user_ip] = 1
print(user_dict)

# 按要求修改文件内容
# 同时打开两个文件，边读编写
with open('TestFile/logs', mode='r', encoding='utf-8') as read_file, open('./new_logs', mode='w', encoding='utf-8') as write_file:
    for line in read_file:
        new_line = line.replace('99', '456')
        write_file.write(new_line)

# 重命名
# import shutil
# shutil.move('./new_logs', './python_logs')