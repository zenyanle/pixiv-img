import requests as req
#import bs4
#from pprint import pprint
import re
import random

headers={
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'
}

def url_get(content):
    findlink3 = re.compile(r'data-src="(.*?)"')
    link3 = re.findall(findlink3, content)

    i = 0
    for name in link3:
        i += 1
        img_url = 'https://imeizi.me' + name
        img = req.get(img_url)
    #    f = open(f'{str(i)}.jpg','wb')
    #    f.write(img.content)
    #    f.close()

        try:
            with open(f'{many}_{i}.jpg', 'wb') as file:
                file.write(img.content)
        except Exception:
            continue
        print('正在下载第', i, '张图片')

while True:
    many = random.randint(1000,9200)
    res = req.get(f'https://imeizi.me/article/{many}/',headers=headers)
    try:
        res.raise_for_status()
        print(f'将要下载的图片编号为{many}')
        url_get(res.text)
    except Exception:
        print('404')
        continue
