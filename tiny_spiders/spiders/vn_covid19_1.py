import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class VnCovid191Spider(scrapy.Spider):
    name = 'vn-covid19-1'
    allowed_domains = ['ncov.moh.gov.vn']
    start_urls = ['https://ncov.moh.gov.vn/web/guest/dong-thoi-gian?p_p_id=101_INSTANCE_iEPhEhL1XSde&p_p_lifecycle=0&p_p_state=normal&p_p_mode=view&p_p_col_id=_118_INSTANCE_IrnCPpeHzQ4m__column-1&p_p_col_count=1&_101_INSTANCE_iEPhEhL1XSde_delta=30&_101_INSTANCE_iEPhEhL1XSde_keywords=&_101_INSTANCE_iEPhEhL1XSde_advancedSearch=false&_101_INSTANCE_iEPhEhL1XSde_andOperator=true&p_r_p_564233524_resetCur=false&_101_INSTANCE_iEPhEhL1XSde_cur=1']

    # rules = (
    #     Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    # )

    i = 0
    def parse(self, response):
        # self.log("\n----------" + str(i) + "----------\n")
        i = i + 1
        for item in response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "portlet-content", " " ))]'):
            yield {
                'id': str(i),
                'time': item.xpath('.//h3').get(),
                'content': item.xpath('.//p').get()
            }
        
        # Follow pagination link
        next_page_url = response.css('div.clearfix.lfr-pagination > ul > li:nth-child(2) > a::attr(href)').get()
        yield from response.follow_all(next_page_url, self.parse)
