# 데이터 관리 방법 세 가지
# 스크랩한 데이터를 웹사이트에 사용하거나 API를 만든다 -> 데이터베이스
# 인터넷에서 문서를 수집해 하드디스크에 저장한다 -> 파일스트림
# 주기적 알림을 받거나, 하루에 한 번 데이터를 집계한다 -> 스스로 이메일

# 미디어 파일 저장 - 참조 저장(URL을 저장 -> 핫링크)
from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com")
bsObj = BeautifulSoup(html, "html.parser")
imageLocation = bsObj.find("div", {"class":"pagelayer-wp-title-section"}).find("img")["src"]
urlretrieve(imageLocation, "logo.jpg")
