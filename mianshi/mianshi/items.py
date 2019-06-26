# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MianshiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 出让日期
    Transfer_date = scrapy.Field()
    # 地块编号
    Plot_number = scrapy.Field()
    # 地块名称
    Parcel_name = scrapy.Field()
    # 土地面积
    Land_area = scrapy.Field()
    # 容积率
    Volme_rate = scrapy.Field()
    # 竞得人
    Winner = scrapy.Field()

