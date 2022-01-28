from urllib.request import urlopen
from urllib.request import HTTPError
from bs4 import BeautifulSoup

# html = urlopen("http://pythonscraping.com/pages/page1.html")
# 위 행에서 문제가 생길 수 있는 부분은 크게 두 가지이다. 
# 페이지를 찾을 수 없거나, URL 해석에서 에러가 생긴 경우 - HTTPError ("404 Page Not Found", "500 Internal Server Error")
# 서버를 찾을 수 없는 경우 - None 값을 리턴하게 된다. None 객체에서 속성을 참조 - AttributeError 발생

def get_title(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read(), "html.parser")
        title = bsObj.body.h1
    except AttributeError as e:
        return None
    return title

title = get_title("http://pythonscraping.com/pages/page1.html")
if title == None:
    print("Title could not be found")
else:
    print(title)