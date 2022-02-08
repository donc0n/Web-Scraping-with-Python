# HTML 테이블을 가져와서 CSV 파일을 만드는 코드

import csv
import re
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://en.wikipedia.org/wiki/Comparison_of_text_editors")
bsObj = BeautifulSoup(html, "html.parser")
# 비교 테이블은 현재 페이지의 첫 번째 테이블
table = bsObj.findAll("table",{"class":"wikitable"})[0]
rows = table.findAll("tr")
csvFile = open("./files/editors.csv", 'wt')
writer = csv.writer(csvFile)
try:
    for row in rows:
        csvRow = []
        for cell in row.findAll(['td', 'th']):
            new_string = re.sub(r"[^a-zA-Z0-9]","",cell.get_text())
            if new_string == "":
                continue
            csvRow.append(new_string)
        print(csvRow)
        writer.writerow(csvRow)
finally:
    csvFile.close()

# HTML 테이블의 콘텐츠를 선택해서 복사하고 엑셀에 붙여 넣으면 스크립트를 실행하지 않아도 CSV 파일을 얻을 수 있다.