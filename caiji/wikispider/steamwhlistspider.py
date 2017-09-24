#encoding:utf-8
from bs4 import BeautifulSoup
import requests
import re


url='http://steamcommunity.com/id/shenyiyangdenanren/wishlist'
response = requests.get(url)
data = BeautifulSoup(response.text,"lxml")

wb_datas = []
for info in data.select("#wishlist_items > div"):
    if info.select("div.discount_block.discount_block_inline") == []:
        continue
    else:
        game = str(info.select("div.wishlistRowItem > h4")[0].get_text())
        off = str(info.select("div.discount_pct")[0].get_text())
        origin_price= str(info.select("div.discount_original_price")[0].get_text())
        discount_price = str(info.select("div.discount_final_price")[0].get_text())
        addr = str(info.select("div.storepage_btn_ctn > a")[0].get('href'))
        print("%s\n\t现价：%s，原价：%s，折扣：%s，商品页面：%s，" % (game, origin_price, discount_price, off, addr))

# print(wb_data)
# print(data)
# offs=[]
# or_prices = []
# dis_prices =[]

# for pricedata in data.findAll("div",{"class":"discount_block discount_block_inline"}):
    # addrdata = pricedata.next_siblings
    # print(addrdata)
#     pricesdata = BeautifulSoup(pricedata.text, "lxml")
#     off = pricedata.select("div.discount_pct")[0].get_text()
#     offs.append(off)
#     or_price = pricedata.select("div.discount_original_price")[0].get_text()
#     or_prices.append(or_price)
#     dis_price = pricedata.select("div.discount_final_price")[0].get_text()
#     dis_prices.append(dis_price)
#
# print(offs)
# print(or_prices)
# print(dis_prices)

# for addrdata in data.findAll("div",{"class":"discount_block discount_block_inline"}).parents:
#     print(addrdata)
