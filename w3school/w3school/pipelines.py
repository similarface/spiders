# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import codecs
class W3SchoolPipeline(object):
    def __init__(self):
        self.file=codecs.open('w3school_data_utf8.json', 'wb', encoding='utf-8')
    #会遍历处理每一个item
    def process_item(self, item, spider):
        #JSON
        line=json.dumps(dict(item))+'\n'
        #写入文件
        self.file.write(line.decode("unicode_escape"))
        return item
