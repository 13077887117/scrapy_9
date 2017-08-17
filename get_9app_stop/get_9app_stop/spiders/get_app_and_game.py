# coding=utf-8

import scrapy
from get_9app_stop.items import Get9AppStopItem
from scrapy.http import Request
from scrapy.crawler import CrawlerProcess


'''
无视
'''
class GetAppsDemo_APPS(scrapy.Spider):
    # name = "lyapps"
    # allowed_domains = ["cnblogs.com"]
    allowed_domains = ["www.9apps.com"]
    start_urls = [
        "https://www.9apps.com/top-android-apps-1/"
    ]

    num = 1
    next_list = []

    def parse(self, response):
        sel = scrapy.Selector(response)
        self.num += 1
        posts = sel.xpath(
            "/html/body/div[2]/div/div[@class='page-section']/div[@class='content-with-title']/div[@class='content border-table hot-app-list']/ul/li")
        for p in posts:
            item = Get9AppStopItem()
            item["app_name"] = p.xpath("div/a/div[@class='info']/span/text()").extract()
            item["app_package"] = p.xpath("div/div[@class='download']/a/@href").extract()
            item["app_size"] = p.xpath("div/a/div[@class='info']/p/span[@class='size']/text()").extract()
            item["app_version"] = p.xpath("div/a/div[@class='info']/p/span[@class='version']/text()").extract()
            yield item
            # print(item["app_name"], "***", item["app_package"], "***", item["app_size"], "***", item["app_version"])
        #     /html/body/div[2]/div/div[3]/div[2]
        #      html/body/div[2]/div/div[3]/div[2]/a[8]
        next_package = sel.xpath(
            "/html/body/div[2]/div/div[@class='page-section']/div[@class='pagination-pages-new pagination-pages']/a/text()").extract()[-2]

        if self.num < int(next_package) + 1:
            yield Request(url="https://www.9apps.com/top-android-apps-" + str(self.num) + "/", callback=self.parse)


class GetAppsDemo_GAME(scrapy.Spider):
    # name = "lygames"
    # allowed_domains = ["cnblogs.com"]
    allowed_domains = ["www.9apps.com"]
    start_urls = [
        "https://www.9apps.com/top-android-games-1/"
    ]

    num = 1
    next_list = []

    def parse(self, response):
        sel = scrapy.Selector(response)
        self.num += 1
        posts = sel.xpath(
            "/html/body/div[2]/div/div[@class='page-section']/div[@class='content-with-title']/div[@class='content border-table hot-app-list']/ul/li")
        next_package = sel.xpath(
            "/html/body/div[2]/div/div[@class='page-section']/div[@class='pagination-pages-new pagination-pages']/a/text()").extract()[-2]
        for p in posts:
            item = Get9AppStopItem()
            item["game_name"] = p.xpath("div/a/div[@class='info']/span/text()").extract()
            item["game_package"] = p.xpath("div/div[@class='download']/a/@href").extract()
            item["game_size"] = p.xpath("div/a/div[@class='info']/p/span[@class='size']/text()").extract()
            item["game_version"] = p.xpath("div/a/div[@class='info']/p/span[@class='version']/text()").extract()
            yield item
            # print(item["app_name"], "***", item["app_package"], "***", item["app_size"], "***", item["app_version"])



        if self.num < int(next_package) + 1:
            yield Request(url="https://www.9apps.com/top-android-games-" + str(self.num) + "/", callback=self.parse)


# process = CrawlerProcess()
# process.crawl(GetAppsDemo_APPS)
# process.crawl(GetAppsDemo_GAME)
# process.start() # the script will block here until all crawling jobs are finished
