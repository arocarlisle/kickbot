# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ProjectItem(scrapy.Item):
    url = scrapy.Field()
    url_img = scrapy.Field()
    title = scrapy.Field()
    category = scrapy.Field()
    date_created = scrapy.Field()
    funding_goal= scrapy.Field()
    funding_current = scrapy.Field()
    description = scrapy.Field()
    author = scrapy.Field()