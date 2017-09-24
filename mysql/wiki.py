from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import pymysql
import datetime
import random

conn = pymysql.connect(host = '127.0.0.1', user = 'root',passwd='root',db='mysql',charset='utf8' )

cur = conn.cursor()
cur.execute("use scraping")

random.seed(datetime.datetime.now())

def store(title,content):
    cur.execute("insert into pages (title,content) values (\"%s\",\"%s\")" %(title,content))
    print(cur.fetchone())
    cur.connection.commit()





def getLinks(articleUrl):
     html = urlopen("https://en.wikipedia.org"+articleUrl)
     soup = BeautifulSoup(html,"lxml")
     title = soup.find("h1").get_text()
     content = soup.find("div",{"id":"mw-content-text"}).find("p").get_text()
     store(title,content)
     return soup.find("div",{"id":"bodyContent"}).findAll("a",href = re.compile("^(/wiki/)((?!:).)*$"))


links = getLinks("/wiki/Kevin_Bacon")
try:
     while len(links)>0:
        newArticle = links[random.randint(0,len(links)-1)].attrs["href"]
        print(newArticle)
        links = getLinks(newArticle)

finally:
     cur.close()
     conn.close()