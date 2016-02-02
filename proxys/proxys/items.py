# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Item,Field

'''
获取免费代理服务器
'''
class FreeProxyListItem(scrapy.Item):
    #IP地址
    ip=Field()
    #端口
    port=Field()
    #地区
    code=Field()
    #城市
    country=Field()
    #是否匿名
    anonymity=Field()
    google = Field()
    https = Field()
    last_checked = Field()
