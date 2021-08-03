import requests as re
import bs4
import pprint
res = re.get('https://imeizi.me/article/9266/')
res.raise_for_status()
sp = bs4.BeautifulSoup(res.text,'html.parser')
elems = sp.select('p img[class="alignnone size-medium wp-image-42]')
#ele = sp.find_all("p", class_="alignnone size-medium wp-image-42")
pprint.pprint(res.text)
pprint.pprint(elems)
lenn = len(elems)
#link = elems[5].getText()
#print(link)
