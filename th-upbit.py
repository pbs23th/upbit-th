import requests
import ccxt


class upbit:
    # def __init__(self):
    #     pass

    def get_orderbook(self):
        binance = ccxt.binance().fetch_order_book('BTC/USDT')
        print(binance['bids'][0])
        print(binance['asks'][0])
        return


upbit().get_orderbook()
