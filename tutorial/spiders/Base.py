import time

from ..until import until
from urllib import parse

from os.path import basename,splitext
from scrapy_redis.spiders import RedisCrawlSpider
from scrapy.contrib.spiders import Rule
from scrapy.contrib.linkextractors import LinkExtractor
from ..items import *
# from scrapy.loader import ItemLoader

from tutorial.settings import *

class Base(RedisCrawlSpider):
    """Spider that reads urls from redis queue (myspider:start_urls)."""
    name = 'base'
    redis_key = 'base:start_urls'
    allowed_domains = ALLOWED_DOMAINS

    rules = (
        # follow all links
        Rule(LinkExtractor(deny=('english.dhu.edu.cn')), callback='parse_page', follow=True),
    )

    def parse_test(self, response):
        print(response.url)

    def get_page_item(self, response):
        nowtime = time.time()
        url = response.url
        origin = parse.urlparse(url).netloc

        _str = '<__split>'\
               'data: {}\n' \
               'url: {}\n' \
               'origin: {}\n' \
               '<\__split>\n'\
               '\n' \
               .format(nowtime, url, origin)
        return _str

    def parse_page(self, response):

        page = until.md5(response.url.encode())
        # print(response.url)

        until.save_file(path=ALL_FILE_PATH, name=page + '.sraw', content=self.get_page_item(response).encode() + response.body)

        urlItem = InformationItem()
        urlItem['urls'] = parse.quote_plus(response.url)
        yield urlItem

        links = response.xpath('//a')
        for index, alink in enumerate(links):
            href = alink.xpath('@href').extract_first()
            path = parse.urlparse(href).path
            filename = '%s' % basename(path)
            extrename = splitext(filename)[1]

            if extrename in INCLUDE_FILE_TYPE:
                name = alink.xpath('text()').extract_first()
                fileItem = self.getFileItem(self.cutHref(href, response.url), name)
                yield fileItem



    def getFileItem(self, file_urls=None, name=None):
        fileItem = FileItem()
        if file_urls is None or name is None:
            return fileItem
        else:
            fileItem['file_urls'] = [file_urls] # 必须为一个list
            fileItem['name'] = name
            return fileItem

    def cutHref(self, href='', url=''):
        if until.isHasHttpOrHttps(href):
            return href
        return parse.urljoin(url, href.strip())

