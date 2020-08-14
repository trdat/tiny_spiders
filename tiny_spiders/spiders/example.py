import scrapy

class Example(scrapy.Spider):
	name = 'example_spider'
	allowed_domains = ['https://www.mdpi.com/']
	start_urls = [
		'https://www.mdpi.com/search?sort=pubdate&page_no=1&page_count=50&year_from=1996&year_to=2020&journal=applsci&view=default',
		'https://www.mdpi.com/search?sort=pubdate&page_no=2&page_count=50&year_from=1996&year_to=2020&journal=applsci&view=default',
		'https://www.mdpi.com/search?sort=pubdate&page_no=3&page_count=50&year_from=1996&year_to=2020&journal=applsci&view=default',
	]

	def parse(self, response):
		self.logger.info('A response from %s just arrived!', response.url)