import scrapy

class AgentItem(scrapy.Item):
    name = scrapy.Field()
    store_name = scrapy.Field()
