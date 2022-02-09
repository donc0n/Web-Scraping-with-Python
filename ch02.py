# 복잡한 HTML 분석 코드

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
# "페이지 인쇄" 같은 링크를 찾아보거나, 더 나은 HTML 구조를 갖춘 모바일 버전 사이트를 찾아본다.
# 자바스크립트 파일에 숨겨진 정보를 찾아본다.
# 원하는 정보가 페이지 URL에 들어있을 때도 있다.
# 다른 웹사이트에 같은 데이터를 찾아본다.
# 그래도 안된다면...
html = urlopen("http://pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html, "html.parser")
nameList = bsObj.findAll("span", {"class":"green"})
for name in nameList:
    print(name.get_text()) # get_text() 태그를 제거할 때 사용 - 항상 마지막에 사용

html = urlopen("http://pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html, "html.parser")

for child in bsObj.find("table", {"id":"giftList"}).children:
    print(child)

for sibling in bsObj.find("table", {"id":"giftList"}).tr.next_siblings: # 타이틀행 제외
    print(sibling)

print(bsObj.find("img",{"src":"../img/gifts/img1.jpg"}).parent.previous_sibling.get_text()) # 이미지가 나타내는 객체의 가격 출력

images = bsObj.findAll("img",{"src":re.compile("\.\./img/gifts/img.*\.jpg")}) # 정규표현식 필터링
for image in images:
    print(image["src"])
