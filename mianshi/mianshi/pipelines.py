# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
import csv
class MianshiPipeline(object):
    # def open_spider(self, spider):
    #     self.db = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='nanjing', charset='utf-8')
    #     self.cursor = self.db.cursor()
    # def process_item(self, item, spider):
    #     sql = "INSERT INTO nanjing VALUES (NULL ,'%s','%s','%s','%','%s','%s')" % (item['Transfer_date'], item['Plot_number'], item['Parcel_name'], item['Land_area'], item['Volme_rate'], item['Winner'])
    #     self.cursor.execute(sql)
    #     self.db.commit()
    #     return item
    # def close_spider(self, spider):
    #     self.cursor.close()
    #     self.db.close()
    def open_spider(self, spider):
        self.csv_file = open("nanjing.csv", 'w', encoding='utf-8')
        # 定义一个列表，用于整合所有的信息
        self.csv_items = []

    def process_item(self, item, spider):
        # 定义一个item用于整合每一个item的信息
        item_csv = []
        item_csv.append(item['Parcel_name'])
        item_csv.append(item["Transfer_date"])
        item_csv.append(item["Plot_number"])
        item_csv.append(item["Land_area"])
        item_csv.append(item['Volme_rate'])
        item_csv.append(item['Winner'])
        self.csv_items.append(item_csv)
        return item

    def close_spider(self, spider):
        writer = csv.writer(self.csv_file)
        writer.writerow(["Parcel_name", "Transfer_date", "Plot_number", "Land_area", "Volme_rate",'Winner'])
        writer.writerows(self.csv_items)

        self.csv_file.close()
