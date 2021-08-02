import requests
import re
import os
def main():
    print('-----美女壁纸-----')
    print('1.性感美女')
    print('2.清纯美女')
    print('3.丝袜美女')
    print('4.美腿美女')
    print('5.美胸美女')
    print('6.Cosplay')
    print('7.制服诱惑')
    print('----请选择----')
headers={
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'
}
def re1():
    input_=input('请输入选项：')
    if input_=='1':
        num = 1
        input_1 = input('请输入1-100任意数字：')
        while num < int(input_1):
            u = "https://imeizi.me/type/1/?page=" + str(num)
            a = requests.get(u, headers=headers).text
            findlink1 = re.compile(r'<h2><a href="(.*?)">')
            link1 = re.findall(findlink1, a)
            findlink2 = re.compile(r'">(.*?)</a></h2>')
            link2 = re.findall(findlink2, a)
            # print(link1,link2)
            for x, path in zip(link1, link2):
                isExists = os.path.exists(path)
                if not isExists:
                    os.makedirs(path)
                url1 = 'https://imeizi.me' + x
                print(path)
                b = requests.get(url1).text
                # print(b)
                findlink3 = re.compile(r'data-src="(.*?)"')
                link3 = re.findall(findlink3, b)
                i = 0
                for name in link3:
                    i += 1
                    img_url = 'https://imeizi.me' + name
                    img = requests.get(img_url)
                    f = open(path + '/' + str(i) + '.jpg', 'ab')
                    f.write(img.content)
                    f.close()
                    print('正在下载第', i, '张图片')
            num += 1

    elif input_=='2':
        num=1
        input_1=input('请输入1-100任意数字：')
        while num<int(input_1):
            u = "https://imeizi.me/type/2/?page=" + str(num)
            a = requests.get(u, headers=headers).text
            findlink1 = re.compile(r'<h2><a href="(.*?)">')
            link1 = re.findall(findlink1, a)
            findlink2 = re.compile(r'">(.*?)</a></h2>')
            link2 = re.findall(findlink2, a)
            # print(link1,link2)
            for x, path in zip(link1, link2):
                isExists = os.path.exists(path)
                if not isExists:
                    os.makedirs(path)
                url1 = 'https://imeizi.me' + x
                print(path)
                b = requests.get(url1).text
                # print(b)
                findlink3 = re.compile(r'data-src="(.*?)"')
                link3 = re.findall(findlink3, b)
                i = 0
                for name in link3:
                    i += 1
                    img_url = 'https://imeizi.me' + name
                    img = requests.get(img_url)
                    f = open(path + '/' + str(i) + '.jpg', 'ab')
                    f.write(img.content)
                    f.close()
                    print('正在下载第',i,'张图片')
            num+=1
    elif input_ == '3':
        num = 1
        input_1 = input('请输入1-100任意数字：')
        while num < int(input_1):
            u = "https://imeizi.me/type/3/?page=" + str(num)
            a = requests.get(u, headers=headers).text
            findlink1 = re.compile(r'<h2><a href="(.*?)">')
            link1 = re.findall(findlink1, a)
            findlink2 = re.compile(r'">(.*?)</a></h2>')
            link2 = re.findall(findlink2, a)
            # print(link1,link2)
            for x, path in zip(link1, link2):
                isExists = os.path.exists(path)
                if not isExists:
                    os.makedirs(path)
                url1 = 'https://imeizi.me' + x
                print(path)
                b = requests.get(url1).text
                # print(b)
                findlink3 = re.compile(r'data-src="(.*?)"')
                link3 = re.findall(findlink3, b)
                i = 0
                for name in link3:
                    i += 1
                    img_url = 'https://imeizi.me' + name
                    img = requests.get(img_url)
                    f = open(path + '/' + str(i) + '.jpg', 'ab')
                    f.write(img.content)
                    f.close()
                    print('正在下载第', i, '张图片')
            num += 1
    elif input_ == '4':
        num = 1
        input_1 = input('请输入1-100任意数字：')
        while num < int(input_1):
            u = "https://imeizi.me/type/4/?page=" + str(num)
            a = requests.get(u, headers=headers).text
            findlink1 = re.compile(r'<h2><a href="(.*?)">')
            link1 = re.findall(findlink1, a)
            findlink2 = re.compile(r'">(.*?)</a></h2>')
            link2 = re.findall(findlink2, a)
            # print(link1,link2)
            for x, path in zip(link1, link2):
                isExists = os.path.exists(path)
                if not isExists:
                    os.makedirs(path)
                url1 = 'https://imeizi.me' + x
                print(path)
                b = requests.get(url1).text
                # print(b)
                findlink3 = re.compile(r'data-src="(.*?)"')
                link3 = re.findall(findlink3, b)
                i = 0
                for name in link3:
                    i += 1
                    img_url = 'https://imeizi.me' + name
                    img = requests.get(img_url)
                    f = open(path + '/' + str(i) + '.jpg', 'ab')
                    f.write(img.content)
                    f.close()
                    print('正在下载第', i, '张图片')
            num += 1
    elif input_ == '5':
        num = 1
        input_1 = input('请输入1-100任意数字：')
        while num < int(input_1):
            u = "https://imeizi.me/type/5/?page=" + str(num)
            a = requests.get(u, headers=headers).text
            findlink1 = re.compile(r'<h2><a href="(.*?)">')
            link1 = re.findall(findlink1, a)
            findlink2 = re.compile(r'">(.*?)</a></h2>')
            link2 = re.findall(findlink2, a)
            # print(link1,link2)
            for x, path in zip(link1, link2):
                isExists = os.path.exists(path)
                if not isExists:
                    os.makedirs(path)
                url1 = 'https://imeizi.me' + x
                print(path)
                b = requests.get(url1).text
                # print(b)
                findlink3 = re.compile(r'data-src="(.*?)"')
                link3 = re.findall(findlink3, b)
                i = 0
                for name in link3:
                    i += 1
                    img_url = 'https://imeizi.me' + name
                    img = requests.get(img_url)
                    f = open(path + '/' + str(i) + '.jpg', 'ab')
                    f.write(img.content)
                    f.close()
                    print('正在下载第', i, '张图片')
            num += 1
    elif input_ == '6':
        num = 1
        input_1 = input('请输入1-100任意数字：')
        while num < int(input_1):
            u = "https://imeizi.me/type/6/?page=" + str(num)
            a = requests.get(u, headers=headers).text
            findlink1 = re.compile(r'<h2><a href="(.*?)">')
            link1 = re.findall(findlink1, a)
            findlink2 = re.compile(r'">(.*?)</a></h2>')
            link2 = re.findall(findlink2, a)
            # print(link1,link2)
            for x, path in zip(link1, link2):
                isExists = os.path.exists(path)
                if not isExists:
                    os.makedirs(path)
                url1 = 'https://imeizi.me' + x
                print(path)
                b = requests.get(url1).text
                # print(b)
                findlink3 = re.compile(r'data-src="(.*?)"')
                link3 = re.findall(findlink3, b)
                i = 0
                for name in link3:
                    i += 1
                    img_url = 'https://imeizi.me' + name
                    img = requests.get(img_url)
                    f = open(path + '/' + str(i) + '.jpg', 'ab')
                    f.write(img.content)
                    f.close()
                    print('正在下载第', i, '张图片')
            num += 1
    elif input_ == '7':
        num = 1
        input_1 = input('请输入1-100任意数字：')
        while num < int(input_1):
            u = "https://imeizi.me/type/7/?page=" + str(num)
            a = requests.get(u, headers=headers).text
            findlink1 = re.compile(r'<h2><a href="(.*?)">')
            link1 = re.findall(findlink1, a)
            findlink2 = re.compile(r'">(.*?)</a></h2>')
            link2 = re.findall(findlink2, a)
            # print(link1,link2)
            for x, path in zip(link1, link2):
                isExists = os.path.exists(path)
                if not isExists:
                    os.makedirs(path)
                url1 = 'https://imeizi.me' + x
                print(path)
                b = requests.get(url1).text
                # print(b)
                findlink3 = re.compile(r'data-src="(.*?)"')
                link3 = re.findall(findlink3, b)
                i = 0
                for name in link3:
                    i += 1
                    img_url = 'https://imeizi.me' + name
                    img = requests.get(img_url)
                    f = open(path + '/' + str(i) + '.jpg', 'ab')
                    f.write(img.content)
                    f.close()
                    print('正在下载第', i, '张图片')
            num += 1



if __name__ == '__main__':
    main()
    re1()
