# session 함수로 로그인과 쿠키 처리
import requests

session = requests.Session()
params = {'username':'Anything', 'password':'password'}
s = session.post("https://pythonscraping.com/pages/cookies/welcome.php", data=params)
print("Cookie is set to:")
print(s.cookies.get_dict())
print("----------")
print("Going to profile page....")
s = session.get("https://pythonscraping.com/pages/cookies/profile.php")
print(s.text)