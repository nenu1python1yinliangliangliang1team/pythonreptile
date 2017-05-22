# -*- coding: utf-8 -*-
import pymysql
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class TaobaoPipeline(object):
    def __init__(self):
        #self.conn=pymysql.connect(host="127.0.0.1",user="root",passwd="root",db="csdn")
       pass
    def process_item(self, item, spider):
        try:
            title=item["title"][0]
            link=item["link"]
            price=item["price"][0]
            comment=item["comment"][0]
            print(title)
            print(price)
            print(comment)
            sql="insert into taob(title,link,price,comment) values('"+title+"','"+link+"','"+price+"','"+comment+"')"
            self.conn.query(sql)
            return item
        except Exception as err:
            pass
    def close_spider(self):
        self.conn.close()
