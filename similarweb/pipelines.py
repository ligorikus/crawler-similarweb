# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json


class SimilarwebPipeline(object):
    def __init__(self):
        self.file = open('sites.json', 'wb')

    def open_spider(self, spider):
        self.file.write(b"[\n")


    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"

        self.file.write(line.encode())
        return item

    def close_spider(self, spider):
        self.file.write(b"]")
