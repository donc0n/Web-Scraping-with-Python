# 홈페이지에서 img 태그 파일을 모두 다운로드 받는 코드

import os
from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup

downloadDirectory = "downloaded"
baseUrl = "https://pythonscraping.com"

def getAbsoluteUrl(baseUrl, source):
    if source.startswith("https://www."):
        url = "https://"+source[11:]
    elif source.startswith("https://"):
        url = source
    elif source.startswith("www."):
        url = "https://" +source[4:]
    else:
        url = baseUrl+"/"+source
    if baseUrl not in url:
        return None
    return url

def getDownloadPath(baseUrl, absoluteUrl, downloadDirectory):
    path = absoluteUrl.replace("www.", "")
    path = path.replace(baseUrl, "")
    path = downloadDirectory+path
    directory = os.path.dirname(path)

    if not os.path.exists(directory):
        os.makedirs(directory)

    return path


html = urlopen("http://www.pythonscraping.com")
bsObj = BeautifulSoup(html, "html.parser")
downloadList = bsObj.findAll("img")

for download in downloadList:
    fileUrl = getAbsoluteUrl(baseUrl, download["src"])
    if fileUrl is not None:
        print(fileUrl)
    urlretrieve(fileUrl, getDownloadPath(baseUrl, fileUrl, downloadDirectory))
