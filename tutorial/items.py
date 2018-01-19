# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class InformationItem(scrapy.Item):
    urls = scrapy.Field()


class FileItem(scrapy.Item):
    file_urls = scrapy.Field()
    file = scrapy.Field()
    name = scrapy.Field()