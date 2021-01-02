from os import environ
from flask import Flask, jsonify
from BillAnalyser import BillAnalyser
from DbConnect import DbConnect
from flask import request

class HttpServer:

    app = Flask(__name__)
    dbConnection = None

    def __init__(self):
        self.dbConnection = DbConnect()

    def start(self):
        """Starts the HttpServer"""
        self.app.run()

    @app.route('/')
    def get_home(self):
        return "The server is up! :D"

    @app.route('/api/bill', methods=['POST'])
    def get_bill(self):
        url = request.args.get('url')
        if self.dbConnection.is_bill_exist(url):
            billAnalyser = BillAnalyser(url)
            bill = billAnalyser.getBillSummary()
            self.dbConnection.add_bill(bill)
        return jsonify(bill)