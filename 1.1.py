import requests
import os
url = 'https://www.nationalgeographic.com/content/dam/expeditions/landing-pages/North-America/hero-national-parks2.adapt.1900.1.jpg'
root = 'D://pics//'
path = root + url.split('/')[-1]
# try:
if not os.path.exists(root):
    os.makedirs(root)
if not os.path.exists(path):
    r = requests.get(url)
    r.raise_for_status()
    with open(path,'wb') as f:
        f.write(r.content)
        f.close()
        print('文件保存成功')
    print(r.status_code)
    print(r.encoding)
    print(r.apparent_encoding)
    r.encoding = r.apparent_encoding
else:
    print('文件已存在')
# except:
#     print('爬取错误')