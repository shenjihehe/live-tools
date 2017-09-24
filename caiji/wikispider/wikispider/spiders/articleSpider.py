from scrapy.selector import Selector
from scrapy import Spider
from wikispider.wikispider.items import Article

class ArticleSpider(Spider):
    name = "article"
    allowed_domains = ["en.wikipedia.org"]
    start_urls = ["https://en.wikipedia.org/wiki/Main_Page","https://en.wikipedia.org/wiki/Python_(programming_language)"]

def parse(self,response):
    item -Article()
    title = response.xpath('//*[@id="firstHeading"]')

