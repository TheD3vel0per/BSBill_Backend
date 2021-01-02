from DbConnect import DbConnect
from Bill import Bill

if __name__ == "__main__":
    dbConnection: DbConnect = DbConnect()
    bill: Bill = dbConnection.get_bill('bill1')
    print(dir(bill))