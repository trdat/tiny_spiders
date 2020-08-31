import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

# TODO
# get the h2 article (1 per page)
class NcovMOH_News(scrapy.Spider):
    name = "NcovMOH_News"
    allowed_domains = ['ncov.moh.gov.vn']
    start_urls = ['https://ncov.moh.gov.vn/web/guest/tin-tuc?p_p_id=101_INSTANCE_bQiShy2NRK1f&p_p_lifecycle=0&p_p_state=normal&p_p_mode=view&p_p_col_id=_118_INSTANCE_IrnCPpeHzQ4m__column-1&p_p_col_count=1&_101_INSTANCE_bQiShy2NRK1f_delta=5&_101_INSTANCE_bQiShy2NRK1f_keywords=&_101_INSTANCE_bQiShy2NRK1f_advancedSearch=false&_101_INSTANCE_bQiShy2NRK1f_andOperator=true&p_r_p_564233524_resetCur=false&_101_INSTANCE_bQiShy2NRK1f_cur=1']

    def parse(self, response):
        for item in response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "text-tletin", " " ))]'):
            yield {
                'article_title': item.xpath('.//text()').get(),
                'article_url': item.xpath('.//@href').get()
            }

        # Follow pagination link
        tmp_next_page_url = response.css(
            '#p_p_id_101_INSTANCE_bQiShy2NRK1f_ > div > div > div.clearfix.lfr-pagination > ul > li:nth-child(2) > a')
        next_page_url = tmp_next_page_url.xpath('.//@href').extract()
        yield from response.follow_all(next_page_url, self.parse)
