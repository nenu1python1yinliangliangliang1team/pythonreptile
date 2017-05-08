# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from taobao.items import TaobaoItem
import urllib.request
import re
class TbSpider(scrapy.Spider):
    name = "tb"
    allowed_domains = ["taobao.com"]
    start_urls = (
        'http://www.taobao.com/',
    )

    def parse(self, response):
       pass
    def page(self,response):
       pass
    def next(self,response):
        pass
