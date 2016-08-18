# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MygeneItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class Drug(scrapy.Item):
    '''
    一脉基因精准用药报告栏目的的药物相关信息
    '''
    #中文名称
    cname = scrapy.Field()
    #英文名称
    ename = scrapy.Field()
    #简述
    description = scrapy.Field()
    #适用疾病
    disease = scrapy.Field()
