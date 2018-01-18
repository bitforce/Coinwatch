from coinwrap import Market

from core.strats.arbitrage import *
from core.strats.monitor import *
from core.strats.trailer import *
from core.strats.stats.standard_deviation import *
from core.strats.stats.mean import *
from core.strats.nlp import *

from aux.generic import fetch_watchlist
from aux.generic import print_fail
from aux.generic import watchdata

import datetime
import csv


# =============================================================================
# assist functions
# =============================================================================
def exists_on_my_exchange(name):
    # get list of exchange from extraced scrape of coin's available exchanges
    tradable = []
    my_exchanges = open(exchanges).read()
    for exchange in extract_exchanges(name):
        if exchange in my_exchanges:
            tradable.append(exchange)


# =============================================================================
# ultimate strategy
# =============================================================================


# =============================================================================
# actions
# =============================================================================
def sell(symbol, current_price):
    return simple_mean(symbol, current_price) - simple_standard_deviation(symbol)


def buy(symbol, current_price):
    return simple_mean(symbol, current_price) + simple_standard_deviation(symbol)


def update():
    f = open(watchdata, 'a')
    date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    for crypto in fetch_watchlist():
        price = float(Market().coin(crypto)[0]['price_usd'])  # * unicode bug
        symbol = str(Market().coin(crypto)[0]['symbol'])  # * unicode bug
        csv.writer(f).writerow([date, price, symbol])
        if price < sell(symbol, price):
            print_fail(symbol + ' $' + str(price))
        elif price > buy(symbol, price):
            print_pass(symbol + ' $' + str(price))
        else:
            print symbol + ' $' + str(price)
    f.write('\n')
    f.close()
    # maybe this can be optimized so you don't have to open the file every update
