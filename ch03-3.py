# 연결된 외부 링크를 따라가는 인터넷 크롤링 코드

from urllib.request import urlopen
from urllib.request import HTTPError
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import re
import datetime
import random
# 외부 링크를 닥치는 대로 따라가는 크롤러를 만들기 전:
# 내가 수집하려는 데이터는 어떤 것인지? 정해진 사이트 몇 개만 수집하면 되나 -> 더 쉬운 방법이 있다.
# 그런 사이트가 있는지조차 몰랐던 사이트에도 방문하는 크롤러가 필요할까? 
# 크롤러가 특정 웹사이트에 도달하면, 즉시 새 웹사이트를 가리키는 링크를 따라가야 할까? 아니면 한동안 현재 웹사이트에서 머물면서 파고들어야 할까?
# 특정 사이트를 스크랩에서 제외할 필요는 없나? 다른 언어권의 콘텐츠도 수집해야 할까?
# 만약 크롤러가 방문한 사이트의 웹마스터가 크롤러의 방문을 알아차렸다면 나 자신을 법적으로 보호할 수 있을까?
pages = set()
random.seed(datetime.datetime.now())

# 페이지에서 발견된 내부 링크를 모두 목록으로 만듭니다.
def getInternalLinks(bsObj, includeUrl):
    includeUrl = urlparse(includeUrl).scheme+"://"+urlparse(includeUrl).netloc
    internalLinks = []
    # /로 시작하는 링크를 모두 찾습니다.
    for link in bsObj.findAll("a", href=re.compile("^(/|.*"+includeUrl+")")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in internalLinks:
                if(link.attrs['href'].startswith("/")):
                    internalLinks.append(includeUrl+link.attrs['href'])
                else:
                    internalLinks.append(link.attrs['href'])
    return internalLinks

# 페이지에서 발견된 외부 링크를 모두 목록으로 만듭니다.
def getExternalLinks(bsObj, excludeUrl):
    externalLinks = []
    # 현재 URL을 포함하지 않으면서 http나 www로 시작하는 링크르 모두 찾습니다.
    for link in bsObj.findAll("a", href=re.compile("^(http|www)((?!"+excludeUrl+").)*$")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in externalLinks:
                externalLinks.append(link.attrs['href'])
    return externalLinks

def splitAddress(address):
    addressParts=address.replace("http://", "").split("/")
    return addressParts

def getRandomExternalLink(startingPage):
    html = urlopen(startingPage)
    bsObj = BeautifulSoup(html, "html.parser")
    externalLinks = getExternalLinks(bsObj, urlparse(startingPage).netloc)
    if len(externalLinks) == 0:
        domain = urlparse(startingPage).scheme+"://"+urlparse(startingPage).netloc
        internalLinks = getInternalLinks(bsObj, domain)
        return getRandomExternalLink(internalLinks[random.randint(0, len(internalLinks)-1)])
    else:
        return externalLinks[random.randint(0, len(externalLinks)-1)]

def followExternalOnly(startingSite):
    externalLink = getRandomExternalLink(startingSite)
    print("Random external link is: "+externalLink)
    followExternalOnly(externalLink)

# followExternalOnly("http://oreilly.com")

allExtLinks = set()
allIntLinks = set()

def getAllExternalLinks(siteUrl):
    try:
        html=urlopen(siteUrl)
    except HTTPError as e:
        return None
    try:
        bsObj=BeautifulSoup(html,"html.parser")
        internalLinks=getInternalLinks(bsObj,splitAddress(domain)[0])
        externalLinks=getExternalLinks(bsObj,splitAddress(domain)[0])
    except AttributeError as e:
        return None

    for link in externalLinks:
        if link not in allExtLinks:
            allExtLinks.add(link)
            print(link)
    for link in internalLinks:
        if link == "/":
            link = domain
        elif link[0:2] == "//":
            link = "http:" + link
        elif link[0:1] == "/":
            link = domain + link

        if link not in allIntLinks:
            print("About to get link: "+link)
            allIntLinks.add(link)
            getAllExternalLinks(link)

domain = "http://oreilly.com"
getAllExternalLinks(domain)
