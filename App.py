from os import environ
from flask import Flask, jsonify
from BillAnalyser import BillAnalyser
from DbConnect import DbConnect
from flask import request

app = Flask(__name__)
dbConnection = DbConnect()

@app.route('/')
def get_home():
    return "The server is up! :D"

@app.route('/api/bill', methods=['POST'])
def get_bill():
    url = request.args.get('url')
    if dbConnection.is_bill_exist(url):
        billAnalyser = BillAnalyser(url)
        bill = billAnalyser.getBillSummary()
        dbConnection.add_bill(bill)
    return jsonify(bill)

app.run(host="0.0.0.0", port=5000)