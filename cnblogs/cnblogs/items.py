# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field

class CnblogsItem(scrapy.Item):
    '''
    你要爬去数据对象化
    '''
    artcleName=Field()
    artcleUrl=Field()


