import shutil

# 压缩文件
"""
base_name 压缩后的压缩文件
format 压缩的格式
root_dir 要压缩的文件路径
"""
# shutil.make_archive(base_name=r'datafile', format='zip', root_dir=r'TestFile')

# 解压文件
"""
filename 要解压的压缩包文件
extract_dir 解压的路径
format 压缩的文件格式
"""
shutil.unpack_archive(filename='datafile.zip', extract_dir=r'xxxxx', format='zip')
