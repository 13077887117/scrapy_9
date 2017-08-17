# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Get9AppStopItem(scrapy.Item):
    app_name = scrapy.Field()
    app_package = scrapy.Field()
    app_size = scrapy.Field()
    app_version = scrapy.Field()

    game_name = scrapy.Field()
    game_package = scrapy.Field()
    game_size = scrapy.Field()
    game_version = scrapy.Field()
