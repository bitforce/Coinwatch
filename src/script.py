#!/usr/local/bin/python2

from coinwrap import Market
import argparse
import datetime
import math
import time
import csv
import sys
import os.path


# =============================================================================
# GLOBAL VARIABLES
# =============================================================================
YELLOW = '\033[93m'
GREEN = '\033[92m'
WHITE = '\033[1m'
RED = '\033[91m'
END = '\033[0m'

watchlist = '.watchlist.txt'
watchdata = '.watchlist.csv'
m = Market()
args = None
run = False
path = '$HOME'  # READ FROM CONFIG FILE

# =============================================================================
# ASSIST FUNCTIONS
# =============================================================================


def print_warn(string):
    print YELLOW + string + END


def print_bold(string):
    print WHITE + string + END


def print_pass(string):
    print GREEN + string + END


def print_fail(string):
    print RED + string + END


def set_path(newpath):
    global path
    path = newpath


def get_path():
    return path


def fetch_watchlist():
    try:
        a = []
        for e in open(watchlist).read().split('\n')[:-1]:
            a.append(e.split()[:-1][0])  # becomes a list when you split it, so you take [0]
        return a
    except IOError:
        print_fail('failed to open watchlist')
        sys.exit(1)


def read_prices(symbol):
    prices = []
    with open(watchdata, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            if row and row[2] == symbol:  # verify non-empty arr
                prices.append(float(row[1]))
    if not prices:
        return [-1]
    return prices


def low(symbol):  # no price parameter b/c not part of for loop, so we use slower method
    prices = read_prices(symbol)
    low = prices[-1]  # last element in list -> V pythonic
    for price in prices:
        if low > price:
            low = price
    return low


def high(symbol):
    prices = read_prices(symbol)
    high = prices[-1]
    for price in prices:
        if high < price:
            high = price
    return high


def mean(symbol, current_price):  # using price parameter here is more efficient and obvious
    mean = current_price
    prices = read_prices(symbol)
    if len(prices) > 1:
        mean = sum(prices) / len(prices)
    return mean


def stddev(symbol):
    dev = 0
    prices = []
    with open(watchdata, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            if row and row[2] == symbol:
                prices.append(float(row[1]))
    if not prices:
        return 0
    sq = 0
    for price in prices:
        sq += math.pow(price - mean(symbol, price), 2)
    return math.sqrt(sq / len(prices))


def sell(symbol, current_price):  # statistically calculated buy price
    return mean(symbol, current_price) - stddev(symbol)


def buy(symbol, current_price):  # statistically calculated buy price
    return mean(symbol, current_price) + stddev(symbol)

# =============================================================================
# MAIN FUNCTIONS
# =============================================================================


def validate():
    if not os.path.isfile(watchlist):
        print_bold('no watchlist.txt found; creating one now')
        open(watchlist, 'w').close()
    if not os.path.isfile(watchdata):
        print_bold('no watchlist.csv found; creating one now')
        open(watchdata, 'w').close()
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--delay',
                        help='delay of http request; in seconds',
                        default=60,
                        type=long)
    parser.add_argument('-c', '--cycles',
                        help='total number of http requests',
                        default=100,
                        type=long)
    parser.add_argument('-r', '--remove',
                        help='remove cryptos from watchlist',
                        nargs='+')
    parser.add_argument('-a', '--add',
                        help='add cryptos to watchlist',
                        nargs='+')
    parser.add_argument('--low',
                        help='returns lowest price--use ticker symbol',
                        nargs='+')
    parser.add_argument('--high',
                        help='returns lowest price--use ticker symbol',
                        nargs='+')
    parser.add_argument('-w', '--wipe',
                        help='wipe watchlist.txt clean',
                        action='store_true')
    parser.add_argument('-e', '--erase',
                        help='wipe watchlist.csv clean',
                        action='store_true')
    parser.add_argument('--show-watchlist',
                        help='prints watchlist.txt contents',
                        action='store_true')
    parser.add_argument('--show-watchdata',
                        help='prints watchlist.csv contents',
                        action='store_true')
    parser.add_argument('--show-symbols',
                        help='show watchlist with ticker symbols',
                        action='store_true')
    parser.add_argument('--show-stddev',
                        help='shows asset\'s standard deviation',
                        nargs='+')
    parser.add_argument('--set-path',
                        help='sets the watchlists\' location path')
    parser.add_argument('--get-path',
                        help='sets the watchlists\' location path',
                        action='store_true')
    parser.add_argument('--run',
                        help='runs watch daemon',
                        action='store_true')
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit()
    global args
    args = parser.parse_args()
    if args.low:
        for arg in args.low:
            arg = arg.upper()
            if low(arg) < 0:
                print_fail(arg + ' : no pricing data to be read')
                continue
            print arg + ' : ' + str(low(arg))
    if args.high:
        for arg in args.high:
            arg = arg.upper()
            if high(arg) < 0:
                print_fail(arg + ' : no pricing data to be read')
                continue
            print arg + ' : ' + str(high(arg))
    # ----------------------------------------

    # ----------------------------------------
    if args.set_path:  # MAYBE USE A CONFIG FILE?
        set_path(args.set_path)  # FIGURE OUT WAY TO SET PATH SO THAT EVEN AFTER PROGRAM RUNS
    if args.get_path:
        print get_path()
    if args.show_watchlist:
        for name in open(watchlist, 'r'):
            print name,
    if args.show_watchdata:
        for data in open(watchdata, 'r'):
            print data,
    if args.show_stddev:
        for dev in args.show_stddev:
            if stddev(dev) != 0:
                print str(stddev(dev))
    if args.wipe:
        print_warn('wiping watchlist.txt contents')
        open(watchlist, 'w').close()
    if args.erase:
        print_warn('wiping watchlist.csv contents')
        open(watchdata, 'w').close()
    if args.remove:
        for arg in args.remove:
            remove_crypto(arg)
    if args.add:
        for arg in args.add:
            add_crypto(arg)


def update():
    if not fetch_watchlist():
        print_warn('not cryptos in watchlist')
        sys.exit()
    f = open(watchdata, 'a')
    date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    for crypto in fetch_watchlist():
        price = float(m.coin(crypto)[0]['price_usd'])  # * unicode bug
        symbol = str(m.coin(crypto)[0]['symbol'])
        csv.writer(f).writerow([date, price, symbol])
        if price < sell(symbol, price):
            print_fail(symbol + ' $' + str(price))
        elif price > buy(symbol, price):
            print_pass(symbol + ' $' + str(price))
        else:
            print symbol + ' $' + str(price)
    f.write('\n')
    f.close()


def remove_crypto(name):  # *** I know it's not most efficient, but it works
    coins = fetch_watchlist()
    for coin in coins:
        if coin == name:
            coins.remove(coin)
    f = open(watchlist, 'w')
    for coin in coins:
        f.write(str(coin + ' (' + m.coin(coin)[0]['symbol'] + ')\n'))
    f.close()


def add_crypto(name):  # *** method is slow b/c it needs to request server
    if type(m.coin(name)) is not list:
        print_bold('{} : coin name non-existent or mispelled'.format(name))
        return
    f = open(watchlist, 'a')
    if name not in open(watchlist).read():
        f.write(str(name + ' (' + m.coin(name)[0]['symbol'] + ')\n'))
    else:
        print_warn(name + ' is already being tracked')
    f.close()


def run():
    validate()
    if not args.run:
        sys.exit()
    print
    cycles = args.cycles
    while cycles > 0:
        cycles -= 1
        print 'CYCLE ' + str((cycles - args.cycles) * -1)
        print '-----'
        update()
        print_bold('\n...\n')
        time.sleep(args.delay)

# =============================================================================
# RUN
# =============================================================================


run()
