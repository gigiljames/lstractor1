# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Lstractor1Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    StoreID = scrapy.Field() 
    StoreName = scrapy.Field()
    Street = scrapy.Field() 
    City = scrapy.Field() 
    State = scrapy.Field() 
    Phone = scrapy.Field()
    Fax = scrapy.Field()
    Latitude = scrapy.Field()
    Longitude = scrapy.Field()
    ZipCode = scrapy.Field()
    URL = scrapy.Field()
