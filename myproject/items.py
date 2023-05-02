# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MyProjectItem(scrapy.Item):
    brand = scrapy.Field()
    series = scrapy.Field()
    model = scrapy.Field()
    purchased = scrapy.Field()
    mileage = scrapy.Field()
    price = scrapy.Field()
    pass
