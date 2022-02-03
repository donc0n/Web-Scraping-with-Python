from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
# 홈페이지와 연결된 전체 사이트 크롤링 코드
pages = set()
def getLinks(pageUrl):
    global pages
    html = urlopen("http://en.wikipedia.org"+pageUrl)
    bsObj = BeautifulSoup(html, "html.parser")
    try:
        print(bsObj.h1.get_text())
        print(bsObj.find(id="mw-content-text").findAll("p")[0])
        print(bsObj.find(id="ca-edit").find("span").find("a").attrs['href'])
    except AttributeError:
        print("This page is missing something! No worries though!")
    for link in bsObj.find("div", {"id":"bodyContent"}).findAll("a", href=re.compile("^(/wiki/)")):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                newPage = link.attrs['href']
                print("---------------\n"+newPage)
                pages.add(newPage)
                getLinks(newPage)
getLinks("")

# 파이썬은 기본적으로 재귀호출을 1,000회로 제한하므로 위 코드는 결국 멈추게 된다.
# 이를 막으려면 재귀 카운터를 삽입하거나 다른 방법을 강구해야 한다.

# 예외 핸들어 안에 여러 행을 넣는 것은 어떤 행에서 예외가 일어날지 모르기 때문에 위험하다. 
# 하지만 원하는 데이터가 사이트에 있을 확률에 순서가 있고 일부 데이터를 잃어도 되거나 자세한 로그를 유지할 필요가 없는 경우에는 별 문제가 없다.