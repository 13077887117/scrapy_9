# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os
from xlwt import *

'''
处理数据
需要在settings中设置
ITEM_PIPELINES = {
   'get_gp_top_scrapy.pipelines.GetGpTopScrapyPipeline': 300,
}
'''
class GetGpTopScrapyPipeline(object):

    # 当spider被开启时，这个方法被调用
    def open_spider(self, spider):
        # 根据spider.name来区分spider
        if spider.name == "in_top_apps":
            self.book = Workbook(encoding='utf-8')
            self.sheet1 = self.book.add_sheet("in_top_apps")
            self.sheet1.write(0, 0, "ID")
            self.sheet1.write(0, 1, "应用名")
            self.sheet1.write(0, 2, "包名")
            self.sheet1.write(0, 3, "Updated")
            self.sheet1.write(0, 4, "Version")
            self.sheet1.write(0, 5, "Requirse Android")
        elif spider.name == "id_top_apps":
            self.book = Workbook(encoding='utf-8')
            self.sheet2 = self.book.add_sheet("id_top_apps")
            self.sheet2.write(0, 0, "ID")
            self.sheet2.write(0, 1, "应用名")
            self.sheet2.write(0, 2, "包名")
            self.sheet2.write(0, 3, "Updated")
            self.sheet2.write(0, 4, "Version")
            self.sheet2.write(0, 5, "Requirse Android")


    # 将数据写入文件
    def process_item(self, item, spider):
        if spider.name == "in_top_apps":
            self.sheet1.write(int(item["in_app_id"]), 0, item["in_app_id"])
            self.sheet1.write(int(item["in_app_id"]), 1, item["in_app_name"])
            self.sheet1.write(int(item["in_app_id"]), 2, item["in_app_package"])

            if len(item["in_app_updated"]) == 0 or item["in_app_updated"][0] == " ":
                self.sheet1.write(int(item["in_app_id"]), 3, "N/A")
            else:
                self.sheet1.write(int(item["in_app_id"]), 3, item["in_app_updated"])
            if len(item["in_app_version"]) == 0:
                self.sheet1.write(int(item["in_app_id"]), 4, "N/A")
            else:
                self.sheet1.write(int(item["in_app_id"]), 4, item["in_app_version"][0].replace(" ", ""))
            if len(item["in_app_requirse_android"]) == 0:
                self.sheet1.write(int(item["in_app_id"]), 5, "N/A")
            else:
                self.sheet1.write(int(item["in_app_id"]), 5, item["in_app_requirse_android"][0].replace(" ", ""))
            # print('*-*-* item["in_app_id"]', item["in_app_id"])
        elif spider.name == "id_top_apps":
            # print("$$$$$", item["id_app_id"])
            self.sheet2.write(int(item["id_app_id"]), 0, item["id_app_id"])
            self.sheet2.write(int(item["id_app_id"]), 1, item["id_app_name"])
            self.sheet2.write(int(item["id_app_id"]), 2, item["id_app_package"])

            if len(item["id_app_updated"]) == 0 or item["id_app_updated"][0] == " ":
                self.sheet2.write(int(item["id_app_id"]), 3, "N/A")
            else:
                self.sheet2.write(int(item["id_app_id"]), 3, item["id_app_updated"])
            if len(item["id_app_version"]) == 0:
                self.sheet2.write(int(item["id_app_id"]), 4, "N/A")
            else:
                self.sheet2.write(int(item["id_app_id"]), 4, item["id_app_version"][0].lstrip().rstrip())
            if len(item["id_app_requirse_android"]) == 0:
                self.sheet2.write(int(item["id_app_id"]), 5, "N/A")
            else:
                self.sheet2.write(int(item["id_app_id"]), 5, item["id_app_requirse_android"][0].lstrip().rstrip())
            # print('*-*-* item["id_app_id"]', item["id_app_id"])
        return item

    # 当spider关闭时，这个方法被调用
    def close_spider(self, spider):
        # 保存文件
        if spider.name == "in_top_apps":
            filename = "Gp - in_top_apps资源.xls"
            print("------------", filename, "文件保存路径", os.getcwd(), "------------")
            self.book.save(filename)
        elif spider.name == "id_top_apps":
            filename = "Gp - id_top_apps资源.xls"
            print("------------", filename, "文件保存路径", os.getcwd(), "------------")
            self.book.save(filename)
