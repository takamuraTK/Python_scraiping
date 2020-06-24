# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from scrapy_tutorial.items import KakugeItem


class KakugeSpider(CrawlSpider):
    name = 'kakuge'
    allowed_domains = ['kakuge-checker.com']
    start_urls = ['https://kakuge-checker.com/']

    rules = (
        Rule(
            LinkExtractor(restrict_css='ul.topic_list'),
            callback='parse_item'
        ),
    )

    def parse_item(self, response):
        print(response)
        item = KakugeItem()
        item['headline'] = response.css('h2::text').extract_first()
        return item
