from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re
random.seed(datetime.datetime.now())
'''
html = urlopen("http://en.wikipedia.org/wiki/Kevin_Bacon")
bsObj = BeautifulSoup(html, "html.parser")
for link in bsObj.findAll("a"):
    if 'href' in link.attrs:
        print(link.attrs['href'])

# 페이지에는 사이드바, 푸터, 헤더 링크 등 우리가 관심 있어 하는 항목이 아닌 페이지를 가리키는 링크가 많이 있다.

for link in bsObj.find("div", {"id":"bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$")):
    if 'href' in link.attrs:
        print(link.attrs['href'])
'''

# 링크 랜덤 서핑 코드
def getLinks(articleUrl):
    html = urlopen("http://en.wikipedia.org"+articleUrl)
    bsObj = BeautifulSoup(html, "html.parser")
    return bsObj.find("div", {"id":"bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$"))

links = getLinks("/wiki/Kevin_Bacon")
while len(links) > 0:
    newArticle = links[random.randint(0, len(links)-1)].attrs["href"]
    links = getLinks(newArticle)
    print(newArticle)
