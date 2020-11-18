from datetime import datetime, timedelta
import random
import scrapy
from scrapy.http.request import Request
from scraper.items import MatchItem



class WikiScraper(scrapy.Spider):
    name = 'wikispider'
    allowed_domains = []
    start_urls = [#'https://en.wikipedia.org/wiki/List_of_battles_before_301',
    #               'https://en.wikipedia.org/wiki/List_of_battles_301%E2%80%931300',
                #   'https://en.wikipedia.org/wiki/List_of_battles_1301%E2%80%931600',
                #   'https://en.wikipedia.org/wiki/List_of_battles_1601%E2%80%931800',
                  'https://en.wikipedia.org/wiki/List_of_battles_1801%E2%80%931900',
                #   'https://en.wikipedia.org/wiki/List_of_battles_1901%E2%80%932000',
                #   'https://en.wikipedia.org/wiki/List_of_battles_since_2001',
                  ]

    # Override start urls so the we start with a random battle list
    def start_requests(self):
        url = random.choice(self.start_urls)
        yield Request(url, self.parse)

    def parse(self, response):
        # make sure response is good
        if response.status == 200:
            print('\n\n')

            # check for the type of page we are dealing with, there are 2:
            # - unordered list of battles
            # - sortable table

            # check if there are sortable tables
            sortable_tables = response.xpath("//table[contains(@class, 'sortable')]")
            if len(sortable_tables) != 0:
                links = response.xpath("//table[contains(@class, 'sortable')]/tbody/tr/td[2]/a/@href")
            
            # otherwise look for li and get first a urls
            else:
                links = response.xpath("//div[contains(@class, 'mw-parser-output')]/ul/li/ul/li/a[1]/@href")
            

            # now take the first 10 rows and shuffle
            random.shuffle(links)
            links = links[:10]

            for link in links:
                print(link.extract())

            # attempt to get match info from first, if that fails continue
            # TODO

            print('\n\n')

            # items = response.css('body center #hnmain tr td .itemlist tr')
            
            # # This is a python idiom for iterating through a list at x items at a time
            # # zip(*[iter(s)]*n) - https://docs.python.org/3/library/functions.html#zip
            # #
            # # 3 Rows make up a single Hacker News Item: header, subtext, and a spacer
            # for header, details, _ in zip(*[iter(items)]*3):
            #     # article title
            #     title = header.css('.athing .title .storylink::text').get()
                
            #     # article link
            #     link = header.css('.athing .title a').attrib.get('href')

            #     # score
            #     score = details.css('.subtext .score::text').get()
            #     digits = [int(s) for s in score.split() if s.isdigit()]
            #     score = digits[0] if len(digits) > 0 else 0

            #     # age
            #     age = details.css('.subtext .age a::text').get()
            #     digits = [int(s) for s in age.split() if s.isdigit()]
            #     age_int = digits[0] if len(digits) > 0 else 0

            #     if 'minute' in age:
            #         age = datetime.now() - timedelta(minutes=age_int)
            #     elif 'hour' in age:
            #         age = datetime.now() - timedelta(hours=age_int)
            #     elif 'day' in age:
            #         age = datetime.now() - timedelta(days=age_int)

            #     # comment details
            #     try:
            #         comments = details.css('.subtext a')[3]

            #         # num of comments
            #         num_comments = comments.css('::text').get()
            #         digits = [int(s) for s in num_comments.split() if s.isdigit()]
            #         if len(digits) > 0:
            #             num_comments = digits[0]
            #         else:
            #             num_comments = 0

            #         # comments link
            #         comment_link = comments.attrib.get('href')
            #     except:
            #         continue

            #     if title and link:
            #         item = NewsItem()
            #         item['title'] = title
            #         item['link'] = link
            #         item['score'] = score
            #         item['age'] = age
            #         item['num_comments'] = num_comments
            #         item['comment_link'] = comment_link

            #         if comment_link:
            #             request = scrapy.Request('http://news.ycombinator.com/' + comment_link, callback=self.parse_news_link)
            #             request.meta['item'] = item
            #             yield request


    # def parse_news_link(self, response):
    #     # get current news item from callback
    #     item = response.meta['item']
    #     import pdb; pdb.set_trace()
    #     return

            # response.css()

            # parse the response body
            # soup = BeautifulSoup(response.body)
            # items = [(x[0].text, x[0].get('href')) for x in
            #     filter(None, [
            #     x.findChildren() for x in
            #         soup.findAll('td', {'class':'title'})
            #     ])]

            # for item in items:
            #     print(item)
            #     news_item = NewsItem()
            #     news_item['title']  = item[0]
            #     news_item['url']    = item[1]
            #     # try:
            #     #     yield scrapy.Request(item[1], callback=self.parse)
            #     # except ValueError:
            #     #     yield scrapy.Request('http://news.ycombinator.com/' + item[1], callback=self.parse)

            #     yield news_item