import requests as re
import json
import time

domain = str(input("输入你反代的域名："))

while True:
    res = re.get(f'https://api.lolicon.app/setu/v2?proxy={domain}&r18=0')
    res.raise_for_status()
    pdata = json.loads(res.text)

    geshi = pdata['data'][0]['ext']
    name = pdata['data'][0]['title']
    d = pdata['data'][0]['urls']['original']
    print('将要下载的地址是',d)

    imgr = re.get(d)
    imgr.raise_for_status()

    pfile = open(f'{name}.{geshi}', 'wb')
    pfile.write(imgr.content)
    pfile.close()


    ans = str(input('完毕，继续按y\n'))
    if ans == 'y':
        time.sleep(1)
        continue
    else:
        break

input('回车退出')
