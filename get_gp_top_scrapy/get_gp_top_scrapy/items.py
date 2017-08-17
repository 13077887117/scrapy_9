# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GetGpTopScrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    in_app_id = scrapy.Field()
    in_app_name = scrapy.Field()
    in_app_package = scrapy.Field()
    # in_app_url = scrapy.Field()
    in_app_updated = scrapy.Field()
    in_app_version = scrapy.Field()
    in_app_requirse_android = scrapy.Field()


    id_app_id = scrapy.Field()
    id_app_name = scrapy.Field()
    id_app_package = scrapy.Field()
    # id_app_url = scrapy.Field()
    id_app_updated = scrapy.Field()
    id_app_version = scrapy.Field()
    id_app_requirse_android = scrapy.Field()

