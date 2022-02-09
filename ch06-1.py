# 웹스크레이핑한 내용을 UTF-8로 인코딩하는 코드

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://en.wikipedia.org/wiki/Python_(programming_language)")
bsObj = BeautifulSoup(html, "html.parser")
content = bsObj.find("div", {"id":"mw-content-text"}).get_text()
content = bytes(content, "UTF-8")
content = content.decode("UTF-8")
print(content)

# HTML 페이지의 인코딩은 보통 <head> 내부의 태그에 들어있기 때문에 이 메타 태그를 찾아보고 이태그에서 지정한 인코딩 방법을 써서 페이지 콘텐츠를 읽는 게 좋다.