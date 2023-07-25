import requests
import os
# 读取csv图片网址，并下载到本地
with open('TestFile/csvTest', mode='r', encoding='utf-8') as file_object:
    # 跳过第一行
    file_object.readline()
    for line in file_object:
        picture_name, url = line.strip().split(' ')
        re = requests.get(
            url=url,
            headers={
                'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.43'
            }
        )

        # 检查是否存在文件夹image
        if not os.path.exists('image'):
            os.makedirs('images')
        with open('images/{}.png'.format(picture_name), mode='wb') as f:
            f.write(re.content)
