#coding:utf-8
__author__ = 'similarface'
import re,json,urllib,pdb
from urlparse import urlparse
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.utils.response import get_base_url
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors.sgml import SgmlLinkExtractor
from scrapy.linkextractors import LinkExtractor
from proxys.items import FreeProxyListItem
from common.log import *
from common.spider import CommonSpider

class ProxyListSpider(CommonSpider):
    name="proxylist"

    allowed_domains=["free-proxy-list.net"]

    start_urls = [
        "https://free-proxy-list.net/",
    ]

    rules = [
        Rule(LinkExtractor(allow=("/$")),callback='parse_next',follow=True),
    ]

    list_css_rules={
        'tbody tr': {
            'ip': 'td:nth-child(1)::text',
            'port': 'td:nth-child(2)::text',
            'code': 'td:nth-child(3)::text',
            'country': 'td:nth-child(4)::text',
            'anonymity': 'td:nth-child(5)::text',
            'google': 'td:nth-child(6)::text',
            'https': 'td:nth-child(7)::text',
            'last_checked': 'td:nth-child(8)::text',
        }
    }

    def parse_next(self,response):
        info('Parse '+response.url)
        items=[]

        x=self.parse_with_rules(response,self.list_css_rules,dict,True)

        x=x[0]['tbody tr']
        pp.pprint(x)

        for i in x:
            item=FreeProxyListItem()
            for k,v in i.items():
                item[k]=v
            items.append(item)
        return items


