# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exporters import CsvItemExporter

class ChromebookWriteItemPipeline(object):

    def __init__(self):
        self.filename = "bestbuy_chromebook.csv"

    def open_spider(self, spider):
        self.csvfile = open(self.filename, "wb")
        self.exporter = CsvItemExporter(self.csvfile)
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.csvfile.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

class GamingLaptopWriteItemPipeline(object):

    def __init__(self):
        self.filename = "bestbuy_gaminglaptop.csv"

    def open_spider(self, spider):
        self.csvfile = open(self.filename, "wb")
        self.exporter = CsvItemExporter(self.csvfile)
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.csvfile.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

class BusinessLaptopWriteItemPipeline(object):

    def __init__(self):
        self.filename = "bestbuy_businesslaptop.csv"

    def open_spider(self, spider):
        self.csvfile = open(self.filename, "wb")
        self.exporter = CsvItemExporter(self.csvfile)
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.csvfile.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item


class ChromebookReviewPipeline(object):

    def __init__(self):
        self.filename = "bestbuy_chromebookReview.csv"

    def open_spider(self, spider):
        self.csvfile = open(self.filename, "wb")
        self.exporter = CsvItemExporter(self.csvfile)
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.csvfile.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item


class BusinessLaptopReviewPipeline(object):

    def __init__(self):
        self.filename = "bestbuy_businessLaptopReview.csv"

    def open_spider(self, spider):
        self.csvfile = open(self.filename, "wb")
        self.exporter = CsvItemExporter(self.csvfile)
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.csvfile.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

class GamingLaptopReviewPipeline(object):

    def __init__(self):
        self.filename = "bestbuy_gamingLaptopReview.csv"

    def open_spider(self, spider):
        self.csvfile = open(self.filename, "wb")
        self.exporter = CsvItemExporter(self.csvfile)
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.csvfile.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item