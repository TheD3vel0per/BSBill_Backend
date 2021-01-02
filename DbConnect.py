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

    def get_bill(self, bill_id: str) -> Bill:
        """Gets the bill with the given id and returns it"""
        return Bill(self.__db.collection('Bills').document(bill_id).get().to_dict())

    def add_bill(self, bill: Bill) -> None:
        """Adds the given bill to the database"""
        self.__db.collection('Bills').document('one').set(bill)
        return None
