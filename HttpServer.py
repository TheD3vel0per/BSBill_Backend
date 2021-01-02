from os import environ
from flask import Flask, jsonify
import server.DbConnect

class HttpServer:

    app = None
    dbConnection = None

    def __init__(self):
        self.app = Flask(__name__, static_url_path='/build')
        self.dbConnection = server.DbConnect.DbConnect()

    def start(self):
        """Starts the HttpServer"""
        self.app.run()

    @app.route('/api/bill/<url>')
    def get_bill(self, url):
        bill = self.dbConnection.get_bill(url)
        if bill == None:
            #bill = _ # request a proper bill
            self.dbConnection.add_bill(bill)
        return jsonify(bill) # request a proper bill