# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html
from webbrowser import browser

from scrapy import signals
from selenium import webdriver
from time import sleep
from scrapy.http import HtmlResponse
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class MianshiSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class MianshiDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    # def isElementExist(self, element):
    #     flag = True
    #
    #     browser = self.driver
    #     try:
    #         browser.find_element_by_css_selector(element)
    #         return flag
    #
    #     except:
    #         flag = False
    #         return flag

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        # 创建一个webdriver对象
        # flag = True
        chrome_path = r'D:\Program Files\ChromPhantomjs\chromedriver.exe'
        opt = webdriver.ChromeOptions()
        opt.add_argument("--headless")
        driver = webdriver.Chrome(executable_path=chrome_path, options=opt)
        driver.get(request.url)
        sleep(3)
        # 让页面滚动
        js = "var q = document.documentElement.scrollTop=%d"
        distance = 100
        list1 = []
        try:
            for j in range(6):
                for i in range(10):
                    driver.execute_script(js % distance)
                    distance += 1000
                    sleep(0.5)
                driver.find_element_by_css_selector("#iframe072002 > div > ul > li:nth-child(9) > a").click()
                list1.append(driver.page_source)
        except:
            for i in range(10):
                driver.execute_script(js % distance)
                distance += 1000
                sleep(0.5)
            list1.append(driver.page_source)
        str1 = ";".join(str(e) for e in list1)
        res = HtmlResponse(url=driver.current_url, body=str1, encoding='utf-8', request=request)
        return res




    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
