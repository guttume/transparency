# -*- coding: utf-8 -*-
import scrapy


class AllSignatoriesSpider(scrapy.Spider):
    name = 'AllSignatories'
    start_urls = ['http://www.unpri.org/signatories/transparency-reports-2019/4506.article/']

    def parse(self, response):
        signatory_page_links = response.xpath('//div[@class="relatedfiles"]/ul/li/a')
        yield from response.follow_all(signatory_page_links, self.details)

    def details(self, response):
        fund_management = response.css('tr#32f3bde967894662b11458d1c48d0a2d label.radio img[src="/Style/img/checkedradio.png"]+span.title b::text').get('NA')
        sub_advised_products = response.css('tr#336bca6d619f473d853ec277caed8e8a label.radio img[src="/Style/img/checkedradio.png"]+span.title b::text').get('NA')
        others = response.css('tr#d896a5424372407589eeddc43843cd5e label.radio img[src="/Style/img/checkedradio.png"]+span.title b::text').get('NA')
        yield {
            'Name': response.css('div.row-fluid div.span12 h2.n-h2::text').get(),
            'Fund management': fund_management.strip(),
            'Fund of funds, manager of managers, sub-advised products': sub_advised_products.strip(),
            'others': others.strip(),
        }
