#!/usr/bin/python2

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

def apoptosis(): # self-delete script from local machine, but keep w-list/data
    sys.exit()

def fetch_watchlist():
    try:
        return open(watchlist).read().split('\n')[:-1]
    except IOError:
       print_fail('failed to open watchlist')
       sys.exit(1)

def mean(symbol, current_price):
    mean = current_price
    prices = []
    with open(watchdata, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            if row and row[2] == symbol: # * verify non-empty array
                prices.append(float(row[1]))
    if len(prices) > 1:
        mean = sum(prices)/len(prices)
    return mean


def stddev(symbol):
    dev = 0
    prices = []
    with open(watchdata, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            if row and row[2] == symbol:
                prices.append(float(row[1]))
    sq = 0
    for price in prices:
        sq += math.pow(price - mean(symbol, price), 2)
    return math.sqrt(sq / len(prices))

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
    parser.add_argument('--run',
            help='runs watch daemon',
            action='store_true')
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit()
    global args
    args = parser.parse_args()
    if args.show_watchlist:
        for name in open(watchlist, 'r'):
            print name,
    if args.show_watchdata:
        for data in open(watchdata, 'r'):
            print data,
    if args.wipe:
        print_warn('wiping watchlist.txt contents')
        open(watchlist, 'w').close()
    if args.erase:
        print_warn('wiping watchlist.csv contents')
        open(watchdata, 'w').close()
    if args.remove is not None:
        for arg in args.remove:
            remove_crypto(arg)
    if args.add is not None:
        for arg in args.add:
            add_crypto(arg)

def update():
    if not fetch_watchlist():
        print_warn('not cryptos in watchlist')
        sys.exit()
    f = open(watchdata, 'a')
    date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    for crypto in fetch_watchlist():
        price = float(m.coin(crypto)[0]['price_usd']) # * unicode bug
        symbol = str(m.coin(crypto)[0]['symbol'])
        csv.writer(f).writerow([date, price, symbol])
        if price < mean(symbol, price) - stddev(symbol):
            print_fail(symbol + ' $' + str(price))
        elif price > mean(symbol, price) + stddev(symbol):
            print_pass(symbol + ' $' + str(price))
        else:
            print symbol + ' $' + str(price)
    f.write('\n')
    f.close()


def remove_crypto(name): # *** I know it's not most efficient, but it works
    coins = fetch_watchlist()
    for coin in coins:
        if coin == name:
            coins.remove(coin)
    f = open(watchlist, 'w')
    for coin in coins:
        f.write(coin + '\n')
    f.close()


def add_crypto(name): # *** method is slow b/c it needs to request server
    if type(m.coin(name)) is not list:
        print_bold('{} : coin name non-existent or mispelled'.format(name))
        return
    f = open(watchlist, 'a')
    if name not in open(watchlist).read():
        f.write(name + '\n')
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
        print 'CYCLE ' + str((cycles - args.cycles)*-1)
        print '-----'
        update()
        print
        time.sleep(args.delay)

# =============================================================================
# RUN
# =============================================================================
run()
