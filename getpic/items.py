# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class GetpicItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    nickname = scrapy.Field()
    imgurl = scrapy.Field()
    
class GetHuaweiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    content = scrapy.Field()