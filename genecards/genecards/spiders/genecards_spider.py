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
from genecards.items import GenecardsItem

class GenecardsSpider(CrawlSpider):
    name="genecards"

    allowed_domains=["genecards.org"]

    rsids="rsid,rs3765527,rs4460629,rs4072037,rs2274223,rs3781264,rs13042395,rs738722,rs9841504,rs13361707,rs2294008,rs2976392,rs599839,rs1746048,rs2259816,rs3744700,rs1883832,rs1044317,rs6903956,rs3798220,rs4977574,rs1333049,rs12567209,rs138694505,rs9439519,rs1663689,rs8034191,rs4809957,rs2895680,rs247008,rs2241766,rs6843082,rs11944041,rs12188950,rs2048327,rs381815,rs2681472,rs1801058,rs1799998,rs751141,rs1260326,rs4635554,rs7016880,rs964184,rs505802,rs2231142,rs11722228,rs12498742,rs11726117,rs231359,rs163182,rs2237892,rs7172432,rs391300,rs7612463,rs1501299,rs17584499,rs13153971,rs2244012,rs1063355,rs9303542,rs8170,rs2072590,rs7651446,rs10088218,rs3814113,rs3790844,rs12413624,rs9573163,rs9543325,rs4885093,rs372883,rs1547374,rs5768709,rs2255280,rs7913069,rs2280543,rs2172873,rs12484776,rs13376333,rs5063,rs2106261,rs6499600,rs10033464,rs2200733,rs6843082,rs1805123,rs1799998,rs823156,rs34778348,rs356220,rs4698412,rs1219648,rs9485370,rs10993994,rs10896449,rs902774,rs9600079,rs11649743,rs721048,rs1465618,rs12621278,rs5759167,rs7679673,rs12653946,rs339331,rs16901979,rs10086908,rs1447295,rs1512268,rs6983267,rs4430796,rs4143094,rs7229639,rs4939827,rs7758229,rs6983267,rs8067378,rs13117307"

    start_urls=["http://www.genecards.org/Search/Keyword?queryString="+i for i in rsids.split(',')]
    #start_urls=["http://www.genecards.org/Search/Keyword?queryString=rs2274223","http://www.genecards.org/Search/Keyword?queryString=rs4460629"]
    # ##此处要注意?号的转换，复制过来需要对?号进行转换。
    rules = [
        Rule(LinkExtractor(allow=('http://www.genecards.org/cgi-bin/carddisp.pl\?gene=\w{1,}&keywords=\w{1,}',)),follow=True, callback='parse_item'),
    ]

    def parse_item(self, response):
        sel=Selector(response)
        items=[]
        item=GenecardsItem()
        #获取rsid的值
        item['rsid']=str(response._url).split('=')[2]
        #获取基因名称
        item['genename']=[i.encode('utf-8') for i in sel.xpath("//h1[@id='geneSymbol']/strong/em/text()").extract()]
        #获取gytogeneticband值Cytogenetic band:
        item['gytogeneticband']=[i.encode('utf-8').replace(' by ','') for i in sel.xpath("//dl[@class='dl-horizontal gc-dl-9']/dd/ul[@class='list-inline']/li[1]/text()").extract()]
        items.append(item)
        return items
        '''
        >>> sel.xpath("//dl[@class='dl-horizontal gc-dl-9']/dd/ul[@class='list-inline']/li[1]/text()").extract()
        [u'10q23.33 by ']
        >>> sel.xpath("//h1[@id='geneSymbol']/strong/em/text()").extract()
        [u'PLCE1']
        '''
