# -*- coding: utf-8 -*-
import scrapy
from mianshi.items import MianshiItem


class NanjingSpider(scrapy.Spider):
    name = 'nanjing'
    allowed_domains = ['ggzy.njzwfw.gov.cn']

    start_urls = ['http://ggzy.njzwfw.gov.cn/njweb/tdkc/072002/landmineral2.html']
    # /njweb/tdkc/072002/20190612/d33a839f-892f-4ad8-8c4c-1068196603ab.html
    # rules = {
    #     Rule(LinkExtractor(allow=r'njweb/tdkc/\d+/\d+/\w[-]+\.html'), callback='parse_item', follow=True),
    # }


    def parse(self, response):
        link_list = response.xpath("//*[@id='iframe072002']/ul/li/@onclick").extract()
        for data in link_list:
            link = data.split("'")[1]
            next_url = 'http://ggzy.njzwfw.gov.cn' + link
            # print(next_url, item)
            yield scrapy.Request(url=next_url, callback=self.parse_next)

    # 解析二级页面
    def parse_next(self, response):
        item = MianshiItem()
        # 地块名称
        item['Parcel_name'] =response.xpath("//div[2]/div[2]/div/div[1]/h1/text()").extract_first()
        # 出让日期--成交时间
        item['Transfer_date'] = response.xpath("//div[2]/div[2]/div/div[1]/div/table/tbody/tr[5]/td[2]/text()").extract_first()
        # # 地块编号
        item['Plot_number'] = response.xpath(".//div/table/tbody/tr[1]/td[2]/text()").extract_first()
        # 土地面积
        item['Land_area'] = response.xpath("//div[2]/div[2]/div/div[1]/div/table/tbody/tr[3]/td[4]/text()").extract_first()
        # 容积率
        item['Volme_rate'] = response.xpath("//div[2]/div[2]/div/div[1]/div/table/tbody/tr[2]/td[2]/text()").extract_first()
        # 竞得人
        item['Winner'] = response.xpath("//div[2]/div[2]/div/div[1]/div/table/tbody/tr[6]/td[2]/text()").extract_first()
        yield item




