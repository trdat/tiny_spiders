import scrapy
import re
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

# TODO
# get the h2 article (1 per page)
class NcovMOH_QA(scrapy.Spider):
    name = "NcovMOH_QA"
    allowed_domains = ['ncov.moh.gov.vn']
    start_urls = ['https://ncov.moh.gov.vn/web/guest/hoi-dap1?p_p_id=tracuu_WAR_coronadvcportlet&p_p_lifecycle=0&p_p_state=normal&p_p_mode=view&p_p_col_id=_118_INSTANCE_IrnCPpeHzQ4m__column-1&p_p_col_count=1&_tracuu_WAR_coronadvcportlet_mvcPath=%2Fhtml%2Fmic%2Fportlet%2Ftracuu%2Fview.jsp&_tracuu_WAR_coronadvcportlet_Keyword=&_tracuu_WAR_coronadvcportlet_tuNgay=&_tracuu_WAR_coronadvcportlet_denNgay=&_tracuu_WAR_coronadvcportlet_linhVucId=0&_tracuu_WAR_coronadvcportlet_thuTucId=0&_tracuu_WAR_coronadvcportlet_showHide=1&_tracuu_WAR_coronadvcportlet_delta=10&_tracuu_WAR_coronadvcportlet_keywords=&_tracuu_WAR_coronadvcportlet_advancedSearch=false&_tracuu_WAR_coronadvcportlet_andOperator=true&_tracuu_WAR_coronadvcportlet_resetCur=false&_tracuu_WAR_coronadvcportlet_cur=1']

    def parse(self, response):
        for item in response.css('#accordion2'):
            yield {
                'time': item.xpath('./div/p[1]/span/text()[2]').get().strip(),
                'question': re.sub('\n\t+', '', item.xpath('./div/div[1]/p/span[2]/text()').get()),
                'answer': item.xpath('./div/div/div/text()').get()
            }

        # Follow pagination link
        next_page_url = response.xpath('//*[@id="_tracuu_WAR_coronadvcportlet_ocerSearchContainerPageIterator"]/div/ul/li[3]/a/@href').extract()
        yield from response.follow_all(next_page_url, self.parse)
