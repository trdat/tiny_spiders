import scrapy


class MDPIJournal(scrapy.Spider):
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