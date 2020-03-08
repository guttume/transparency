import scrapy


class Signatories(scrapy.Spider):
    name = 'signatories'
    start_urls = [
        'https://www.unpri.org/signatories/transparency-reports-2019/4506.article']

    def parse(self, response):
        signatory_page_links = response.css('div.relatedfiles ul li a')
        yield from response.follow_all(signatory_page_links, self.details)

    def details(self, response):
        fund_management = response.css('tr#32f3bde967894662b11458d1c48d0a2d label.radio img[src="/Style/img/checkedradio.png"]+span.title b::text').get()
        sub_advised_products = response.css('tr#336bca6d619f473d853ec277caed8e8a label.radio img[src="/Style/img/checkedradio.png"]+span.title b::text').get()
        others = response.css('tr#d896a5424372407589eeddc43843cd5e label.radio img[src="/Style/img/checkedradio.png"]+span.title b::text').get()
        yield {
            'Name': response.css('div.row-fluid div.span12 h2.n-h2::text').get(),
            'Fund management': fund_management.strip() if fund_management is not None else 'NA',
            'Fund of funds, manager of managers, sub-advised products': sub_advised_products.strip() if sub_advised_products is not None else 'NA',
            'others': others.strip() if others is not None else 'NA',
        }
