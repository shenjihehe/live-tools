from bs4 import BeautifulSoup
with open('G:/practice/python/pycharm/1/index.html','r') as wb_data:
    Soup = BeautifulSoup(wb_data,'lxml')
    titles = Soup.select('body > div > div > div.col-md-9 > div > div > div > div.caption > h4:nth-of-type(2) > a')
    prices = Soup.select('body > div > div > div.col-md-9 > div > div > div > div.caption > h4.pull-right')
    images = Soup.select('body > div > div > div.col-md-9 > div > div > div > img')
    mounts = Soup.select('body > div > div > div.col-md-9 > div > div > div > div.ratings > p.pull-right')
    stars = Soup.select('body > div > div > div.col-md-9 > div > div > div > div.ratings > p:nth-of-type(2)')
    #print(titles,prices,images,mounts,stars,sep='\n--------\n')
for title,price,image,mount,star in zip(titles,prices,images,mounts,stars):
    data = {
        'title': title.get_text(),
        'price': price.get_text(),
        'image': image.get('src'),
        'mount': mount.get_text(),
        'star': len(star.find_all("span","glyphicon glyphicon-star"))
    }
    print(data)
