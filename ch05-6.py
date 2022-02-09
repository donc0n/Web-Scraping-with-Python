# 케빈 베이컨 위키 문서부터 시작해서 링크를 랜덤 서핑하며 위키 문서를 DB에 저장하는 코드

from urllib.request import urlopen
from urllib.parse import quote
from bs4 import BeautifulSoup
import datetime
import random
import re
import pymysql

conn = pymysql.connect(host='127.0.0.1', user='root', passwd='[Your Password]', db='mysql', charset='utf8')

cur = conn.cursor()
cur.execute("USE scraping")

random.seed(datetime.datetime.now())


def store(title, content):
    cur.execute(
        "INSERT INTO pages (title, content) VALUES (\"%s\", \"%s\")", (title, content)
    )
    cur.connection.commit()

def getLinks(articleUrl):
    html = urlopen("http://ko.wikipedia.org"+articleUrl)
    bsObj = BeautifulSoup(html, "html.parser")
    title = bsObj.find("h1").get_text()
    content = bsObj.find("div", {"id":"mw-content-text"}).find("p").get_text()
    store(title, content)
    return bsObj.find("div", {"id":"bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$"))

links = getLinks("/wiki/"+quote("케빈_베이컨"))
try:
    while len(links) > 0:
        newArticle = links[random.randint(0, len(links)-1)].attrs["href"]
        print(newArticle)
        links = getLinks(newArticle)

finally:
    cur.close()
    conn.close()
