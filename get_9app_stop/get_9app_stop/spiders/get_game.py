# coding=utf-8

import scrapy
from get_9app_stop.items import Get9AppStopItem
from scrapy.http import Request
from scrapy.crawler import CrawlerProcess

'''
获取9apps中的app
'''
class GetAppsDemo_GAME(scrapy.Spider):
    # scrapy运行的唯一标识，在pipeines中识别
    name = "lygames"
    # 搜索的域名范围，也就是爬虫的约束区域，规定爬虫只爬取这个域名下的网页
    allowed_domains = ["www.9apps.com"]
    # 开始爬取的地址
    start_urls = [
        "https://www.9apps.com/top-android-games-1/"
    ]
    # 控制循环的次数
    num = 1

    # 处理url的响应
    def parse(self, response):
        # 创建查询对象
        sel = scrapy.Selector(response)
        self.num += 1
        posts = sel.xpath(
            "/html/body/div[2]/div/div[@class='page-section']/div[@class='content-with-title']/div[@class='content border-table hot-app-list']/ul/li")
        for p in posts:
            # 循环获取posts中的每个数据
            item = Get9AppStopItem()
            # 获取游戏名
            item["game_name"] = p.xpath("div/a/div[@class='info']/span/text()").extract()
            # 获取游戏包名
            item["game_package"] = p.xpath("div/div[@class='download']/a/@href").extract()
            # 获取游戏大小
            item["game_size"] = p.xpath("div/a/div[@class='info']/p/span[@class='size']/text()").extract()
            # 获取游戏版本号
            item["game_version"] = p.xpath("div/a/div[@class='info']/p/span[@class='version']/text()").extract()
            # 将item传入pipelines中
            yield item
            # print(item["app_name"], "***", item["app_package"], "***", item["app_size"], "***", item["app_version"])

        next_package = sel.xpath(
            "/html/body/div[2]/div/div[@class='page-section']/div[@class='pagination-pages-new pagination-pages']/a/text()").extract()[
            -2]
        # 获取所有页数中的资源
        if self.num < int(next_package) + 1:
            yield Request(url="https://www.9apps.com/top-android-games-" + str(self.num) + "/", callback=self.parse)
