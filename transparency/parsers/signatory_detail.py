from transparency.parsers.basic_information import BasicInformationParser


class Parser:
    def __init__(self, response):
        self.response = response

    def parse_details(self):
        parser = BasicInformationParser(self.response)
        return parser.parse()
