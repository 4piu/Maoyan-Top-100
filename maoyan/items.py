# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class MaoyanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = scrapy.Field()
    rank = scrapy.Field()
    name_cn = scrapy.Field()
    name_alt = scrapy.Field()
    date = scrapy.Field()
    celebrity = scrapy.Field()
    score = scrapy.Field()
    box_first_week = scrapy.Field()
    box_sum = scrapy.Field()
    poster = scrapy.Field()
    region = scrapy.Field()
    tag = scrapy.Field()
    length = scrapy.Field()
    honor_count = scrapy.Field()
    nomination_count = scrapy.Field()