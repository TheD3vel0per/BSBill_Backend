from lexnlp.extract.en.dates import get_dates
from lexnlp.extract.en.entities.nltk_maxent import get_companies
from lexnlp.extract.en.courts import get_courts
from lexnlp.extract.en.money import get_money 
from lexnlp.extract.en.cusip import get_cusip
from lexnlp.extract.en.regulations import get_regulations
from lexnlp.extract.en.ratios import get_ratio_annotations
from lexnlp.extract.en.percents import get_percents

from bs4 import BeautifulSoup
import requests
from WebScraper import WebScraper
from Bill import Bill


class BillAnalyser:
    def __init__(self, url):
        self.url = url
        self.scraper = WebScraper()
        self.bill_text = self.scraper.get_bill_text_from_url(url) # bill text cleaned
        self.bill = Bill() # bill object to store the info in

    def getDate(self):
        dates = list(get_dates(self.bill_text))
        self.bill.info['dates'] = dates

    def getCompanies(self):
        companies = list(get_companies(self.bill_text))
        self.bill.info['companies'] = companies

    def getCusip(self):
        cusip = list(get_cusip(self.bill_text))
        self.bill.info['cusip'] = cusip

    def getCourts(self):
        courts = list(get_courts(self.bill_text))
        self.bill.info['courts'] = courts

    def getMoney(self):
        money = list(get_money(self.bill_text))
        self.bill.info['money'] = money

    def getPercentages(self):
        percentages = list(get_percentages(self.bill_text))
        self.bill.info['percentages'] = percentages
        
    def getRatios(self):
        ratios = list(get_ratios(self.bill_text))
        self.bill.info['ratios'] = ratios

    def getRegulations(self):
        regulations = list(get_regulations(self.bill_text))
        self.bill.info['regulations'] = regulations  

    def getBillSummary(self):
        self.getCompanies()
        self.getCourts()
        self.getCusip()
        self.getDate()
        self.getMoney()
        self.getPercentages()
        self.getRatios()
        self.getRegulations()


if __name__ == "__main__":
    url = "https://www.congress.gov/congressional-record/2019/10/29/house-section/article/H8588-3"

    b = BillAnalyser(url)
    b.getBillSummary()
    print()