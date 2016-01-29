#coding:utf-8
__author__ = 'similarface'

from scrapy.spiders import Spider
from scrapy.selector import Selector
from logging import log
from w3school.items import W3SchoolItem
'''
对www.w3school.com.cn的网站的一些爬取
'''
class W3schoolSpider(Spider):
    name="w3school"
    allowed_domains = ["w3school.com.cn"]
    #访问url的入口
    start_urls = [
        "http://www.w3school.com.cn/xml/xml_syntax.asp"
    ]

    def parse(self, response):
        sel=Selector(response)
        #这儿的ul加了1表示div[navsecond]下的第一个ul标签
        sites=sel.xpath('//div[@id="navsecond"]/div[@id="course"]/ul[1]/li')
        #item的容器
        items=[]
        #选择器结果遍历
        for site in sites:
            item=W3SchoolItem()
            #获取a标签的文本
            title = site.xpath('a/text()').extract()
            #获取a标签的href属性
            link = site.xpath('a/@href').extract()
            #获取a标签的title属性
            desc = site.xpath('a/@title').extract()
            #
            item['title'] = [t.encode('utf-8') for t in title]
            #response.urljoin 会加上访问的domain
            item['link'] = [response.urljoin(l.encode('utf-8')) for l in link]
            item['desc'] = [d.encode('utf-8') for d in desc]
            items.append(item)
            print("Appending item...")
        print("Append done.")
        return items