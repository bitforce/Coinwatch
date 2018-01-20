from coinwrap import Market

from core.strats.arbitrage import *
from core.strats.monitor import *
from core.strats.trailer import *
from core.strats.stats.standard_deviation import *
from core.strats.stats.mean import *
from core.strats.nlp import *

from aux.generic import fetch_watchlist
from aux.generic import print_pass
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
        print_symbol = '{:8}'.format(symbol)
        print_price = '{:>4}'.format('$') + '{0:.2f}'.format(price)
        if price < sell(symbol, price):
            print_fail(print_symbol + print_price)
        elif price > buy(symbol, price):
            print_pass(print_symbol + print_price)
        else:
            print print_symbol + print_price
    f.write('\n')
    f.close()

    # maybe this can be optimized so you don't have to open the file every update
    # also perhaps add how much price has changed in last hour
