# -*- coding: utf-8 -*-


BOT_NAME = 'proxys'

SPIDER_MODULES = ['proxys.spiders']
NEWSPIDER_MODULE = 'proxys.spiders'


DOWNLOADER_MIDDLEWARES = {
   # 'misc.middleware.CustomHttpProxyMiddleware': 400,
    'misc.middleware.CustomUserAgentMiddleware': 401,
}

ITEM_PIPELINES = {
    #json存储
    'proxylist.pipelines.JsonWithEncodingPipeline': 300,
    #redis存储
    #'proxylist.pipelines.RedisPipeline': 301,
    #mysql存储
    #'proxylist.pipelines.MySQLStorePipeline': 302
}

LOG_LEVEL = 'INFO'

#限制下载延迟一秒
DOWNLOAD_DELAY = 1