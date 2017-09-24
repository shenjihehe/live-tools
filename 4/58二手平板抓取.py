from bs4 import BeautifulSoup
from time import sleep
import requests


#header ={}

def get_url(num):
    urls=['http://bj.58.com/pbdn/0/pn{}/'.format(str(i)) for i in range(1,num+1,1)]
    print(urls)
    for url in urls:
        wb_data=requests.get(url)
        soup = BeautifulSoup(wb_data.text,'lxml')
        item_urls = soup.select('#infolist > div.infocon > table > tbody > tr.zzinfo > td.img > a')

        links = []
        for item_url in item_urls:
            links.append(item_url.get('href'))


        result_urls = []
        i = 0
        for link in links:
            if link[7:11] == 'zhua' :
                result_urls.append(link)
        sleep(2)
    return  result_urls


def get_message(url):
    wb_data= requests.get(url)
    soup = BeautifulSoup(wb_data.text,'lxml')

    type = soup.select('#nav > div > span:nth-of-type(4) > a')
    title = soup.select('div.box_left > div > div.box_left_top > h1')
    price = soup.select('body > div.content > div > div.box_left > div.info_lubotu.clearfix > div.info_massege.left > div.price_li > span > i')
    address = soup.select('body > div.content > div > div.box_left > div.info_lubotu.clearfix > div.info_massege.left > div.palce_li > span > i')
    tagss = soup.select('body > div.content > div > div.box_left > div.info_lubotu.clearfix > div.info_massege.left > div.biaoqian_li > span')
    tags=[]
    for tag in tagss:
        tags.append(tag.get_text())
    view = soup.select('body > div.content > div > div.box_left > div.info_lubotu.clearfix > div.box_left_top > p > span.look_time')
    print(type,title,price,address,tags,view)


    data = {
        'type': type[0].get_text().strip(),
        'title': title[0].get_text(),
        'price': price[0].get_text(),
        'address': address[0].get_text(),
        'tags': tags,
        'view': view[0].get_text()
    }
    print(data)
    sleep(2)

urls =get_url(2)
for url in urls:
    get_message(url)