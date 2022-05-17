# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BaiduNewsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #标题
    title = scrapy.Field()
    #发布时间
    dateTime = scrapy.Field()
    #详情url
    href = scrapy.Field()
    #百度快照摘要
    summary = scrapy.Field()
    #新闻来源
    sources = scrapy.Field()
