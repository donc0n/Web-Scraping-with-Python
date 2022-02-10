# 다이브다이스 홈페이지에서 룰북 파일을 모두 다운로드 받는 코드

import os
import re
from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup

# 다운로드 경로
downloadDirectory = "downloaded"
downloadList = []

# page 1 부터 page 25 까지
for i in range(1, 26):
    html = urlopen("https://www.divedice.com/board/?page="+str(i)+"&db=basic_7")
    bsObj = BeautifulSoup(html, "html.parser")
    sublinks = bsObj.findAll("li", onclick=re.compile("^[?]mari_mode=view@view&db=basic_7&no="))

    for sublink in sublinks:
        html = urlopen("https://www.divedice.com/board/"+sublink["onclick"])
        bsObj = BeautifulSoup(html, "html.parser")
        downloadList.append(bsObj.find("div", {"class":"modelete"}).find("a", href=re.compile(".*[.]pdf$")))

if not os.path.exists(downloadDirectory):
    os.makedirs(downloadDirectory)

for download in downloadList:
    if download is not None:
        urlretrieve(download["href"], downloadDirectory+"/"+download.get_text())
