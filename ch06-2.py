# 몬티 파이튼 앨범 목록(CSV 파일)을 가져와서 터미널에 행 단위로 출력하는 코드

from urllib.request import urlopen
from io import StringIO
import csv

data = urlopen("http://pythonscraping.com/files/MontyPythonAlbums.csv").read().decode('ascii', 'ignore') # 파일을 문자열 형식으로 읽어온다.
dataFile = StringIO(data)
dictReader = csv.DictReader(dataFile) # reader는 리스트로 반환. dictReader는 딕셔너리로 반환 (약간 더 느림)

print(dictReader.fieldnames)

for row in dictReader:
    print(row)


# 파이썬의 CSV 라이브러리는 주로 로컬 파일을 가정하고 만들어져 있다. 파일이 로컬에 없을 경우 우회할 방법:
# 원하는 파일을 직접 내려받은 후 파이썬에 그 파일의 위치를 알려주는 방법
# 파일을 내려받는 파이썬 스크립트를 작성해서 읽고, (원한다면) 삭제하는 방법
# 파일을 문자열 형식으로 읽은 후 StringIO 객체로 바꿔서 파일처럼 다루는 방법 (good! - 디스크에 저장하지 않아도 된다.)
