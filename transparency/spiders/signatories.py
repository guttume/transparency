import scrapy


class Signatories(scrapy.Spider):
    name = 'signatories'
    start_urls = [
        'https://www.unpri.org/signatories/transparency-reports-2019/4506.article']

    def parse(self, response):
        for signatory in response.css('div.relatedfiles ul li'):
            yield {
                'name': signatory.css('a h3::text').get(),
                'link': signatory.css('a::attr(href)').get()
            }
