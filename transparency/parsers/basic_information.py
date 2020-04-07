class BasicInformationParser:
    COMPANY_NAME = '//div[@class="row-fluid"]//div[@class="span12"]//h2[@class="n-h2"]//text()'
    TYPE_OF_ORGANISATION = '//h3[contains(text(), "Select the type that best describes your organisation or the services you provide")]/parent::div/following-sibling::div/div/div/label/img[@src="/Style/img/checkedradio.png"]/following-sibling::span/b/text()'
    FUND_MANAGEMENT = '//tr[@id="32f3bde967894662b11458d1c48d0a2d"]/td/div/div/div/div/label/img[@src="/Style/img/checkedradio.png"]/following-sibling::span/b/text()'
    SUB_ADVISED_PRODUCTS = '//tr[@id="336bca6d619f473d853ec277caed8e8a"]/td/div/div/div/div/label/img[@src="/Style/img/checkedradio.png"]/following-sibling::span/b/text()'
    OTHER_SERVICES = '//tr[@id="d896a5424372407589eeddc43843cd5e"]/td/div/div/div/div/label/img[@src="/Style/img/checkedradio.png"]/following-sibling::span/b/text()'
    FURTHER_SERVICES = '//h3[contains(text(), "Further options")]/parent::div/following-sibling::div/div/div/label/img[@src="/Style/img/checkedcheckbox.png"]/following-sibling::span/b/text()'
    COMPANY_DETAILS = '//h3[contains(text(), "01.2")]/parent::div[contains(@class, "sub-question")]/following-sibling::div/span/p/text()'
    HEADQUARTERS = '//div[@class="countries"]//span[@class="response"]//text()'
    COUNTRY_OFFICES = '//h3[contains(text(), "Indicate the number of countries in which you have offices (including your headquarters)")]/ancestor::div[@class="radio_parent"]/div/div/div/label/img[@src="/Style/img/checkedradio.png"]/following-sibling::span/b/text()'
    TOTAL_STAFF = '//h3[contains(text(), "number of staff")]/ancestor::div[@class="group"]/div/div/div/span[@class="response number"]/text()'
    HAVE_SUBSIDIARIES = '//h3[contains(text(), 3.1)]/ancestor::div[@class="radio_parent"]/div/div/div/label/img[@src="/Style/img/checkedradio.png"]/following-sibling::span/b/text()'
    YEAR_END = '//h3[contains(text(), "4.1")]/ancestor::div[@class="group"]/div/div/div/span[@class="response date"]/text()'
    AUM = '//tr[@id="survey_question_eecc99ddbe254b6b986276a57cb00d21"]/td/input/@value'
    ASSETS = '//tr[@id="pri_usd_eecc99ddbe254b6b986276a57cb00d21"]/td/input/@value'
    SUBSIDIARIES_DETAILS = '//h3[contains(text(), "03.3")]/parent::div[contains(@class, "sub-question")]/following-sibling::div/span/p/text()'
    AUM_DETAILS = '//h3[contains(text(), "04.5")]/parent::div[contains(@class, "sub-question")]/following-sibling::div/span/p/text()'
    AUM_CURRENCY = '//select[@id="ea7f13c4520843fa8d40d90e26f03056"]/option[@selected="selected"]/text()'
    SUBJECT_TO_EXECUTION = '//h3[contains(text(), 04.4)]/parent::div/following-sibling::div/div/div/div/div/label/img[@src="/Style/img/checkedcheckbox.png"]/following-sibling::span/b/text()'
    DISCLOSE_ASSET = '//h3[contains(text(), "06.1")]/parent::div/following-sibling::div/div/div/div/div/label/input[@checked="checked"]/following-sibling::span/b/text()'
    OFF_BALANCE_SHEET = '//h3[contains(text(), "06.3")]/parent::div/following-sibling::div/div/div/label/img[@src="/Style/img/checkedradio.png"]/following-sibling::span/b/text()'
    FIDUCIARY_MANAGERS = '//h3[contains(text(), "06.3")]/parent::div/following-sibling::div/div/div/label/img[@src="/Style/img/checkedradio.png"]/following-sibling::span/b/text()'

    def __init__(self, response):
        self.response = response

    def parse(self):
        return {
            'Name': self.parse_details(self.COMPANY_NAME),
            'Type of organisation': self.parse_details(self.TYPE_OF_ORGANISATION),
            'Fund management': self.parse_details(self.FUND_MANAGEMENT),
            'Fund of funds, manager of managers, sub-advised products': self.parse_details(self.SUB_ADVISED_PRODUCTS),
            'others': self.parse_details(self.OTHER_SERVICES),
            'Further options': self.parse_details(self.FURTHER_SERVICES),
            'Company details': self.parse_all_details(self.COMPANY_DETAILS, False),
            'Headquarters': self.parse_details(self.HEADQUARTERS),
            'Number of countries': self.parse_details(self.COUNTRY_OFFICES),
            'Total staffs': self.parse_details(self.TOTAL_STAFF),
            'Have subsidiaries': self.parse_details(self.HAVE_SUBSIDIARIES),
            'Subsidiaries details': self.parse_all_details(self.SUBSIDIARIES_DETAILS, False),
            'Year end': self.parse_details(self.YEAR_END),
            'AUM': self.parse_all_details(self.AUM),
            'AUM currency': self.parse_details(self.AUM_CURRENCY),
            'Assets in USD': self.parse_all_details(self.ASSETS),
            'Assets subject to an execution and/or advisory approach': self.parse_details(self.SUBJECT_TO_EXECUTION),
            'How you would like to disclose your asset class mix': self.parse_details(self.DISCLOSE_ASSET),
            'Indicate whether your organisation has any off-balance sheet assets': self.parse_details(
                self.OFF_BALANCE_SHEET),
            'Indicate whether your organisation uses fiduciary managers': self.parse_details(self.FIDUCIARY_MANAGERS)
        }

    def parse_details(self, path):
        return self.response.xpath(path).get('').strip()

    def parse_all_details(self, path, comma_separated=True):
        results = self.response.xpath(path).getall()
        if len(results) == 0:
            return ''

        if len(results) == 1:
            return results[0]

        if comma_separated:
            return ', '.join(results)

        return ''.join(results)
