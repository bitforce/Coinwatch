from aux.generic import read_prices


# =============================================================================
# assist functions
# =============================================================================


# =============================================================================
# main functions
# =============================================================================

# commandline-option functions
# ----------------------------------------
def add_crypto(name):
    if type(m.coin(name)) is not list:
        print_bold('{} : coin crypto non-existent or mispelled'.format(name))
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


def add_exchange(exchange):
    return


def remove_exchange(exchange):
    return


# data storage functions
# ----------------------------------------
def backfill():
    return


# configuration functions
# ---------------------------------------
def get_path():
    # if config file not set, then return current dir
    return path


def set_path(newpath):
    global path
    path = ''
    # get os type and then appropriate use '$HOME' or '$home', etc...


# numeric data analysis functions
# ----------------------------------------
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


def get_percent_change(name, interval):
    if len(data) > 4 or len(data) < 2:
        print_fail('must specify at least one asset and a combination of the following: ' +
                   '1 24 7')
        return
    if type(m.coin(data[0])) is not list:
        print_fail('{} : coin name non-existent or mispelled'.format(data[0]))
        return
    times = ['1', '24', '7']
    for d in data[1:]:
        if d in times:
            if d == times[0]:
                print 'last hour : ' + m.coin(data[0])[0]['percent_change_1h'] + '%'
            elif d == times[1]:
                print 'last day : ' + m.coin(data[0])[0]['percent_change_24h'] + '%'
            elif d == times[2]:
                print 'this week : ' + m.coin(data[0])[0]['percent_change_7d'] + '%'
