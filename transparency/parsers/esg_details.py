class ESGDetailParser:
    UNDERTAKES_SCENARIO_ANALYSIS = '//h3[contains(text(), "13.1")]/parent::div/following-sibling::div/div/div/label/img[@src="/Style/img/checkedcheckbox.png"]/following-sibling::span/b/text()'
    ASSET_ALLOCATION = '//h3[contains(text(), "13.2")]/parent::div/following-sibling::div/div/div/div/div/label/img[@src="/Style/img/checkedcheckbox.png"]/following-sibling::span/b/text()'
    ADDITIONAL_DETAILS = '//h3[contains(text(), "13.3")]/parent::div/following-sibling::div/span/p/text()'
    FUTURE_PLANS = '//h3[contains(text(), 13.4)]/parent::div/following-sibling::div/div/div/label/img[@src="/Style/img/checkedcheckbox.png"]/following-sibling::span/b/text()'
    WHO_USES = '//h3[contains(text(), 13.5)]/parent::div/following-sibling::div/div/div/label/img[@src="/Style/img/checkedcheckbox.png"]/following-sibling::span/b/text()'
    IMPACTS_OF_CLIMATE = '//h3[contains(text(), 13.6)]/parent::div/following-sibling::div/div/div/label/img[@src="/Style/img/checkedradio.png"]/following-sibling::span/b/text()'
    CLIMATE_RANGE = '//h3[contains(text(), 13.7)]/parent::div/following-sibling::div/div/div/label/img[@src="/Style/img/checkedradio.png"]/following-sibling::span/b/text()'
    RISKS_AND_OPPORTUNITIES = '//h3[contains(text(), "14.1")]/parent::div/following-sibling::div/div/div/label/img[@src="/Style/img/checkedcheckbox.png"]/following-sibling::span/b/text()'
    CLIMATE_ACTIVITIES = '//h3[contains(text(), "14.2")]/parent::div/following-sibling::div/div/div/label/img[@src="/Style/img/checkedcheckbox.png"]/following-sibling::span/b/text()'
    CLIMATE_ORGANISATION = '//h3[contains(text(), "14.3")]/parent::div/following-sibling::div/div/div/label/img[@src="/Style/img/checkedcheckbox.png"]/following-sibling::span/b/text()'
    TOOLS_OR_FRAMEWORKS = '//h3[contains(text(), "14.4")]/parent::div/following-sibling::div/span/p/text()'
    CLIMATE_ADDITIONAL_INFORMATION = '//h3[contains(text(), "14.5")]/parent::div/following-sibling::div/span/p/text()'
    INTEGRATED_RISKS = '//h3[contains(text(), "14.8")]/parent::div/following-sibling::div/div/div/label/img[@src="/Style/img/checkedradio.png"]/following-sibling::span/b/text()'
    OWNERSHIP_ACTIVITIES = '//h3[contains(text(), "14.9")]/parent::div/following-sibling::div/div/div/label/img[@src="/Style/img/checkedradio.png"]/following-sibling::span/b/text()'
    ENVIRONMENTAL_AND_SOCIAL = '//h3[contains(text(), "15.1")]/parent::div/following-sibling::div/div/div/label/img[@src="/Style/img/checkedradio.png"]/following-sibling::span/b/text()'
    ENVIRONMENTAL_INVESTMENT = '//h3[contains(text(), "15.2")]/parent::div/following-sibling::div/div/div/span/text()'
    AREAS_OF_INVESTMENT = '//h3[contains(text(), "15.3")]/parent::div/following-sibling::div/div/div/div/div/label/img[@src="/Style/img/checkedcheckbox.png"]/following-sibling::span/b/text()'

    def __init__(self, response):
        self.response = response

    def parse(self):
        return {
            "Indicate whether the organisation undertakes scenario analysis and/or modelling and provide a description of the scenario analysis (by asset class, sector, strategic asset allocation, etc.).":
                self.parse_all_details(self.UNDERTAKES_SCENARIO_ANALYSIS),
            "Indicate if your organisation considers ESG issues in strategic asset allocation and/or allocation of assets between sectors or geographic markets.":
                self.parse_all_details(self.ASSET_ALLOCATION),
            "ESG issues: additional information": self.parse_all_details(self.ADDITIONAL_DETAILS),
            " Describe how the organisation is using scenario analysis to manage climate-related risks and opportunities, including how the analysis has been interpreted, the results and any future plans.":
                self.parse_all_details(self.FUTURE_PLANS),
            "Indicate who uses this analysis.": self.parse_all_details(self.WHO_USES),
            "Indicate whether the organisation has evaluated the impacts of climate-related risk, beyond the investment time-horizon, on the organisations investment strategy.": self.parse_details(self.IMPACTS_OF_CLIMATE),
            "Indicate whether a range of climate scenarios is used": self.parse_details(self.CLIMATE_RANGE),
            "Some investment risks and opportunities arise as a result of long term trends. Indicate which of the following are considered.": self.parse_all_details(self.RISKS_AND_OPPORTUNITIES),
            "Indicate which of the following activities you have undertaken to respond to climate change risk and opportunity": self.parse_all_details(self.CLIMATE_ACTIVITIES),
            "Indicate which of the following tools the organisation uses to manage climate-related risks and opportunities.": self.parse_all_details(self.CLIMATE_ORGANISATION),
            "If you selected disclosure on emissions risks, list any specific climate related disclosure tools or frameworks that you used.": self.parse_all_details(self.TOOLS_OR_FRAMEWORKS),
            "Climate related additional information": self.parse_all_details(self.CLIMATE_ADDITIONAL_INFORMATION),
            "Indicate whether climate-related risks are integrated into overall risk management and explain the risks management processes for identifying, assessing, and managing climate-related risks.":
                self.parse_details(self.INTEGRATED_RISKS),
            "Indicate whether the organisation undertakes active ownership activities to encourage TCFD adoption.":
                self.parse_details(self.OWNERSHIP_ACTIVITIES),
            "Indicate if your organisation allocates assets to, or manages, funds based on specific environmental and social themed areas.": self.parse_details(self.ENVIRONMENTAL_AND_SOCIAL),
            "Indicate the percentage of your total AUM invested in environmental and social themed areas.":
                self.parse_all_details(self.ENVIRONMENTAL_INVESTMENT, False),
            "Specify which thematic area(s) you invest in, indicate the percentage of your AUM in the particular asset class and provide a brief description.": self.parse_all_details(self.AREAS_OF_INVESTMENT)
        }

    def parse_details(self, path):
        return self.response.xpath(path).get('').strip()

    def parse_all_details(self, path, comma_separated=True):
        results = self.response.xpath(path).getall()
        results = list(map(lambda x: x.strip(" \r\n\t"), results))
        if len(results) == 0:
            return ''

        if len(results) == 1:
            return results[0]

        if comma_separated:
            return ', '.join(results)

        return ''.join(results)
