# POST 요청으로 로그인과 쿠키 처리
import requests

params = {'username':'Anything', 'password':'password'}
r = requests.post("https://pythonscraping.com/pages/cookies/welcome.php", data=params)
print("Cookie is set to:")
print(r.cookies.get_dict())
print("----------")
print("Going to profile page....")
r = requests.get("https://pythonscraping.com/pages/cookies/profile.php", cookies=r.cookies)
print(r.text)