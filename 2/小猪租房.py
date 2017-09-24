from bs4 import BeautifulSoup
import requests
from time import sleep

def get_urls(num):
    target_urls = ['http://bj.xiaozhu.com/zhengzu-duanzufang-p{}-2/'.format(str(i)) for i in range(1, num+1, 1)]
    result_urls=[]
    for target_url in target_urls:
        wb_data = requests.get(target_url)
        soup = BeautifulSoup(wb_data.text, 'lxml')
        urls = soup.select('#page_list > ul > li > a')
        for url in urls:
            result_urls.append(url.get('href'))
        sleep(2)
    return  result_urls

def print_gender(class_name):
    if class_name == 'member_ico1':
        return '女'
    if class_name == 'member_ico':
        return '男'


def get_message(url):
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    titles = soup.select('div.pho_info > h4 > em')
    addrs = soup.select('div.pho_info > p')
    prices = soup.select('#pricePart > div.day_l > span')
    images = soup.select('#curBigImage')
    houseimages= soup.select('#floatRightBox > div.js_box.clearfix > div.member_pic > a > img')
    names = soup.select('#floatRightBox > div.js_box.clearfix > div.w_240 > h6 > a')
    sexs = soup.select('#floatRightBox > div.js_box.clearfix > div.member_pic > div')


    for title,addr,price,image,houseimage,name,sex in zip(titles,addrs,prices,images,houseimages,names,sexs):
        title = title.get_text()
        addr = addr.get('title')
        price = price.get_text()
        image = image.get('src')
        houseimage: houseimage.get('src')
        name = name.get_text()
        sex = sex.get('class')[0]
        print(addr)

        data = {
            'title':title,
            'addr':addr,
            'price':price,
            'image':image,
            'houseimage':houseimage,
            'name':name,
            'sex':print_gender(sex)
        }
        print(data)
        sleep(1)



full_urls = get_urls(1)
for full_url in full_urls:
    get_message(full_url)







