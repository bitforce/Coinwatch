from aux.generic import verified_coin
from aux.generic import read_prices


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
def add_exchange(exchange):
    return


def remove_exchange(exchange):
    return


# numeric data display
# --------------------
def get_low(name):
    prices = read_prices(symbol)
    low = prices[-1]
    for price in prices:
        if low > price:
            low = price
    return low


def get_high(name):
    prices = read_prices(symbol)
    high = prices[-1]
    for price in prices:
        if high < price:
            high = price
    return high


def get_simple_percent_changes(name):
    if not verified_coin(name):
        return
    return [m.coin(data[0])[0]['percent_change_1h'],
            m.coin(data[0])[0]['percent_change_24h'],
            m.coin(data[0])[0]['percent_change_7d']]
