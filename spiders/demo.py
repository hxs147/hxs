# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from Lianjia_new.items import LianjiaNewItem

class DemoSpider(scrapy.Spider):
    name = 'demo'
    # allowed_domains = ['cq.ke.com/ershoufang/']
    
    def start_requests(self):
        start_urls = 'https://cq.ke.com/ershoufang/'         # 更改城市名称就可以爬取指定城市的租房信息，如成都：cd，苏州是su
        ua = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6756.400 QQBrowser/10.3.2473.400'}
        for i in range(1, 101):
            if i == 1:
                url = start_urls   
            else:
                url = "https://cq.ke.com/ershoufang/pg" + str(i)
            yield Request(url, headers = ua, callback = self.parse_house)

    def parse_house(self, response):
        ua = {'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36'}
        house_list = response.xpath('//a[@class="CLICKDATA maidian-detail"]/@href').extract()
        for i in range(len(house_list)):
            yield Request(url = house_list[i], headers = ua, callback = self.parse)

    def parse(self, response):
        item = LianjiaNewItem()
        item['title'] = response.xpath('//h1[@class="main"]/text()').extract()
        item['price'] = response.xpath('//span[@class="total"]/text()').extract()
        item['info'] = response.xpath('//span[@class="info"]/a/text()').extract()       
        item['model'] = response.xpath('//div[@class="content"]/ul/li[1]/text()').extract()        
        item['floor'] = response.xpath('//div[@class="content"]/ul/li[2]/text()').extract()
        item['area'] = response.xpath('//div[@class="content"]/ul/li[3]/text()').extract()
        item['structure'] = response.xpath('//div[@class="content"]/ul/li[4]/text()').extract()
        item['type1'] = response.xpath('//div[@class="content"]/ul/li[6]/text()').extract()
        item['toward'] = response.xpath('//div[@class="content"]/ul/li[7]/text()').extract()
        item['elevator'] = response.xpath('//div[@class="content"]/ul/li[11]/text()').extract()
        for i in range(len(item['title'])):
            print(item['title'][i])
            print(item['price'][i])
            for j in item['info']:
                print(j + '\t')
            print(item['model'][i])
            for x in item['floor']:
                print(x + '\t')
            print(item['area'][i])
            print(item['strcture'][i])
            print(item['type1'][i])
            print(item['toward'][i])
            print(item['elevator'][i])
            print('-'*80)
            
        yield item
