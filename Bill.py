

# class definition 
# If you need any reference to the info of the bill please check the following links:
#   - https://towardsdatascience.com/lexnlp-library-for-automated-text-extraction-ner-with-bafd0014a3f8

class Bill:
    
    # Every bill has a name, number, and url
    billName = ""
    billNumber = ""
    billUrl = ""

    info = {
        "dates": [],        # e.g  ["2020-03-05", "2017-10-01"]
        "money": [],        # e.g ["100", "500", "30000000"]
        "percentages": [],  # e.g ["50%"]
        "ratios": [],       # e.g ["one to two", "5:4"]
        "companies": [],    # e.g ["Company-Name LLC"]
        "courts": [],       # e.g ["Supreme Court of New York"]
        "cusip": [],        # cusip is a 9 digit code that idetntifies all registered US public stocks  e.g []
        "regulations": []   # e.g [('Code of Federal Regulations', '123 CFR 456')]
    }

    def __init__(self):
        return


    def __iter__(self):
        yield 'billName', self.billName
        yield 'billNumber', self.billNumber
        yield 'billUrl', self.billUrl
        yield 'info', self.info

    def from_dict(self, d):
        for a, b in d.items():
            if isinstance(b, (list, tuple)):
               setattr(self, a, [Bill(x) if isinstance(x, dict) else x for x in b])
            else:
               setattr(self, a, Bill(b) if isinstance(b, dict) else b)

    def set_id(self, id: str) -> None:
        self.id = id
        return None






    