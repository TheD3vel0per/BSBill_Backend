from lexnlp.extract.en.dates import get_dates
from lexnlp.extract.en.entities.nltk_maxent import get_companies
from lexnlp.extract.en.money import get_money, get_money_annotations
from lexnlp.extract.en.cusip import get_cusip
from lexnlp.extract.en.regulations import get_regulations
from lexnlp.extract.en.ratios import get_ratios
from lexnlp.extract.en.percents import get_percents

import collections
import pandas as pd
# import requests
from WebScraper import WebScraper
from Bill import Bill


class BillAnalyser:
    def __init__(self, url):
        # bill object to store the info in
        self.bill = Bill()
        self.bill.billUrl = url

        # Get the bill text
        self.url = url
        self.scraper = WebScraper(url)
        self.bill_text = self.scraper.get_bill_text_from_url()
        self.bill.billName = self.scraper.get_bill_name()

        # Get the 5 most common words
        #self.mostCommonWords(self.bill_text)
        #print(self.stopwords)

    """
    def mostCommonWords(self, bill_text):
        # Write the bill text to a txt file
        text_file = open("bill.txt", "w")
        n = text_file.write(bill_text)
        text_file.close()

        file = open('bill.txt')
        fp = file.read()

        stopwords = set(line.strip() for line in open('stopwords.txt'))
        stopwords = stopwords.union(set(['a', 'mr', 'mrs', 'ms', 'whoever', 'cannot', 'one', 'said', 'one', 'gets', 'from']))
        wordcount = {}

        # Remove punctuation, make all words lower case
        for word in fp.lower().split():
            word = word.replace(".", "")
            word = word.replace(",", "")
            word = word.replace(":", "")
            word = word.replace("\"", "")
            word = word.replace("!", "")
            word = word.replace("â€œ", "")
            word = word.replace("â€˜", "")
            word = word.replace("*", "")

            # Count word frequency now, ignoring all stopwords
            if word not in stopwords:
                if word not in wordcount:
                    wordcount[word] = 1
                else:
                    wordcount[word] += 1

        # Find the 5 most common words
        word_counter = collections.Counter(wordcount)
        for word, count in word_counter.most_common(5):
            print(word, ": ", count)

        # Close the file
        file.close()"""

    def getDate(self):
        mem = []
        dates = list(get_dates(self.bill_text))
        for date in dates:
            mem.append(str(date))
        self.bill.info['dates'] = mem

    def getCompanies(self):
        mem = []
        companies = list(get_companies(self.bill_text))
        for company in companies:
             mem.append(str(company[0]+" "+str(company[1])))
        self.bill.info['companies'] = mem

    def getCusip(self):
        mem = []
        cusip = list(get_cusip(self.bill_text))
        for code in cusip:
            mem.append(str(code['text']))
        self.bill.info['cusip'] = mem

    def getMoney(self):
        mem = []
        money = list(get_money(self.bill_text))
        for mon in money:
            mem.append(str(mon[0]))
        self.bill.info['money'] = mem

    def getRegulations(self):
        mem = []
        regulations = list(get_regulations(self.bill_text))
        for reg in regulations:
            mem.append(str(reg[1]))
        self.bill.info['regulations'] = mem

    def getPercentages(self):
        mem = []
        percentages = list(get_percents(self.bill_text))
        for percent in percentages:
            mem.append(str(percent[1])+str(percent[0]))
        self.bill.info['percentages'] = mem

    def getRatios(self):
        mem = []
        ratios = list(get_ratios(self.bill_text))
        self.bill.info['ratios'] = ratios
        for ratio in ratios:
            mem.append(str(ratio[0]) + " : " + str(ratio[1]))
        self.bill.info['ratios'] = mem

    def getBillSummary(self):
        # Extract some info using Lex NLP
        self.getCompanies()
        self.getCusip()
        self.getDate()
        self.getMoney()
        self.getPercentages()
        self.getRatios()
        self.getRegulations()
        self.printSummary()
        return self.bill

    def printSummary(self):
        print(self.bill.info['dates'])
        print(self.bill.info['companies'])
        print(self.bill.info['cusip'])
        print(self.bill.info['money'])
        print(self.bill.info['regulations'])

if __name__ == "__main__":
    url = "https://www.congress.gov/congressional-record/2020/3/5/extensions-of-remarks-section/article/e268-5?q=%7B%22search%22%3A%5B%22health+care%22%5D%7D&s=2&r=1"
    url = "https://www.congress.gov/bill/116th-congress/house-bill/3498/text?format=txt&q=%7B%22search%22%3A%5B%22immigration%22%5D%7D&r=4&s=4"
    b = BillAnalyser(url)
    b.getBillSummary()
