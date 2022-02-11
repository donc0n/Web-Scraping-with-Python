# 지저분한 데이터 코드로 정리하기
# 위키 문서 페이지의 n-grams을 얻어내는 코드

from urllib.request import urlopen
import re
import string
import operator

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
    output = {}
    for i in range(len(input)-n+1):
        ngramTemp = " ".join(input[i:i+n])
        if ngramTemp not in output:
            output[ngramTemp] = 0
        output[ngramTemp] += 1
    return output

def isCommon(ngram):
    commonWords = ["the", "be", "and", "of", "a", "in", "to", "have", "it", "I", "that", "for", "you", "he", "with", "on", "do", "say", "this", "they", "is", "an", "at", "but",
    "we", "his", "from", "that", "not", "by", "she", "or", "as", "what", "go", "their", "can", "who", "get", "if", "would", "her", "all", "my", "make", "about", "know", "will",
    "up", "one", "no", "which", "was", "has", "been", "our", "which", "those", "are", "any"]
    for word in ngram:
        if word in commonWords:
            return True
    return False

content = str(urlopen("http://pythonscraping.com/files/inaugurationSpeech.txt").read(), 'utf-8')
ngrams = ngrams(content, 2)
sortedNGrams = sorted(ngrams.items(), key = operator.itemgetter(1), reverse=True)
# 3회 이상 반복된, 흔한 단어가 들어가지 않은 ngrams를 출력 
for ngrams in sortedNGrams:
    if ngrams[1] >= 3 and not isCommon(ngrams[0].split()):
        print(ngrams)

# 자주 쓰인 각각의 ngram에 대해 그 구절이 쓰인 첫 번째 문장을 검색하는 방법 - 본문 전체에 대한 만족할 만한 개관이 될 거라고 짐작할 수 있다.