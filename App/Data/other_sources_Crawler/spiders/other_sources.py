import scrapy


class OtherSourcesSpider(scrapy.Spider):
    name = 'other_sources'
    allowed_domains = ['kenyanmagazine.co.ke']
    start_urls = ['http://kenyanmagazine.co.ke/']

    def parse(self, response):
        pass
