from datetime import datetime, timedelta
import random
from re import A
import scrapy
from scrapy.http.request import Request
from sqlalchemy import false
from scraper.items import BattleItem



class WikiScraper(scrapy.Spider):
    name = 'wikispider'
    allowed_domains = []
    start_urls = ['https://en.wikipedia.org/wiki/List_of_battles_before_301',
                #   'https://en.wikipedia.org/wiki/List_of_battles_301%E2%80%931300',
                #   'https://en.wikipedia.org/wiki/List_of_battles_1301%E2%80%931600',
                #   'https://en.wikipedia.org/wiki/List_of_battles_1601%E2%80%931800',
                #   'https://en.wikipedia.org/wiki/List_of_battles_1801%E2%80%931900',
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
            
            # now shuffle and take the first 10 rows
            random.shuffle(links)
            links = links[:40]
            new_links = [
                'https://en.wikipedia.org/wiki/Battle_of_Thermopylae',
                'https://en.wikipedia.org/wiki/Siege_of_Harran',
                'https://en.wikipedia.org/wiki/Battle_of_Megiddo_(609_BC),',
                'https://en.wikipedia.org/wiki/Battle_of_Pelusium_(343_BC)',
                'https://en.wikipedia.org/wiki/Battle_of_Issus',
                'https://en.wikipedia.org/wiki/Battle_of_the_Granicus',
                'https://en.wikipedia.org/wiki/Battle_of_Cannae',
                'https://en.wikipedia.org/wiki/Battle_of_the_Teutoburg_Forest',
            ]

            for link in links:
                # print('\n\n\nbeginning new link:\n{}\n\n\n'.format(link.extract()))
                # request = scrapy.Request('https://en.wikipedia.org' + link.extract(), callback=self.parse_battle_page)

                # Testing individual battles
                battle = 'https://en.wikipedia.org/wiki/Battle_of_Marathon'
                request = scrapy.Request(battle, callback=self.parse_battle_page)
                yield request
                break


    def parse_battle_page(self, response):
        '''
        Pull out the following details from a page:

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

        If any details cannot be found, the battle is skipped.

        :param :
        :return:
        '''
        if response.status != 200:
            print('Response was not 200.')
        
        # This represents the battle row that will be stored in the database
        battle = BattleItem()
        battle['wikipediaLink'] = response.url


        # Parse battle name
        battleName = response.xpath("//*[@id='firstHeading']/text()").extract()
        # See if the xpath found anything
        if len(battleName) > 0:
            battleName = self.parse_battle_name(battleName[0])
            battle['battleName'] = battleName


        # Parse date
        date = response.xpath("//table[contains(@class, 'infobox')]/tbody/tr/td/table/tbody/tr/th[text()='Date']/following-sibling::td/text()").extract()
        if len(date) > 0: 
            date = self.remove_unusual_characters(date[0])
            battle['date'] = date


        # Parse location
        # not(self::span)]   [not(self::a)]
        location = response.xpath("//div[contains(@class, 'location')]/*[not(self::style)]/text()").extract()
        if len(location) > 0:
            location = self.parse_location(location)  # convert list into string
            location = self.remove_unusual_characters(location)
            battle['location'] = location



        # Parse belligerents
        belligerent_selectors = ["/text()", "/a/text()", "/span/a/text()", "/p/a/text()", "/div/div/div/span/a/text()"]
        # //th[text()='Belligerents']/../following-sibling::tr[1]/td[1]/div/div/div/span/a
        # //th[text()='Belligerents']/../following-sibling::tr[1]/td[2]/a
        # //th[text()='Belligerents']/../following-sibling::tr[1]/td[2]/span/a
        # //th[text()='Belligerents']/../following-sibling::tr[1]/td[1]/p/a

        # Belligerent A
        for selector in belligerent_selectors:
            belligerent_a = response.xpath("//th[text()='Belligerents']/../following-sibling::tr[1]/td[1]" + selector).extract()
            # See if the xpath found anything
            if len(belligerent_a) > 0:
                belligerent_a = belligerent_a[0]  # convert list to string
                belligerent_a = self.remove_unusual_characters(belligerent_a)
            # Check if we actually got a string
            if len(belligerent_a) > 0:
                battle['belligerentA'] = belligerent_a
                break


        # Belligerent B
        for selector in belligerent_selectors:
            belligerent_b = response.xpath("//th[text()='Belligerents']/../following-sibling::tr[1]/td[2]" + selector).extract()
            # See if the xpath found anything
            if len(belligerent_b) > 0:
                belligerent_b = belligerent_b[0]  # convert list to string
                belligerent_b = self.remove_unusual_characters(belligerent_b)
            # Check if we actually got a string
            if len(belligerent_b) > 0:
                battle['belligerentB'] = belligerent_b
                break


        # Parse battle result
        battle_result = response.xpath("//table[contains(@class, 'infobox')]/tbody/tr/td/table/tbody/tr/th[text()='Result']/following-sibling::td/text()").extract()
        if len(battle_result) > 0:
            battle_result = self.remove_unusual_characters(battle_result[0])
            battle_result = self.parse_winner(belligerent_a, belligerent_b, battle_result)
            battle['answer'] = battle_result


        # Parse leaders
        #  //th[text()='Commanders and leaders']/../following-sibling::tr[1]/td[1]/a[2]
        leader_a = response.xpath("//th[text()='Commanders and leaders']/../following-sibling::tr[1]/td[1]/a[not(contains(@class, 'image'))]/text()").extract()
        leader_a_link = response.xpath("//th[text()='Commanders and leaders']/../following-sibling::tr[1]/td[1]/a[not(contains(@class, 'image'))]/@href").extract()
        if len(leader_a) > 0:
            battle['leaderAName'] = leader_a[0]


        leader_b = response.xpath("//th[text()='Commanders and leaders']/../following-sibling::tr[1]/td[2]/a[not(contains(@class, 'image'))]/text()").extract()
        leader_b_link = response.xpath("//th[text()='Commanders and leaders']/../following-sibling::tr[1]/td[2]/a[not(contains(@class, 'image'))]/@href").extract()
        if len(leader_b) > 0:
            battle['leaderBName'] = leader_b[0]


        # Parse wikipedia summary
        # *[not(self::style)]/text()
        # //*[not(self::script)]/text()
        wikipediaBlurb = response.xpath("//div[contains(@class, 'navbox') or contains(@class, 'infobox') or contains(@class, 'stack-container')]/following-sibling::p[1]/descendant::text()[not(parent::style) and not(parent::sup)]").extract()
        if len(wikipediaBlurb) > 0:
            wikipediaBlurb = self.parse_summary(wikipediaBlurb)  # condense list of strings to single string
            battle['wikipediaBlurb'] = wikipediaBlurb[:350] if len(wikipediaBlurb) <= 350 else wikipediaBlurb[:350] + '...'  # if the blurb is trimmed, add elipsis
        

        # If we are missing a leader image, scrap this battle and move on
        print(leader_a_link)
        print(leader_b_link)
        if not leader_a_link and len(leader_a_link) == 0 or not leader_b_link and len(leader_b_link) == 0:
            print('test 1')
            yield None
        else:
            # Now to scrape the leader wikipedia pages to get the source for their images
            yield scrapy.Request('https://en.wikipedia.org' + leader_a_link[0],
                                callback=self.get_leader_image_url,
                                meta={'battle': battle,
                                    'leader_b_link': leader_b_link[0],
                                    'is_second_leader': False})


    def get_leader_image_url(self, response):
        '''
        This scrapes the image src for each leader by visiting both of their wikipedia pages.

        :param response: The scrapy request, containing our meta data: battle (our battle db row)
                         and is_second_leader (flag for indicating if its the first or second leader)
        :return: None
        '''
        battle = response.meta.get('battle')
        leader_image_url = response.xpath("//td[contains(@class, 'infobox-image')]/a/img/@src").extract()
        
        # If this is the first leader, then store leader_a data and recurse
        if not response.meta.get('is_second_leader', True):
            battle['leaderAImageLink'] = leader_image_url
            yield scrapy.Request('https://en.wikipedia.org' + response.meta.get('leader_b_link'),
                                 callback=self.get_leader_image_url,
                                 meta={'battle': battle, 'is_second_leader': True})

        # Otherwise store second leader data and end
        else:
            battle['leaderBImageLink'] = leader_image_url

            #final checks
            if battle.get('leaderAImageLink') and len(battle.get('leaderAImageLink')) <= 300 and \
               battle.get('leaderBImageLink') and len(battle.get('leaderBImageLink')) <= 300:
                yield battle
            else:
                print('test 2')
                yield None


    '''
    Helper Methods

    remove_unusual_characters - removes mostly unicode characters that get scraped
    parse_battle_name - removes any parenthese info from the name
    parse_location - joins location strings with a comma
    '''

    def remove_unusual_characters(self, string):
        '''
        Some characters from wikipedia need to be converted. This handles the following characters:
        \xa0 -> [space]
        \n -> [remove]
        
        :param string: Scraped string from wikipedia
        :return: String, removed unusual characters
        '''
        return string.replace(u'\xa0', u' ').replace(u'\n', '')


    def parse_battle_name(self, name):
        '''
        Some names contain additional info, like a date.

        Trim the any parentheses at the end of the name and return the result.

        :param name: The raw string header from the wikipedia page
        :return: String, the trimmed name
        '''
        if '(' in name:
            index = name.index('(')
            return name[:index].strip()
        else:
            return name


    def parse_location(self, location):
        '''
        Location is usually two strings joined by a comma. We get the location as a
        list and need to convert it to a string.

        :param location: List containg location string
        :return: String, location as a string
        '''
        result = location[0]

        if len(location) > 1:
            for sub_string in location[1:]:
                result += (', ' + sub_string)
        
        result = result.rstrip()
        return result

    def parse_winner(self, belligerent_a, belligerent_b, result_string):
        '''
        Wikipedia result strings typically contain the name of the winning belligerent
        followed by 'victory'.
        
        For example, "Mexican Rebel Victory" where the belligerents were 'Mexican Rebels'
        and 'Spanish Empire.'

        This decides the winner by matching as many characters to each one as possible. That
        means, creating a character map for each string, and seeing which ones are closest.

        Finally, some names are quite different...
        United States -> American Victory

        Dictionary will convert some specific terms

        :param:
        :param:
        :param:
        :return:
        '''

        '''
        Helper methods
        '''
        convert_specific_victory_strings = {
            'american victory': 'United States'
        }

        def add_to_character_map(map, char):
            '''
            Either create a new key in a dict with count = 1, or increment
            the count for the character.
            '''
            if char in map.keys():
                map[char] += 1
            else:
                map[char] = 1
        
        def count_differences_between_character_maps(map_a, map_b):
            '''
            Start with the first map, and iterate through the second,
            subtract each key from the second.
            '''
            # Begin by subtracting all map_b values from map_a
            for key, b_value in map_b.items():
                a_value = map_a.get(key, 0)  # if its not in the first string, then there are 0 occurences
                map_a[key] = abs(a_value - b_value)
            
            # Now return a final count of all values in map_a
            return sum(map_a.values())

        '''
        End helper methods
        '''

        # First check if the victory string matches any specific terms
        # and convert it if it does
        if result_string.lower() in convert_specific_victory_strings.keys():
            result_string = convert_specific_victory_strings.get(result_string.lower())

        # create character maps
        result_string_character_map = {}
        for char in result_string:
            add_to_character_map(result_string_character_map, char)

        belligerent_a_character_map = {}
        for char in belligerent_a:
            add_to_character_map(belligerent_a_character_map, char)

        belligerent_b_character_map = {}
        for char in belligerent_b:
            add_to_character_map(belligerent_b_character_map, char)

        # get number of differences for belligerent a
        num_differences_a = count_differences_between_character_maps(belligerent_a_character_map,
                                                                     result_string_character_map)

        # get number of differences for belligerent b
        num_differences_b = count_differences_between_character_maps(belligerent_b_character_map,
                                                                     result_string_character_map)
        
        if num_differences_a < num_differences_b:
            return 'A'
        elif num_differences_a > num_differences_b:
            return 'B'
        else:
            return None

    def parse_summary(self, list_of_strings):
        '''
        Converts the summary, a list of strings, to a single string with some characters removed.

        Certain unicode characters are removed.
        Wikipedia references are removed (ex. '[1]')

        :param list_of_strings: The list of strings containing the wikipedia summary
        :return: String, the processed wikipedia summary
        '''

        def remove_brackets(string):
            '''
            Iterates recursively through a string to remove all references
            (ex. "[1]")

            :param string: A string
            :return: String, without any grouped brackets
            '''
            # if string is empty, return it
            if string is None or len(string) == 0 or '[' not in string:
                return string
            
            # get first occurence of an open bracket
            else:
                # if there is a close bracket within a few characters, this will be removed
                if ']' in string[string.find('['):string.find('[') + 4]:
                    # save the text before the open bracket
                    before_open_bracket = string[:string.find('[')]
                    # for the remainder string, trim the string to the open bracket
                    after_open_bracket = string[string.find('['):]
                    # and then trim down past the close bracket
                    after_open_bracket = string[string.find(']') + 1:]
                    # Recurse on the remainder of the string
                    return before_open_bracket + remove_brackets(after_open_bracket)
        
        def inch_forward_commas(string):
            '''
            '''
            result = ''

            for c in string:
                if c == ',':
                    # remove every whitespace preceeding this
                    result = result.rstrip()
                result += c
            
            return result




        result = ''.join(list_of_strings)  # convert list of strings to a single string
        result = self.remove_unusual_characters(result)  # remove unicode characters
        result = remove_brackets(result)  # remove wikipedia references (ex. "[1]")
        result = inch_forward_commas(result)  # if any commas trail whitespace, remove the whitespace
        return result