import scrapy
import re
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

# TODO
# get the h2 article (1 per page)
class Vinmec_QA(scrapy.Spider):
    name = "Vinmec_QA"
    allowed_domains = ['vinmec.com']
    start_urls = ['https://www.vinmec.com/vi/tin-tuc/thong-tin-suc-khoe/dich-2019-ncov/tu-van-bac-si/']
    isFirstPage = True

    # @staticmethod
    # def isFirstPage() {

    # }

    def parse(self, response):
        for post in response.css('#vue-bootstrap > div.post-list'):
            yield {
                'question': post.css('ul > li > div > h2 > a::text').get(),
                'url': post.css('ul > li > div > h2 > a::attr(href)').get()
            }

        # Follow pagination link
        if (self.isFirstPage):
            path = '//*[@id="vue-bootstrap"]/div[5]/span/a'
        else:
            path = '//*[@id="vue-bootstrap"]/div[5]/span/a[2]'
        next_page_url = response.css('#vue-bootstrap > div.pagination > span > a::attr(href)').get()
        if next_page_url is not None:
            next_page_url = response.urljoin(next_page_url)
            # print(next_page_url)
            self.isFirstPage = False
            yield scrapy.Request(next_page_url, callback=self.parse)
