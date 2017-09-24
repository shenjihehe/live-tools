import requests
from bs4 import BeautifulSoup

session = requests.Session()
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36",
           "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
           "Cookie":"__utmt=1; csrftoken=Ha7zoxi0EEsdFV01NfzNaoxkRSyE8GPCwTlCWA4M7XlnFOI3npSKK9u4UyNmZHom; __utma=12798129.2125769567.1506134445.1506134445.1506134445.1; __utmb=12798129.2.10.1506134445; __utmc=12798129; __utmz=12798129.1506134445.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)"
            }

url = "	https://www.whatismybrowser.com/detect/what-http-headers-is-my-browser-sending"
req = session.get(url,headers=headers)

soup = BeautifulSoup(req.text,"lxml")
print(soup.find("table",{"class":"table-striped"}).get_text)