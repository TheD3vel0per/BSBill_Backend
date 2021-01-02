from lexnlp.extract.en.dates import get_dates
from lexnlp.extract.en.entities.nltk_maxent import get_companies
from lexnlp.extract.en.definitions import get_definitions
from lexnlp.extract.en.money import get_money 
from lexnlp.extract.en.durations import get_durations
from lexnlp.extract.en.amounts import get_amount_annotations, get_amounts
from lexnlp.extract.en.addresses.addresses import get_addresses
from lexnlp.nlp.en.segments.pages import get_pages
from bs4 import BeautifulSoup
import requests

import WebScraper, Bill


class BillAnalyser:
    def __init__(self, url):
        self.url = url
        self.scraper = WebScraper()
        self.scrapper.get_bill_text_from_url(url)
        self.bill = Bill()

    def getDate(self):
        dates = list(get_dates(self.bill_text))
        self.bill.info['dates'] = dates

    def getCompanies(self):
        companies = list(get_companies(self.bill_text))
        self.bill.info['companies'] = companies

    def getAmounts(self):
        amounts = list(get_amounts(self.bill_text))
        self.info['dates'] = amounts

    def getMoney(self):
        money = list(get_money(self.bill_text))
        self.info['money'] = money

    def getDurations(self):
        durations = list(get_amounts(self.bill_text))
        self.info['durations'] = durations

    def getPercentages(self):
        pass

    def getRatios(self):
        pass

    def displayInfo(self):
        print("\n\nInformation from legal text: ")
        print(self.info['dates'])
        print(self.info['companies'])
        print(self.info['amounts'])
        print(self.info['money'])
        print(self.info['durations'])
        print(self.info['percentages'])
        print(self.info['ratios'])



if __name__ == "__main__":
    url = "https://www.congress.gov/congressional-record/2019/10/29/house-section/article/H8588-3"

    b = BillAnalyser(url)