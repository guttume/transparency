import scrapy

from transparency.parsers.signatory_detail import Parser


class SignatoriesSpider(scrapy.Spider):
    name = 'signatories'
    start_urls = ['https://www.unpri.org/signatories/transparency-reports-2019/4506.article']
    companies = []

    def parse(self, response):
        self.load_required_companies()

        signatory_page_links = response.xpath('//div[@class="relatedfiles"]/ul/li/a')

        if self.companies_provided():
            for signatory in signatory_page_links:
                signatory_name = self.clean_signatory_name(signatory.xpath('.//h3/text()').get())
                if signatory_name in self.companies:
                    signatory_url = signatory.xpath('.//@href').get()
                    yield scrapy.Request(signatory_url, self.signatory_details)

    def signatory_details(self, response):
        parser = Parser(response)
        yield parser.parse_details()

    def load_required_companies(self):
        with open('companies.txt', 'r') as file:
            for line in file:
                self.companies.append(line.lower().replace('\n', ''))
        return self.companies

    def companies_provided(self):
        return len(self.companies) > 0

    def clean_signatory_name(self, name):
        return name.lower().replace('\n', '').replace('\t', '').strip()
