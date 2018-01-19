# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
from scrapy.pipelines.files import FilesPipeline
from urllib.parse import urlparse
from os.path import basename,splitext

class TutorialPipeline(object):
    def process_item(self, item, spider):
        return item


class FileDownloadPipeline(FilesPipeline):
    def get_media_requests(self, item, info):
        # print(item)
        if 'file_urls' in item:
            self.__file_name = item['name']
            for file_url in item['file_urls']:
                yield scrapy.Request(file_url)

    # def file_path(self, request, response=None, info=None):
    #     path=urlparse(request.url).path
    #     filename = '%s' % basename(path)
    #     if self.__file_name is None:
    #         return filename
    #     else:
    #         return './test/'+self.__file_name + splitext(filename)[1]