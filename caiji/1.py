from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen('http://www.pythonscraping.com/pages/page3.html')
soup = BeautifulSoup(html,'lxml')

# for chlid in soup.find("table",{"id":"giftList"}).children:
#     print(chlid)

# for sibling in soup.find("table",{"id":"giftList"}).tr.next_siblings:
#     print(sibling)

print(soup.find("img",{"src":"../img/gifts/img1.jpg"}).parent.previous_sibling.get_text())

# images = soup.findAll("img",{"src":re.compile("\.\.\/img\/gifts\/img.*\.jpg")})
# for image in images:
#     print(image["src"])
#     address = "http://www.pythonscraping.com/ "+'/'.join(image["src"].split('/')[1:])
#     print(address)

# a = soup.findAll(lambda tag: len(tag.attrs) == 1)
# print(a)