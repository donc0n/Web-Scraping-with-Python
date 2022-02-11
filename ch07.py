# 지저분한 데이터 코드로 정리하기
# 위키 문서 페이지의 n-grams을 얻어내는 코드

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import string

# 줄바꿈 문자 -> 공백으로 지운다.
# UTF-8로 인코딩해서 이스케이프 문자를 없앤다.
# i, a를 제외한 한 글자로 된 '단어'는 버려야 한다.
# 위키백과 인용 표시인 대괄호로 감싼 숫자도 버려야 한다.
# 구두점도 버려야 한다.
def cleanInput(input):
    input = re.sub("\n+", " ", input)
    input = re.sub("\[[0-9]*\]", "", input)
    input = re.sub(" +", " ", input)
    input = bytes(input, "UTF-8")
    input = input.decode("ascii", "ignore")
    cleanInput = []
    input = input.split(" ")
    for item in input:
        item = item.strip(string.punctuation)
        if len(item) > 1 or (item.lower() == "a" or item.lower() == "i"):
            cleanInput.append(item)
    return cleanInput


def ngrams(input, n):
    input = cleanInput(input)
    output = []
    for i in range(len(input)-n+1):
        output.append(input[i:i+n])
    return output

html = urlopen("https://en.wikipedia.org/wiki/Python_(programming_language)")
bsObj = BeautifulSoup(html, "html.parser")
content = bsObj.find("div", {"id":"mw-content-text"}).get_text()
ngrams = ngrams(content, 2)
print(ngrams)
print("2-gram count is: "+str(len(ngrams)))