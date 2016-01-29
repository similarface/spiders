# -*- coding: utf-8 -*-
BOT_NAME = 'w3school'
SPIDER_MODULES = ['w3school.spiders']
NEWSPIDER_MODULE = 'w3school.spiders'
#300表示权值0-1000
ITEM_PIPELINES = {
   'w3school.pipelines.W3SchoolPipeline': 300,
}
