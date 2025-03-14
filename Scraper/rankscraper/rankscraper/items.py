# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class RankscraperItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    pass

class RankscraperItem(scrapy.Item):
    Region = scrapy.Field()
    Branch = scrapy.Field()
    Jee_Rank = scrapy.Field()
    Round = scrapy.Field()
    Category = scrapy.Field()
    

