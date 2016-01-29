#coding:utf-8
__author__ = 'similarface'
from scrapy.selector import Selector
from cnblogs.items import CnblogsItem
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
class CnblogsSpider(CrawlSpider):
    name = "cnblogs"
    #下载数据延迟1s
    download_delay=1
    #domain限制
    allowed_domains=['cnblogs.com']
    #入口
    start_urls=[
        'http://www.cnblogs.com/rwxwsblog/default.html?page=0'
    ]
    # 定义爬取URL的规则，并指定回调函数为parse_item
    # #此处要注意?号的转换，复制过来需要对?号进行转换。
    rules = [
        ##此处要注意?号的转换，复制过来需要对?号进行转换。
        Rule(LinkExtractor(allow=('/rwxwsblog/default.html\?page=\d{1,}',)),follow=True, callback='parse_item')
    ]
    def parse_item(self, response):
        sel=Selector(response)
        items=[]
        postTitle=sel.css('div.day div.postTitle')
        for index in range(len(postTitle)):
            item=CnblogsItem()
            item['artcleName'] = postTitle[index].css("a").xpath('text()').extract()[0]
            item['artcleUrl'] = postTitle[index].css("a").xpath('@href').extract()[0]
            items.append(item)
        return items
