# 베이컨 넘버(케빈 베이컨까지의 링크 숫자)가 6 이하인 위키백과 페이지를 모두 저장하는 코드

"""SQL
CREATE TABLE wikipedia.pages (
    id INT NOT NULL AUTO_INCREMENT,
    url VARCHAR(255) NOT NULL,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id)); 

CREATE TABLE wikipedia.links (
    id INT NOT NULL AUTO_INCREMENT,
    fromPageId INT NULL,
    toPageId INT NULL,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id));
"""
from urllib.request import urlopen
from urllib.parse import quote
from bs4 import BeautifulSoup
import re
import pymysql

conn = pymysql.connect(host='127.0.0.1', user='root', passwd='[Your Password]', db='mysql', charset='utf8')

cur = conn.cursor()
cur.execute("USE wikipedia")

def pageScraped(url):
    cur.execute("SELECT * FROM pages WHERE url = %s", (url))
    if cur.rowcount == 0:
        return False
    page = cur.fetchone()

    cur.execute("SELECT * FROM links WHERE fromPageId = %s", (int(page[0])))
    if cur.rowcount == 0:
        return False
    return True


def insertPageIfNotExists(url):
    cur.execute("SELECT * FROM pages WHERE url = %s", (url))
    if cur.rowcount == 0:
        cur.execute("INSERT INTO pages (url) VALUES (%s)", (url))
        conn.commit()
        return cur.lastrowid
    else:
        return cur.fetchone()[0]


def insertLink(fromPageId, toPageId):
    cur.execute("SELECT * FROM links WHERE fromPageId = %s AND toPageId = %s", (int(fromPageId), int(toPageId)))
    if cur.rowcount == 0:
        cur.execute("INSERT INTO links (fromPageId, toPageId) VALUES (%s, %s)", (int(fromPageId), int(toPageId)))
    conn.commit()


def getLinks(pageUrl, recursionLevel):
    global pages
    if recursionLevel > 4:
        return
    pageId = insertPageIfNotExists(pageUrl)
    html = urlopen("http://ko.wikipedia.org"+pageUrl)
    bsObj = BeautifulSoup(html, "html.parser")
    for link in bsObj.findAll("a", href=re.compile("^(/wiki/)((?!:).)*$")):
        insertLink(pageId, insertPageIfNotExists(link.attrs['href']))
        if not pageScraped(link.attrs['href']):
            newPage = link.attrs['href']
            print(newPage)
            getLinks(newPage, recursionLevel+1)
        else:
            print("Skipping: "+str(link.attrs['href'])+" found on "+pageUrl)
    

getLinks("/wiki/"+quote("케빈_베이컨"), 0)
cur.close()
conn.close()
