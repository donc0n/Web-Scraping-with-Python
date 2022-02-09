# Gmail 이메일을 보내는 코드
# 1시간에 1번씩 https://isitchristmas.com 사이트를 확인하여 "아니오"외에 다른 것이 보이면 크리스마스가 되었다고 메일을 보내는 프로그램.

from email.mime.text import MIMEText
from urllib.request import urlopen
from urllib.parse import quote
from bs4 import BeautifulSoup
import smtplib
import time

def sendMail(subject, body):    
    msg = MIMEText(body) # 저수준 MIME 프로토콜 이메일 형식
    msg['Subject'] = subject
    msg['From'] = "christmas_alerts@gmail.com"
    msg['To'] = '[Your Id]@gmail.com'

    username = '[Your Id]@gmail.com'
    password = '[Your App-Specific Password]' # app-specific password
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(username, password)
    server.send_message(msg)
    server.quit()

bsObj = BeautifulSoup(urlopen("https://isitchristmas.com/"), "html.parser")
while(bsObj.find("a", {"id":"answer"}).attrs['title'] == "아니요"):
    print("It is not Christmas yet.")
    time.sleep(3600)
sendMail("It is Christmas!", "According to http://isitchristmas.com, it is Christmas.")