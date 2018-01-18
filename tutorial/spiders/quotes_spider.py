# import scrapy
import hashlib
# from scrapy.spiders import Rule,CrawlSpider
# from scrapy.linkextractors import LinkExtractor
#

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor


class QuotesSpider(CrawlSpider):
    name = "quotes"
    start_urls = [
        'http://www.dhu.edu.cn',
    ]
    allowed_domains = [
        'dhu.edu.cn',
    ]
    rules = (
        Rule(LinkExtractor(deny=('english.dhu.edu.cn')), callback='parse_test', follow=True),
    )
    # def start_requests(self):
    #     urls = [
    #         'http://www.dhu.edu.cn',
    #     ]
    #     allowed_domains = [
    #         'dhu.edu.cn',
    #     ]
    #     rules = (
    #         Rule(LinkExtractor(allow=('dhu')), callback='parse_test', follow=True),
    #     )
    #     for url in urls:
    #         yield scrapy.Request(url=url, callback=self.parse)

    def parse_test(self, response):
        print(response.meta)
        m = hashlib.md5()
        m.update(response.url.encode())
        page = m.hexdigest()
        filename = './html/%s.html' % page
        with open(filename, 'ab') as f:
            f.write(response.url.encode())
            f.write(response.body)
        # next_pages = response.css('a::attr(href)').extract()
        # for next_page in next_pages:
        #     if next_page is not None:
        #         yield response.follow(next_page, callback=self.parse_test)


    # def parse(self, response):
    #     pass
    # def parse(self, response):
    #     m = hashlib.md5()
    #     m.update(response.url.encode())
    #     page = m.hexdigest()
    #     filename = './html/%s.html' % page
    #     next_pages = response.css('a::attr(href)').extract()
    #     self.log('****************url %s' % response.url)
    #     with open(filename, 'wb') as f:
    #         f.write(response.body)
    #     for next_page in next_pages:
    #         if next_page is not None:
    #             yield response.follow(next_page, callback=self.parse)
    #     # self.log('****************url %s' % response.url)