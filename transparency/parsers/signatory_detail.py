from transparency.parsers.basic_information import BasicInformationParser
from transparency.parsers.esg_details import ESGDetailParser


class Parser:
    def __init__(self, response):
        self.response = response

    def parse_details(self):
        basic_information = BasicInformationParser(self.response)
        esg_url = self.response.xpath('//a[contains(text(), "ESG issues in asset allocation")]/@href').get()

        if esg_url is None:
            yield basic_information
        else:
            yield self.response.follow(
                esg_url,
                self.parse_esg_details,
                cb_kwargs={"basic_information": basic_information.parse()}
            )

    def parse_esg_details(self, response, basic_information):
        esg_details = ESGDetailParser(response)
        basic_information.update(esg_details.parse())
        return basic_information
