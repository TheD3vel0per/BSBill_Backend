from BillAnalyser import BillAnalyser
from DbConnect import DbConnect

if __name__ == "__main__":
    url = "https://www.congress.gov/congressional-record/2019/10/29/house-section/article/H8588-3"
    b = BillAnalyser(url)
    b.getBillSummary()

    print(b.bill.info['dates'])

# if __name__ == "__main__":
#     dbConnection: DbConnect = DbConnect()
#     dbConnection.get_bill('best1')