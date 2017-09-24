from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import pymysql
import datetime

conn = pymysql.connect(host = '127.0.0.1', user = 'root',passwd='root',db='mysql',charset='utf8' )

cur = conn.cursor()
cur.execute("use wikipedia")

class SolutionFound(RuntimeError):
    def __init__(self,message):
        self.message = message


def getLinks(fromPageId):
    cur.execute("select toPageId from links WHERE fromPageId = %s" %fromPageId)
    if cur.rowcount == 0:
        return None
    else4:


def store(title,content):
    cur.execute("insert into pages (title,content) values (\"%s\",\"%s\")" %(title,content))
    print(cur.fetchone())
    cur.connection.commit()





links = getLinks("/wiki/Kevin_Bacon")
try:
     while len(links)>0:
        newArticle = links[random.randint(0,len(links)-1)].attrs["href"]
        print(newArticle)
        links = getLinks(newArticle)

finally:
     cur.close()
     conn.close()