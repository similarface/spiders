# coding:utf-8
__author__ = 'similarface'
import unittest

from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.linkextractors.sgml import SgmlLinkExtractor
from scrapy import Request, FormRequest


class MygeneDrugReaction(CrawlSpider):
    name = 'drugeaction'

    allowed_domains = ['www.mygene.com']
    start_urls = [
        'https://www.mygene.com/Home/Genekang/drug_reaction.html'
    ]

    rules = (
        Rule(SgmlLinkExtractor(allow = ('*', )), callback = 'parse_page', follow = True)
    )

    # 请求头
    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.8",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36",
        "Host": "www.mygene.com",
        "Content-Length": 36,
        "Origin": "https://www.mygene.com",
        "X-Requested-With": "XMLHttpRequest",
        "Referer": "https://www.mygene.com/Home/Public/login.html"
    }
    # Cookie: PHPSESSID=u4hca0mhujv07nri9d36cnah60; Hm_lvt_13b1c64a0657e0bd740411edb33fc95e=1456469464; Hm_lpvt_13b1c64a0657e0bd740411edb33fc95e=1456470984; error_time=2

    def start_requests(self):
        return [Request("https://www.mygene.com/Home/Public/login.html", meta={'cookiejar': 1},
                        callback=self.post_login)]  # 添加了meta

    def post_login(self, response):
        # 登陆成功后, 会调用after_login回调函数
        print 'Preparing login'
        # 下面这句话用于抓取请求网页后返回网页中的_xsrf字段的文字, 用于成功提交表单
        a = response
        family = Selector(response).xpath('//input[@name="family"]/@value').extract()[0]
        print family
        return FormRequest.from_response(response,
                                         meta={
                                             'cookiejar': response.meta['cookiejar']
                                         },
                                         headers=self.headers,
                                         formdata={
                                             'family': '',
                                             'username': 'Ywj',
                                             'password': '198998',
                                             'remember': 1
                                         },
                                         callback=self.after_login
                                         )

    def after_login(self, response):
        print('good')
        a = response
        b = 1
        c = 2
        return
        # for url in self.start_urls:
        #     yield self.make_requests_from_url(url)

    def parse_page(self, response):
        problem = Selector(response)

        # problem = Selector(response)
        # item = MygeneDrugReaction()
        # item['url'] = response.url
        # item['name'] = problem.xpath('//span[@class="name"]/text()').extract()
        # print item['name']
        # item['title'] = problem.xpath('//h2[@class="zm-item-title zm-editable-content"]/text()').extract()
        # item['description'] = problem.xpath('//div[@class="zm-editable-content"]/text()').extract()
        # item['answer'] = problem.xpath('//div[@class=" zm-editable-content clearfix"]/text()').extract()
        # return item


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
