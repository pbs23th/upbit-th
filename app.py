from flask import Flask, render_template, jsonify
import ccxt
import requests

app = Flask(__name__)


def get_orderbook(market):
    url = f"https://th-api.upbit.com/v1/orderbook?markets={market}"
    headers = {"Accept": "application/json"}
    response = requests.request("GET", url, headers=headers).json()
    response = response[0]['orderbook_units'][0]
    return response


def get_binance_orderbook(market):
    response = ccxt.binance().fetch_order_book(market)
    content = {
        'bid_price' : response['bids'][0][0],
        'ask_price' : response['asks'][0][0],
        'bid_size' : response['bids'][0][1],
        'ask_size' : response['asks'][0][1],
    }
    return content


@app.route('/')
def home():  # put application's code here
    data_1 = get_orderbook("THB-BTC")
    data_2 = get_orderbook("USDT-BTC")
    data_3 = get_orderbook("THB-USDT")
    data_4 = get_binance_orderbook('BTC/USDT')
    data_1['bid_thb'] = int(data_1['bid_price'])
    data_1['ask_thb'] = int(data_1['ask_price'])
    data_2['bid_thb'] = int(data_2['bid_price'] * data_3['bid_price'])
    data_2['ask_thb'] = int(data_2['ask_price'] * data_3['ask_price'])
    data_4['bid_thb'] = int(data_4['bid_price'] * data_3['bid_price'])
    data_4['ask_thb'] = int(data_4['ask_price'] * data_3['ask_price'])
    return render_template('index.html', data_1=data_1, data_2=data_2, data_4=data_4)


@app.route('/pricedata')
def pricedata():
    data_1 = get_orderbook("THB-BTC")
    data_2 = get_orderbook("USDT-BTC")
    data_3 = get_orderbook("THB-USDT")
    data_4 = get_binance_orderbook('BTC/USDT')
    data_1['bid_thb'] = int(data_1['bid_price'])
    data_1['ask_thb'] = int(data_1['ask_price'])
    data_2['bid_thb'] = int(data_2['bid_price'] * data_3['bid_price'])
    data_2['ask_thb'] = int(data_2['ask_price'] * data_3['ask_price'])
    data_4['bid_thb'] = int(data_4['bid_price'] * data_3['bid_price'])
    data_4['ask_thb'] = int(data_4['ask_price'] * data_3['ask_price'])
    data = [data_1, data_2, data_3, data_4]
    return jsonify(data)


if __name__ == '__main__':
    app.run()
