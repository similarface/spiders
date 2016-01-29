# -*- coding: utf-8 -*-
BOT_NAME = 'cnblogs'
SPIDER_MODULES = ['cnblogs.spiders']
NEWSPIDER_MODULE = 'cnblogs.spiders'
ITEM_PIPELINES = {
   'cnblogs.pipelines.CnblogsPipeline': 300,
}
COOKIES_ENABLED = False