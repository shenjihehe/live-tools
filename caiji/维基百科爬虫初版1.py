from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import random
import datetime

html = urlopen("https://en.wikipedia.org/wiki/Kevin_Bacon")
soup = BeautifulSoup(html,'lxml')

# for link in soup.findAll("a"):
#     if 'href' in link.attrs:
#         print(link.attrs['href'])
#

# for link in soup.find("div",{"id":"bodyContent"}).findAll("a",href = re.compile("^(\/wiki\/)((?!:).)*$")):
#     if 'href' in link.attrs:
#             print(link.attrs['href'])

random.seed(datetime.datetime.now())
def getLinks(articleUrl):
    try:
        html = urlopen("https://en.wikipedia.org"+articleUrl)
        soup =BeautifulSoup(html,"lxml")
        return soup.find("div",{"id":"bodyContent"}).findAll("a",href = re.compile("^(\/wiki\/)((?!:).)*$"))
    except AttributeError:
        print("div id属性定位失效，请重新选择或修改！")

links=getLinks("/wiki/Kevin_Bacon")
# print(links)
try:
    while len(links)>0:
        newArticle = links[random.randint(0,len(links)-1)].attrs['href']
        print(newArticle)
        links = getLinks(newArticle)
except TypeError:
    print("未有数据被抓取！")