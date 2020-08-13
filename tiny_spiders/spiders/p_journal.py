import scrapy


class MDPI_Journal_Crawler(scrapy.Spider):
	name = 'test_journal_crawler'

	start_urls = [
		'https://www.mdpi.com/search?q=&journal=applmech&sort=pubdate&page_count=15&page_no=1',
		# 'https://www.mdpi.com/search?q=&journal=applmech&sort=pubdate&page_count=15&page_no=2',
		# 'https://www.mdpi.com/search?q=&journal=applmech&sort=pubdate&page_count=15&page_no=3',
		# 'https://www.mdpi.com/search?q=&journal=applmech&sort=pubdate&page_count=15&page_no=4',
		# 'https://www.mdpi.com/search?q=&journal=applmech&sort=pubdate&page_count=15&page_no=5',
		# 'https://www.mdpi.com/search?q=&journal=applmech&sort=pubdate&page_count=15&page_no=6',
	]

	def parse(self, response):
		for link in response.xpath("//*[@class='title-link']"):
			yield {
				'article_title': link.xpath('.//text()').get(),
				'link_to_article': 'https://www.mdpi.com' + link.xpath('./@href').get(),
				'link_download_pdf': 'https://www.mdpi.com' + link.xpath('./@href').get() + '/pdf'
			}