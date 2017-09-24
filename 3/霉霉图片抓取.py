from bs4 import BeautifulSoup
import time,requests,urllib.request


header ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'}

def get_url(num):
    urls = ['https://weheartit.com/inspirations/taylorswift?scrolling=true&page={}'.format(str(i)) for i in range(1,num+1,1)]
    image_urls = []
    for url in urls:
        wb_data = requests.get(url,headers=header)
        soup = BeautifulSoup(wb_data.text,'lxml')
        target_urls = soup.select('  div.no-padding > div > a > img')
        for target_url in target_urls:
            image_urls.append(target_url.get('src'))
        print(image_urls)
    return image_urls

def down_image(urls):
    local = 'G:/practice/python/pycharm/3/'
    i=1
    for url in urls:
        urllib.request.urlretrieve(url,local + str(i) + url[-5:])
        i += 1
        sleep(1)
        print(done)




full_iamges = get_url(1)
down_image(full_iamges)

