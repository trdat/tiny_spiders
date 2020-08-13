# -*- coding: utf-8 -*-
# For crawling MDPI.com
from twisted.internet import ractor, defer
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from download import download

process = CrawlerProcess(get_project_settings())

# Get list of all journals
class Spider1(scrapy.Spider):
	name = "mdpi_journal"

    start_urls = [
        'https://www.mdpi.com/about/journals'
    ]
    
    def parse(self, response):
        # rows = table.xpath('//tr')
        for row in response.xpath('//*[@class="journaltable new tablesorter top-border"]//tbody//tr'):
            yield {
                'journal-name': row.xpath('td').xpath('a/div//text()').get().strip(),
                'ISSN': row.xpath('td')[1].xpath('.//text()').get(),
                'launched': row.xpath('td')[2].xpath('.//text()').get(),
                'current_issue': row.xpath('td')[3].xpath('./a//text()').get().strip(),
                'IF': row.xpath('td')[4].xpath('.//text()').get().strip(),
                'upc_articles': row.xpath('td')[5].xpath('.//text()').get().strip(),
                'tot_articles': row.xpath('td')[6].xpath('./a/text()').get(),
                'rss': row.xpath('td')[7].xpath('./a/@href').get(),
            }

# Get all link download of each journal
class Spider2(scrapy.Spider):
	pass

def downloadAllJournals(journal):
	dir_path = '/home/trdat/Projects/tiny_spiders/data/mdpi/' + journal + '/'
	with open('test.json', 'r') as file_handle:
		articles = json.load(file_handle)
		for article in articles:
			file_name_to_save = dir_path + article['article_title'].replace(" ", "_") + '.pdf'
			link_download_pdf = article['link_download_pdf']
			print(file_name_to_save, '\n', link_download_pdf)
			path = download(link_download_pdf, file_name_to_save)

configure_logging()
runner = CrawlerRunner()

@defer.inlineCallbacks
def crawl():
	yield runner.crawl(Spider1)
	yield runner.crawl(Spider2)
	reactor.stop()
