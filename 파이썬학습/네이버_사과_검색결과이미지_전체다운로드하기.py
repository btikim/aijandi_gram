from urllib.request import urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
import os

baseUrl = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query='
plusUrl = input('검색어를 입력하세요.')
url = baseUrl + quote_plus(plusUrl)

print(url)

html = urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
img = soup.find_all(class_='_img')

print(img[0])

if not os.path.exists(plusUrl):
    os.mkdir(plusUrl)

os.chdir(plusUrl)

n = 1
for i in img:
    imgUrl = i['data-source']
    with urlopen(imgUrl) as f:
        with open(plusUrl + '_' + str(n)+'.jpg', 'wb') as h:
            img = f.read()
            h.write(img)
    n += 1

print('다운로드 완료')