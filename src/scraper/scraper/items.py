# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MatchItem(scrapy.Item):
    link = scrapy.Field()
    date = scrapy.Field()
    location = scrapy.Field()

    leader_A_name = scrapy.Field()
    leader_A_pic_url = scrapy.Field()
    leader_A_people = scrapy.Field()

    leader_B_name = scrapy.Field()
    leader_B_pic_url = scrapy.Field()
    leader_B_people = scrapy.Field()
