import requests as re
import json
import time

n = 1
while True:
    res = re.get('https://api.lolicon.app/setu/v2?proxy=api.pixiv.moe/image/i.pximg.net/')
    res.raise_for_status()
    pdata = json.loads(res.text)

    geshi = pdata['data'][0]['ext']
    name = pdata['data'][0]['title']
    d = pdata['data'][0]['urls']['original']
    print('将要下载的地址是',d)

    imgr = re.get(d)
    imgr.raise_for_status()
    img = imgr.content

    with open(f'{name}.{geshi}', 'wb') as file:
        file.write(imgr.content)

    time.sleep(3)
    n += 1
    print(f"正在开始第{n}次下载")
