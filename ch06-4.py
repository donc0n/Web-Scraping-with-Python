# 원격 워드 문서를 바이너리 파일 객체로 읽는 코드

from urllib.request import urlopen
from zipfile import ZipFile
from io import BytesIO
from bs4 import BeautifulSoup

# .docx 파일의 압축을 풀고 압축이 풀린 XML 파일을 읽느다.
wordFile = urlopen("http://pythonscraping.com/pages/AWordDocument.docx").read()
wordFile = BytesIO(wordFile)
document = ZipFile(wordFile)
xml_content = document.read('word/document.xml')

wordObj = BeautifulSoup(xml_content.decode('utf-8'), "html.parser")
textStrings = wordObj.findAll("w:t")
for textElem in textStrings:
    closeTag = ""
    try: # 임의의 텍스트 스타일 주위의 태그를 출력하거나 구분할 수 있도록 확장할 수 있다.
        # h1 태그를 출력하는 코드
        style = textElem.parent.previousSibling.find("w:pstyle")
        if style is not None and style["w:val"] == "Title":
            print("<h1>")
            closeTag = "</h1>"
    except AttributeError:
        pass
    print(textElem.text)
    print(closeTag)