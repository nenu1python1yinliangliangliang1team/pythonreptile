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
        key="零食"
        for i in range(0,101):
            url="https://s.taobao.com/search?q="+str(key)+"&s="+str(44*i)
            yield Request(url=url,callback=self.page)
    def page(self,response):
        body=response.body.decode("utf-8","ignore")
        patid='"nid":"(.*?)"'
        allid=re.compile(patid).findall(body)
        print(allid)
        for j in range(0,len(allid)):
            thisid=allid[j]
            url1="https://item.taobao.com/item.htm?id="+str(thisid)
            yield Request(url=url1,callback=self.next)
    def next(self,response):
        item=TaobaoItem()
        item["title"]=response.xpath("//h3[@class='tb-main-title']/@data-title").extract()
        item["link"]=response.url
        item["price"]=response.xpath("//em[@class='tb-rmb-num']/text()").extract()
        patid='id=(.*?)$'
        thisid=re.compile(patid).findall(response.url)[0]
        commenturl="https://rate.taobao.com/detailCount.do?callback=jsonp100&itemId="+str(thisid)
        #print(commenturl)
        commentdata=urllib.request.urlopen(commenturl).read().decode("utf-8","ignore")
        #print(commentdata)
        pat='"count":(.*?)}'
        item["comment"]=re.compile(pat).findall(commentdata)
        #print(item["comment"])
        yield item
