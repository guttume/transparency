import scrapy


class Signatories(scrapy.Spider):
    name = 'signatories'
    start_urls = ['https://www.unpri.org/signatories/transparency-reports-2019/4506.article']

    def parse(self, response):
        signatory_page_links = response.xpath('//div[@class="relatedfiles"]/ul/li/a')
        requested_signatory = getattr(self, 'company', None)
        if requested_signatory is not None:
            for signatory in signatory_page_links:
                signatory_name = signatory.xpath('.//h3/text()').get()
                if signatory_name.lower().find(requested_signatory.lower()) != -1:
                    signatory_url = signatory.xpath('.//@href').get()
                    yield scrapy.Request(signatory_url, self.signatory_details)

    def signatory_details(self, response):
        # category_and_services = response.xpath('//a[@id="38c2a07a5d084d6e83f67409e7b5be74"]')
        # services_and_funds = category_and_services.xpath('./parent::div/div/div/div/h3[contains(text(), "Select the services and funds you offer")]/parent::div/following-sibling::table')
        fund_management = response.css('tr#32f3bde967894662b11458d1c48d0a2d label.radio img[src="/Style/img/checkedradio.png"]+span.title b::text').get('NA')
        sub_advised_products = response.css('tr#336bca6d619f473d853ec277caed8e8a label.radio img[src="/Style/img/checkedradio.png"]+span.title b::text').get('NA')
        others = response.css('tr#d896a5424372407589eeddc43843cd5e label.radio img[src="/Style/img/checkedradio.png"]+span.title b::text').get('NA')
        further_options = getFurtherOptions(response.xpath('//a[@id="38c2a07a5d084d6e83f67409e7b5be74"]/following-sibling::div/div[@class="checkbox_parent"]/div[@class=" type_K parent_^"]/div[@class="question-block"]'))

        yield {
            'Name': response.css('div.row-fluid div.span12 h2.n-h2::text').get(),
            'Fund management': fund_management.strip(),
            'Fund of funds, manager of managers, sub-advised products': sub_advised_products.strip(),
            'others': others.strip(),
            'Further options': further_options
        }

    def getFurtherOptions(path):
        options = []
        for option in path:
            options.append(option.xpath('./div/label/img[@src="/Style/img/checkedcheckbox.png"]/following-sibling::span/b/text()').get(''))

        if len(options) == 0:
            return 'NA'

        if len(options) == 1:
            return options[0]

        return ', '.join(options)
