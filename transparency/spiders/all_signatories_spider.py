# -*- coding: utf-8 -*-
import scrapy

from transparency.parsers.signatory_detail import Parser


class AllSignatoriesSpider(scrapy.Spider):
    name = 'AllSignatories'
    start_urls = ['http://www.unpri.org/signatories/transparency-reports-2019/4506.article/']

    def parse(self, response):
        signatory_page_links = response.xpath('//div[@class="relatedfiles"]/ul/li/a')
        yield from response.follow_all(signatory_page_links, self.details)

    def details(self, response):
        parser = Parser(response)
        return parser.parse_details()
