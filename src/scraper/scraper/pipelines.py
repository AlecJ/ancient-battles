# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem


class ScraperPipeline:
    def process_item(self, item, spider):
        # Validation
        adapter = ItemAdapter(item)
        print(adapter)
        validation_fields = ['battleName', 'date', 'location', 'belligerentA', 'belligerentB', 'answer', 'leaderAName', 'leaderBName',
                             'wikipediaBlurb', 'leaderAImageLink', 'leaderAImageLink', 'leaderBImageLink']
        for field in validation_fields:
            if not adapter.get(field) or len(adapter.get(field)) == 0:
                raise DropItem('Missing Field: {}'.format(field))
        
        # some final length checks
        if len(adapter.get('leaderAImageLink')) > 300 or len(adapter.get('leaderBImageLink')) > 300:
            raise DropItem('Image Link is too long.')
        
        if len(adapter.get('wikipediaBlurb')) > 450:
            raise DropItem('Wiki blurb is too long.')

        return item