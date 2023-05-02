import random
import time

import scrapy
from myproject.items import MyProjectItem


class MySpider(scrapy.Spider):
    name = "my_spider"
    start_urls = 'https://www.guazi.com/www/buy/c-1/#bread'
    page_count = 0
    max_page = 5
    headers = {}
    headers[
        'User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'

    def start_requests(self):

       

    def parse(self, response):

       
