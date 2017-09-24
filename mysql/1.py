import pymysql

conn = pymysql.connect(host = '127.0.0.1', user = 'root',passwd='root',db='mysql' )

cur = conn.cursor()
cur.execute("use scraping")

cur.execute("select * from pages where id = 3")
print(cur.fetchone())
cur.close()
conn.close()