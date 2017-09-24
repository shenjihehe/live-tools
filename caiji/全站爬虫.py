from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random

pages = set()
random.seed(datetime.datetime.now())

#获取页面内所有内链连接
def getInternalLinks(soup,includerUrl):
    internaLinks = []
    #找出所有以“/”开头的链接
    for link in soup.findAll("a",href = re.compile("^(/|.*"+includerUrl+")")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in internaLinks:
                internaLinks.append(link.attrs['href'])
    return internaLinks

#获取页面内所有外链连接
def getExternalLinks(soup,excluderUrl):
    externalLinks = []
    #找出所有以“http”或“www”开头且不包含当前URL的链接
    for link in soup.findAll("a",href = re.compile("^(http|www)((?!"+excluderUrl+").)*$")):
        if link.attrs['href'] is not  None:
            if link.attrs['href'] not in externalLinks:
                externalLinks.append(link.attrs['href'])
    return externalLinks

def splitAddress(address):
    addressParts = address.replace("http://","").split("/")
    return addressParts


def getRandomExternalLink(startingPage):
    html = urlopen(startingPage)
    soup = BeautifulSoup(html,"lxml")
    externalLinks = getExternalLinks(soup,splitAddress(startingPage)[0])
    if len(externalLinks) == 0:
        internalLinks =getInternalLinks(soup,startingPage)
        return getExternalLinks(soup,internalLinks[random.randint(0,len(internalLinks)-1)])
    else:
        return externalLinks[random.randint(0,len(externalLinks)-1)]

def followExternalOnly(startingSite):
    externalLink = getRandomExternalLink(startingSite)
    print("随机外链是："+externalLink)
    followExternalOnly(externalLink)

# followExternalOnly("https://oreilly.com/")

#收集网站上发现的所有外链列表
allExtlinks = set()
allIntLinks = set()

def getAllExternalLinks(siteUrl):
    html = urlopen(siteUrl)
    soup = BeautifulSoup(html,"lxml")
    internalLinks = getInternalLinks(soup,splitAddress(siteUrl)[0])
    externalLinks = getExternalLinks(soup,splitAddress(siteUrl)[0])
    for link in externalLinks:
        if link not in allExtlinks:
            allExtlinks.add(link)
            print("外链："+link)
    for link in internalLinks:
        if link not in allIntLinks:
            print("即将获取的内链：" + link)
            allIntLinks.add(link)
            getAllExternalLinks(link)

getAllExternalLinks("https://oreilly.com")
