# coding=utf-8

import scrapy
import os
from xlwt import *
from scrapy.http import FormRequest
from get_gp_top_scrapy.items import GetGpTopScrapyItem


class GetInTop(scrapy.Spider):
    # 创建文件夹，用于保存生成的资源文件
    if os.path.exists("E:\\get_gp_in_and_id_top540_scrapy"):
        pass
    else:
        os.chdir("E:\\")
        os.mkdir("get_gp_in_and_id_top540_scrapy")
    os.chdir("E:\\get_gp_in_and_id_top540_scrapy")

    # scrapy运行的唯一标识，在pipeines中识别
    name = "in_top_apps"
    allowed_domains = ["play.google.com"]  # 搜索的域名范围，也就是爬虫的约束区域，规定爬虫只爬取这个域名下的网页
    start_urls = [
        "https://play.google.com/store/apps/collection/topselling_free?gl=in&hl=en"
    ]  # 开始爬取的地址

    # 每次爬取的数量
    num = 60
    # 每次爬取的起始位置
    start_list = ["60", "120", "180", "240", "300", "360", "420", "480", "540"]
    # 控制post请求的次数
    i = -1
    urls = []
    # 处理url的响应
    def parse(self, response):
        # print(response.body_as_unicode())
        # 创建查询对象
        sel = scrapy.Selector(response)
        posts = sel.xpath(
            ".//*[@id='body-content']/div/div/div[@class='main-content']/div/div/div/div[@class='id-card-list card-list two-cards']/"
            "div[@class='card no-rationale square-cover apps small']")
        for a in posts:
            # 循环获取posts中的每个数据
            item = GetGpTopScrapyItem()
            app_package_url = a.xpath("div/div[@class='cover']/a/@href").extract()
            app_name_id = a.xpath("div/div[@class='cover']/a/@aria-label").extract()
            # 获取应用id
            item["in_app_id"] = app_name_id[0].split(".")[0].replace(" ", "")
            # 获取应用名字
            item["in_app_name"] = app_name_id[0].split(".")[1].lstrip().rstrip()
            # 获取应用包名
            item["in_app_package"] = app_package_url[0].split("?id=")[1].replace(" ", "")
            # 获取应用的url链接
            in_app_url = "https://play.google.com" + app_package_url[0]
            # 访问每一个应用的链接
            yield scrapy.Request(url=in_app_url, meta={'key': item}, callback=self.parse_category)
        self.i = self.i + 1
        # post请求循环获取
        if self.i < len(self.start_list) - 1:
            # 设置提交的表单
            formadata = {'start': self.start_list[self.i], 'num': '60'}
            # post请求
            yield FormRequest("https://play.google.com/store/apps/collection/topselling_free?gl=in&hl=en&authuser=0",
                              formdata=formadata,
                              callback=self.parse)

    def parse_category(self, response):
        # 创建查询对象
        sel = scrapy.Selector(response)
        item = response.meta["key"]
        item["in_app_updated"] = sel.xpath(".//*[@id='body-content']/div/div/div[1]/div/div/div[2]/div[@class='meta-info']/div[@itemprop='datePublished']/text()").extract()
        item["in_app_version"] = sel.xpath(".//*[@id='body-content']/div/div/div[1]/div/div/div[2]/div[@class='meta-info']/div[@itemprop='softwareVersion']/text()").extract()
        item["in_app_requirse_android"] = sel.xpath(".//*[@id='body-content']/div/div/div[1]/div/div/div[2]/div[@class='meta-info']/div[@itemprop='operatingSystems']/text()").extract()
        yield item
