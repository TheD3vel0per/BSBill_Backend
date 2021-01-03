import requests
import re
from bs4 import BeautifulSoup

import BillAnalyser

class WebScraper:
    """
    Class to scrap from either a Canadian or American website and then return the text to analyze
    """
    def __init__(self, url):
        self.url = url
        self.us_text_class = "txt-box"   # US site's class for the text to extract in the html
        self.can_text_class = "publication-container-content"         # Canada's site's class for the text to extract in the html

    # function to check which country bill is from.
    def parse_url(self, url):
        # check url and see if its congress.gov or parl.ca
        if re.findall(r"(congress.gov)", url):
            return "US" # just return US for now
        elif re.findall(r"(parl.ca)", url):
            return "CAN"
        else:
            print("Country not recognized")
            return

    # text normalization of bill content
    # strip some of the html tags out of the string
    def clean(self, SoupObject):
        clean_str = str(SoupObject).replace("<div>","").replace("</div>", "")
        clean_str = clean_str.replace("<span>","").replace("</span>", "")
        clean_str = clean_str.replace("<a>","").replace("</a>", "")
        clean_str = clean_str.replace("<pre>","").replace("</pre>", "")
        clean_str = clean_str.replace("<h1>","").replace("</h1>", "")
        clean_str = clean_str.replace("<h2>","").replace("</h2>", "")
        clean_str = clean_str.replace("<h3>","").replace("</h3>", "")
        clean_str = clean_str.replace("<h4>","").replace("</h4>", "")
        clean_str = clean_str.replace("<h5>","").replace("</h5>", "")
        clean_str = clean_str.replace("<h6>","").replace("</h6>", "")
        return clean_str

    #function to extract the text content of the bill
    def get_bill_text_from_url(self):
        url = self.url
        # Check url to see if from US or Canadian site
        self.country_code = self.parse_url(url) 
        
        # First get text from url
        self.page = requests.get(url).content
        self.html = BeautifulSoup(self.page, 'html.parser')
        #print(self.html)
        
        if self.country_code == "US":
            self.text = self.html.find_all("div", class_=self.us_text_class)
        elif self.country_code == "CAN":
            self.text = self.html.find_all("div", class_=self.can_text_class)
        else:
            print("Country code invalid.")
            self.text = ""

        return self.clean(self.text)

    def get_bill_name(self):
        name = ""
        if self.country_code == "US":
            name = self.html.find_all("h2")[4]
        elif self.country_code == "CAN":
            name = self.html.find_all("h1", class_="page-title")[0]
        else:
            print("Country code invalid.")
            return ""
        return self.clean(name)

    

if __name__ == "__main__":
    us_url = "https://www.congress.gov/congressional-record/2019/10/29/house-section/article/H8588-3"
    can_url = "https://parl.ca/DocumentViewer/en/43-2/bill/C-7/second-reading"
    random_url = "https://www.google.com" # should break the code

    #w = WebScraper()
    #txt = w.get_bill_text_from_url(us_url)

    b = BillAnalyser(us_url)

