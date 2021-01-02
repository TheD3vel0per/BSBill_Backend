from os import environ
import firebase_admin
from firebase_admin import credentials, firestore
from Bill import Bill

class DbConnect:

    def __init__(self):
        self.__cred = credentials.Certificate('./serviceAccountKey.json')
        self.__default_app = firebase_admin.initialize_app(self.__cred)
        self.__db = firebase_admin.firestore.client()
        return

    def is_bill_exist(self, url: str) -> bool:
        """Finds the bill with the given url and returns whether it exists,
           returns false if the bill does not exist"""
        return self.__db.collection('Bills').where("billUrl", "==", url).get().len() == 0

    def add_bill(self, bill: Bill) -> None:
        """Adds the given bill to the database"""
        bill['_id'] = self.__db.collection('Bills').document().id
        self.__db.collection('Bills').document('one').set(bill)
        return None
