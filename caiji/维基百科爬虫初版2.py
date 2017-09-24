# 因为没有限制就不设置代理池和规避部署
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages=set()

def getLinks(pageUrl):
    global pages
    html = urlopen("https://en.wikipedia.org"+pageUrl)
    soup = BeautifulSoup(html,"lxml")
    try:
        for link in soup.find("div",{"id":"bodyContent"}).findAll("a",href = re.compile("^(\/wiki\/)((?!:).)*$")):
            if len(pages) < 6:
                if 'href' in link.attrs:
                    if link.attrs['href'] not in pages:
                        newPage = link.attrs['href']
                        print(newPage)
                        pages.add(newPage)
                        getLinks(newPage)
            else:
                break
    except AttributeError:
        print("div id属性定位失效，请重新选择或修改！")

getLinks("/wiki/Kevin_Bacon")
print("太累了，不爬了！")

print(pages)
