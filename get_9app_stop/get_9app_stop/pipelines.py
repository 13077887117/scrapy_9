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
   'get_9app_stop.pipelines.Get9AppStopPipeline': 300,
}
'''
class Get9AppStopPipeline(object):

    # 运行两次
    def __init__(self):
        # app应用id
        self.app_num = 1
        # game应用id
        self.game_num = 1
        # 创建文件夹
        if os.path.exists("E:\\get_9apps_all_top_scrapy"):
            pass
        else:
            os.chdir("E:\\")
            os.mkdir("get_9apps_all_top_scrapy")
        os.chdir("E:\\get_9apps_all_top_scrapy")

    # 当spider被开启时，这个方法被调用
    def open_spider(self, spider):
        if spider.name == "lyapps":
            self.book = Workbook(encoding='utf-8')
            self.sheet1 = self.book.add_sheet("lyapps")
            self.sheet1.write(0, 0, "ID")
            self.sheet1.write(0, 1, "应用名")
            self.sheet1.write(0, 2, "包名")
            self.sheet1.write(0, 3, "大小")
            self.sheet1.write(0, 4, "版本")
        elif spider.name == "lygames":
            self.book = Workbook(encoding='utf-8')
            self.sheet2 =self.book.add_sheet("lygames")
            self.sheet2.write(0, 0, "ID")
            self.sheet2.write(0, 1, "应用名")
            self.sheet2.write(0, 2, "包名")
            self.sheet2.write(0, 3, "大小")
            self.sheet2.write(0, 4, "版本")

    # 将数据写入文件
    def process_item(self, item, spider):
        if spider.name == "lyapps":
            if item["app_name"] and item["app_package"] and item["app_size"] and item["app_version"]:
                self.sheet1.write(self.app_num, 0, self.app_num)
                self.sheet1.write(self.app_num, 1, item["app_name"])
                if item["app_package"] == ['http://www.9apps.com/down/pc4.apk']:
                    self.sheet1.write(self.app_num, 2, "com.mobile.indiapp")
                else:
                    self.sheet1.write(self.app_num, 2, item["app_package"][0].replace("/jump/down/", "").replace(
                "/app/?f=9_0_1_0_1", ""))
                self.sheet1.write(self.app_num, 3, item["app_size"])
                self.sheet1.write(self.app_num, 4, item["app_version"])
            else:
                self.sheet1.write(self.app_num, 0, self.app_num)
                self.sheet1.write(self.app_num, 1, "null")
                self.sheet1.write(self.app_num, 2, "null")
                self.sheet1.write(self.app_num, 3, "null")
                self.sheet1.write(self.app_num, 4, "null")
            self.app_num += 1
        elif spider.name == "lygames":
            if item["game_name"] and item["game_package"] and item["game_size"] and item["game_version"]:
                self.sheet2.write(self.game_num, 0, self.game_num)
                self.sheet2.write(self.game_num, 1, item["game_name"])
                # if item["game_package"] == ['http://www.9apps.com/down/pc4.apk']:
                #     self.sheet1.write(self.app_num, 2, "com.mobile.indiapp")
                # else:
                self.sheet2.write(self.game_num, 2, item["game_package"][0].replace("/jump/down/", "").replace(
                "/app/?f=9_0_1_0_1", ""))
                self.sheet2.write(self.game_num, 3, item["game_size"])
                self.sheet2.write(self.game_num, 4, item["game_version"])
            else:
                self.sheet2.write(self.game_num, 0, self.game_num)
                self.sheet2.write(self.game_num, 1, "null")
                self.sheet2.write(self.game_num, 2, "null")
                self.sheet2.write(self.game_num, 3, "null")
                self.sheet2.write(self.game_num, 4, "null")
            self.game_num += 1
        return item

    # 当spider关闭时，这个方法被调用
    def close_spider(self, spider):
        # app = get_app()
        # game = get_game()
        # print(app == "true" == game, "*****", app, "*****", game)
        # if app == True == game:
        #     filename = "9apps - APP_AND_GAME_TOP资源.xls"
        #     self.book.save(filename)
        #     print("------------", "文件保存路径", os.getcwd(), "------------")
        # else:
        #     print("------------", "文件保存失败", "------------")
        if spider.name == "lyapps":
            filename = "9apps - top - apps资源.xls"
            print("------------", filename, "文件保存路径", os.getcwd(), "------------")
            self.book.save(filename)
        elif spider.name == "lygames":
            filename = "9apps - top - games资源.xls"
            print("------------", filename, "文件保存路径", os.getcwd(), "------------")
            self.book.save(filename)
