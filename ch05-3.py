# CSV 파일을 WRITE 하는 코드

# CSV(Comma-Spearated Values) 스프레드시트 데이터를 저장할 때 가장 널리 쓰이는 파일 형식
import os
import csv

if not os.path.exists("files"):
        os.makedirs("files")

csvFile = open("./files/test.csv", 'w+')
try:
    writer = csv.writer(csvFile)
    writer.writerow(('number', 'number plus 2', 'number times 2'))
    for i in range(10):
        writer.writerow((i, i+2, i*2))
finally:
    csvFile.close()