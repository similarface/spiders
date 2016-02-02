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
        "http://free-proxy-list.net/",
    ]
    #
    rules = [
        Rule(LinkExtractor(allow=("/$",)),callback='parse_next',follow=True),
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
    #解析
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


'''
抓取http://proxylist.hidemyass.com/ 的网站的代理IP
'''
class hidemyassSpider(CrawlSpider):
    name = "hidemyass"
    allowed_domains = ["hidemyass.com"]
    start_urls = [
        "http://proxylist.hidemyass.com",
    ]
    #http://proxylist.hidemyass.com/2#listable
    rules = [
        Rule(LinkExtractor(allow=("\d{1,}#listable")), callback='parse_1', follow=True),
    ]

    # xpath: note that the paras are not rendered, so we cannot use it directly
    # we should 1. render it or 2. write some logic to filter the real displayed node.
    # n[2].css('td:nth-child(2)').xpath(".//*[not(contains(@style,'display:none'))]/text()")
    # list_css_rules = {
    #     'tbody tr': {
    #         'ip': "td:nth-child(2)", #, "xpath:.//*[not(contains(@style,'display:none'))]/text()"],
    #         'port': 'td:nth-child(3)::text',
    #         'code': 'td:nth-child(8)::text',
    #         'country': 'td:nth-child(4)::text',
    #         'speed': 'td:nth-child(5) *::attr(value)',
    #         'connection_time': 'td:nth-child(6) *::attr(value)',
    #         'type': 'td:nth-child(7)::text',
    #         'last_checked': '.timestamp span::text',
    #     }
    # }

    def parse_1(self, response):
        print('Parse '+response.url)
        items = []
        n = response.css('tbody tr')
        import pdb; pdb.set_trace()
        x = self.parse_with_rules(response, self.list_css_rules, dict, True)
        x = x[0]['tbody tr']
        for i in x:
           item = FreeProxyListItem()
           for k, v in i.items():
               item[k] = v
           items.append(item)
        return items
        #return self.parse_with_rules(response, self.css_rules, proxylistItem)
