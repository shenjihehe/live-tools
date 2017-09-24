from bs4 import BeautifulSoup
import requests,pymongo
from time import sleep

client = pymongo.MongoClient('localhost',27017)
xiaozhu = client['xiaozhu']
rent_informations = xiaozhu['rent_informations']

# header ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36','Cookie':'f=n; ipcity=tongling%7C%u94DC%u9675; myfeet_tooltip=end; f=n; f=n; id58=c5/ns1mhBLhE7AtDDO6yAg==; bj58_id58s="VGNjZGlKNDM3S0hHODY2Mg=="; sessionid=dce5136b-746e-46b4-b9b8-fa2c0813a967; als=0; bj58_new_uv=1; 58tj_uuid=452490c9-951f-466a-bf1d-8fa1f72e5faf; new_uv=1; commontopbar_city=1%7C%u5317%u4EAC%7Cbj; f=n; xxzl_deviceid=XviTFb%2BR1Fg70mXEpROx3wmOBoZhWaqCnu07GA8TdbhM6bA0Iln3H15R2T4MXoPw','Cookie':'gr_user_id=b48000d7-a559-41f7-af1a-51ffd5b0f7de; _ga=GA1.2.1940505077.1503564721; abtest_ABTest4SearchDate=b; xzuuid=2a08d793; gr_session_id_59a81cc7d8c04307ba183d331c373ef6=b471a9e8-da2b-490c-ac12-0bcdaa0eb98e; __utmt=1; __utma=29082403.1940505077.1503564721.1503583957.1503847260.3; __utmb=29082403.1.10.1503847260; __utmc=29082403; __utmz=29082403.1503564721.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)'}
#
#
# def get_urls(num):
#     target_urls = ['http://bj.xiaozhu.com/zhengzu-duanzufang-p{}-2/'.format(str(i)) for i in range(1, num+1, 1)]
#     print(target_urls)
#     result_urls=[]
#     for target_url in target_urls:
#         wb_data = requests.get(target_url,headers=header)
#         soup = BeautifulSoup(wb_data.text, 'lxml')
#         urls = soup.select('#page_list > ul > li > a')
#         for url in urls:
#             result_urls.append(url.get('href'))
#         sleep(3)
#     return  result_urls
#
# def print_gender(class_name):
#     if class_name == 'member_ico1':
#         return '女'
#     if class_name == 'member_ico':
#         return '男'
#
#
# def get_message(url):
#     wb_data = requests.get(url,headers=header)
#     soup = BeautifulSoup(wb_data.text, 'lxml')
#     titles = soup.select('div.pho_info > h4 > em')
#     addrs = soup.select('div.pho_info > p')
#     prices = soup.select('#pricePart > div.day_l > span')
#     images = soup.select('#curBigImage')
#     houseimages= soup.select('#floatRightBox > div.js_box.clearfix > div.member_pic > a > img')
#     names = soup.select('#floatRightBox > div.js_box.clearfix > div.w_240 > h6 > a')
#     sexs = soup.select('#floatRightBox > div.js_box.clearfix > div.member_pic > div')
#
#
#
#     for title,addr,price,image,houseimage,name,sex in zip(titles,addrs,prices,images,houseimages,names,sexs):
#         title = title.get_text()
#         addr = addr.get('title')
#         price = price.get_text()
#         image = image.get('src')
#         houseimage = houseimage.get('src')
#         name = name.get_text()
#         sex = sex.get('class')[0]
#         print(addr)
#
#         data = {
#             'title':title,
#             'addr':addr,
#             'price':price,
#             'image':image,
#             'houseimage':houseimage,
#             'name':name,
#             'sex':print_gender(sex)
#         }
#
#         print(data)
#         rent_informations.insert_one(data)
#         print('写入成功！')
#         sleep(3)
#
#
#
# full_urls = get_urls(3)
# for full_url in full_urls:
#     get_message(full_url)
#     sleep(3)
# print('写入全部成功！')

# $lt/$lte/$gt/$gte/$ne，依次等价于</<=/>/>=/!=。（l表示less g表示greater e表示equal n表示not  ）
for item in rent_informations.find({'price':{'$lte':'500'}}):
    print(item)

# for item in rent_informations.find():
#     print(item['price'])


