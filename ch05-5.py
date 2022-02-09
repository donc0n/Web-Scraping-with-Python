# sql문을 실행하는 코드

import pymysql
conn = pymysql.connect(host='127.0.0.1', user='root', passwd='[Your Password]', db='mysql')

cur = conn.cursor()
cur.execute("USE scraping")
cur.execute("SELECT * FROM pages WHERE id=2")
print(cur.fetchone())
cur.close()
conn.close()
