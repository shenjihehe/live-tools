from urllib.request import urlopen
from bs4 import BeautifulSoup
from collections import OrderedDict
import re
import string


def cleanInput(input):
    input = re.sub('\n+'," ",input)
    input = re.sub('\[[0-9]*]',"",input)
    input = re.sub(' +'," ",input)
    input = bytes(input ,"utf-8")
    input = input.decode("ascii","ignore")
    cleanInput = []
    input = input.split(' ')
    for item in input:
        item = item.strip(string.punctuation)
        if len(item)>1 or (item.lower() == 'a' or item.lower() == 'i'):
            cleanInput.append(item)
    return  cleanInput
def ngrams(input,n):
    input = cleanInput(input)
    output = {}
    for i in range(len(input)-n+1):
        ngramTemp = str(input[i:i+n])
        if ngramTemp not in output:
            output[ngramTemp] = 0
        output[ngramTemp] += 1
    return output


dicts ={}
html = urlopen("https://en.wikipedia.org/wiki/Python_(programming_language)")
soup = BeautifulSoup(html,"lxml")
content = soup.find("div",{"id":"mw-content-text"}).get_text()

ngrams = ngrams(content,2)
print("2-grams count is:"+str(len(ngrams)))
print(ngrams)

ngrams = OrderedDict(sorted(ngrams.items(),key=lambda t : t[1],reverse=True))
print(ngrams)
