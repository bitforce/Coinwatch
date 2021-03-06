from coinwrap import Market

from aux.extract import extract_all_exchanges
from aux.generic import fetch_exchanges
from aux.generic import fetch_watchlist
from aux.generic import verified_coin
from aux.generic import read_prices
from aux.generic import print_fail
from aux.generic import print_warn
from aux.generic import exchanges
from aux.generic import watchlist


# global var
# ----------
m = Market()


# configuration
# -------------
def get_path():
    # if config file not set, then return current dir
    return path


def set_path(newpath):
    global path
    path = ''
    # get os type and then appropriate use '$HOME' or '$home', etc...


# common args
# -----------
def add_crypto(name):
    if not verified_coin(name):
        return
    f = open(watchlist, 'a')
    if name not in open(watchlist).read():
        f.write(str(name + ' (' + m.coin(name)[0]['symbol'] + ')\n'))
    else:
        print_warn(name + ' is already being tracked')
    f.close()


def remove_crypto(name):
    coins = fetch_watchlist()
    for coin in coins:
        if coin == name:
            coins.remove(coin)
    f = open(watchlist, 'w')
    for coin in coins:
        f.write(str(coin + ' (' + m.coin(coin)[0]['symbol'] + ')\n'))
    f.close()


# rare args
# ---------
def add_exchange(name):
    if name not in extract_all_exchanges():
        print_fail('{} : exchange non-existent or mispelled'.format(name))
        return
    f = open(exchanges, 'a')
    if name not in open(exchanges).read():
        f.write(name + '\n')
    else:
        print_warn(name + ' already exists')
    f.close()


def remove_exchange(name):
    arr = fetch_exchanges()
    for exchange in arr:
        if exchange == name:
            arr.remove(exchange)
    f = open(exchanges, 'w')
    for exchange in arr:
        f.write(exchange + '\n')
    f.close()


# numeric data display
# --------------------
def get_low(symbol):
    prices = read_prices(symbol)
    low = prices[-1]
    for price in prices:
        if low > price:
            low = price
    return low


def get_high(symbol):
    prices = read_prices(symbol)
    high = prices[-1]
    for price in prices:
        if high < price:
            high = price
    return high


def get_standard_deviation(symbol):
    return


def get_percent_change(symbol):
    return


def get_simple_percent_changes(name):
    return [m.coin(name)[0]['percent_change_1h'],
            m.coin(name)[0]['percent_change_24h'],
            m.coin(name)[0]['percent_change_7d']]
