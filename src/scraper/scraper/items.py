# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BattleItem(scrapy.Item):
    '''
    Battle name - string
    Date - string
    Location - string
    Belligerent A - string
    Belligerent B - string
    Leader A - string
    Leader B - string
    Leader A Photo Link - string
    Leader B Photo Link - string
    Result - string
    Wikipedia blurb - string
    Wikipedia link - string
    '''
    battleName = scrapy.Field()
    date = scrapy.Field()
    location = scrapy.Field()
    answer = scrapy.Field()

    belligerentA = scrapy.Field()
    belligerentB = scrapy.Field()

    leaderAName = scrapy.Field()
    leaderAImageLink = scrapy.Field()

    leaderBName = scrapy.Field()
    leaderBImageLink = scrapy.Field()

    wikipediaBlurb = scrapy.Field()
    wikipediaLink = scrapy.Field()