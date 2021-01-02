from os import environ
from flask import Flask, jsonify
from BillAnalyser import BillAnalyser
from DbConnect import DbConnect
from flask import request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
dbConnection = DbConnect()

@app.route('/api/bill', methods=['GET', 'POST'])
@cross_origin()
def get_bill():
    url = request.args.get('url')
    if dbConnection.is_bill_exist(url):
        billAnalyser = BillAnalyser(url)
        bill = billAnalyser.getBillSummary()
        dbConnection.add_bill(bill)
        return jsonify(dict(bill))
    return jsonify({})

@app.route('/')
def get_home():
    return "The server is up! :D"

app.run(host="0.0.0.0", port=8080)