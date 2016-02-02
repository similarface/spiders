#coding: utf-8

import re
import json
from urlparse import urlparse


from scrapy.selector import Selector
try:
    from scrapy.spiders import Spider
except:
    from scrapy.spiders import BaseSpider as Spider
from scrapy.utils.response import get_base_url
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors.sgml import SgmlLinkExtractor as sle


from .log import *


'''
1. 默认取sel.css()[0]，如否则需要'__unique':False or __list:True
2. 默认字典均为css解析，如否则需要'__use':'dump'表明是用于dump数据
'''


class CommonSpider(CrawlSpider):

    auto_join_text = True
    ''' # css rule example:
    all_css_rules = {
        '.zm-profile-header': {
            '.zm-profile-header-main': {
                '__use':'dump',
                'name':'.title-section .name::text',
                'sign':'.title-section .bio::text',
                'location':'.location.item::text',
                'business':'.business.item::text',
                'employment':'.employment.item::text',
                'position':'.position.item::text',
                'education':'.education.item::text',
                'education_extra':'.education-extra.item::text',
            }, '.zm-profile-header-operation': {
                '__use':'dump',
                'agree':'.zm-profile-header-user-agree strong::text',
                'thanks':'.zm-profile-header-user-thanks strong::text',
            }, '.profile-navbar': {
                '__use':'dump',
                'asks':'a[href*=asks] .num::text',
                'answers':'a[href*=answers] .num::text',
                'posts':'a[href*=posts] .num::text',
                'collections':'a[href*=collections] .num::text',
                'logs':'a[href*=logs] .num::text',
            },
        }, '.zm-profile-side-following': {
            '__use':'dump',
            'followees':'a.item[href*=followees] strong::text',
            'followers':'a.item[href*=followers] strong::text',
        }
    }
    '''

    # Extract content without any extra spaces.
    # NOTE: If content only has spaces, then it would be ignored.
    '''
    将select选择器选中的数据进行处理返回list
    '''
    def extract_item(self, sels):
        contents = []
        for i in sels:
            #匹配任何不可见字符，包括空格、制表符、换页符等等。等价于[ \f\n\r\t\v]。
            content = re.sub(r'\s+', ' ', i.extract())
            if content != ' ':
                contents.append(content)
        return contents

    def extract_items(self, sel, rules, item):
        for nk, nv in rules.items():
            if nk in ('__use', '__list'):
                continue
            if nk not in item:
                item[nk] = []
            if sel.css(nv):
                # item[nk] += [i.extract() for i in sel.css(nv)]
                # Without any extra spaces:
                item[nk] += self.extract_item(sel.css(nv))
            else:
                item[nk] = []

    # 1. item是一个单独的item，所有数据都聚合到其中 *merge
    # 2. 存在item列表，所有item归入items
    '''
    sel selector选择器
    rules 规则
    item_class
    item None
    items 空的list
    '''
    def traversal(self, sel, rules, item_class, item, items):
        # print 'traversal:', sel, rules.keys()
        if item is None:
            item = item_class()
        if '__use' in rules:
            if '__list' in rules:
                unique_item = item_class()
                self.extract_items(sel, rules, unique_item)
                items.append(unique_item)
            else:
                self.extract_items(sel, rules, item)
        else:
            for nk, nv in rules.items():
                for i in sel.css(nk):
                    self.traversal(i, nv, item_class, item, items)

    DEBUG=True
    def debug(sth):
        if DEBUG == True:
            print(sth)

    def deal_text(self, sel, item, force_1_item, k, v):
        #如果值是已::text结尾 并且 auto_join_text＝True
        if v.endswith('::text') and self.auto_join_text:
            item[k] = ' '.join(self.extract_item(sel.css(v)))
        else:
            _items = self.extract_item(sel.css(v))
            if force_1_item:
                if len(_items) >= 1:
                    item[k] = _items[0]
                else:
                    item[k] = ''
            else:
                item[k] = _items

    keywords = set(['__use', '__list'])

    '''
    sel selector选择器
    rules 规则 是一个字典
    item_class 空字典
    item None
    items 空的list
    '''
    def traversal_dict(self, sel, rules, item_class, item, items, force_1_item):
        #import pdb; pdb.set_trace()
        item = {}
        for k, v in rules.items():
            #如果值不是一个字典
            if type(v) != dict:
                #
                if k in self.keywords:
                    continue
                if type(v) == list:
                    continue
                #
                self.deal_text(sel, item, force_1_item, k, v)
                #import pdb;pdb.set_trace()
            else:
                item[k] = []
                for i in sel.css(k):
                    #print(k, v)
                    self.traversal_dict(i, v, item_class, item, item[k], force_1_item)
        items.append(item)

    '''
    (response,self.list_css_rules,dict,True)
    sel 表示selecter 选择器
    rules 规则 是一个字典
    item_class 字典
    force_1_item True
    '''
    def dfs(self, sel, rules, item_class, force_1_item):
        #如果选择器是None 返回[]
        if sel is None:
            return []
        #
        items = []
        #如果item_class 不是字典
        if item_class != dict:
            #
            self.traversal(sel, rules, item_class, None, items, force_1_item)
        else:
            #是字典的情况下
            self.traversal_dict(sel, rules, item_class, None, items, force_1_item)

        return items

    def parse_with_rules(self, response, rules, item_class, force_1_item=False):
        return self.dfs(Selector(response), rules, item_class, force_1_item)

    ''' # use parse_with_rules example:
    def parse_people_with_rules(self, response):
        item = self.parse_with_rules(response, self.all_css_rules, ZhihuPeopleItem)
        item['id'] = urlparse(response.url).path.split('/')[-1]
        info('Parsed '+response.url) # +' to '+str(item))
        return item
    '''