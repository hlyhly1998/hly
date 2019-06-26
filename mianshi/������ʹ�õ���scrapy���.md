## 该爬虫使用的是scrapy框架

这些网页都是需要动态加载才可以爬取到数据的,在scrapy中selenium部分代码在middlewares.py文件中实现

```
chrome_path = r'D:\Program Files\ChromPhantomjs\chromedriver.exe'
opt = webdriver.ChromeOptions()
opt.add_argument("--headless")
driver = webdriver.Chrome(executable_path=chrome_path, options=opt)
driver.get(request.url)
sleep(3)
# 让页面滚动
js = "var q = document.documentElement.scrollTop=%d"
distance = 100
for i in range(10):
    driver.execute_script(js % distance)
    distance += 1000
    sleep(0.5)
```

```
driver.find_element_by_css_selector("#iframe072002 > div > ul > li:nth-child(9) > a").click() # 点击事件
```



保存到mysql中的部分代码

```
class MianshiPipeline(object):
    def open_spider(self, spider):
        self.db = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='nanjing', charset='utf-8')
        self.cursor = self.db.cursor()
    def process_item(self, item, spider):
        sql = "INSERT INTO nanjing VALUES (NULL ,'%s','%s','%s','%','%s','%s')" % (item['Transfer_date'], item['Plot_number'], item['Parcel_name'], item['Land_area'], item['Volme_rate'], item['Winner'])
        self.cursor.execute(sql)
        self.db.commit()
        return item
    def close_spider(self, spider):
        self.cursor.close()
        self.db.close()
```

爬虫部分代码

```
解析二级页面
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
```