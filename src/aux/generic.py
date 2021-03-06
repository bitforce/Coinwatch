from coinwrap import Market

import csv
import os.path


YELLOW = '\033[93m'
GREEN = '\033[92m'
WHITE = '\033[1m'
RED = '\033[91m'
END = '\033[0m'

exchanges = 'out/exchanges.txt'
watchlist = 'out/watchlist.txt'
watchdata = 'out/watchlist.csv'
backfills = 'out/backfill.csv'
tracker = 'out/tracker.txt'


def print_bold(string):
    print WHITE + string + END


def print_pass(string):
    print GREEN + string + END


def print_fail(string):
    print RED + string + END


def print_warn(string):
    print YELLOW + string + END


def print_bold_single_line(string):
    print WHITE + string + END,


def print_pass_single_line(string):
    print GREEN + string + END,


def print_fail_single_line(string):
    print RED + string + END,


def print_warn_single_line(string):
    print YELLOW + string + END,


def verified_coin(name):
    if type(Market().coin(name)) is not list:
        print_fail('{} : coin name non-existent or mispelled'.format(name))
        return False
    return True


def fetch_exchanges():  # NOT SURE IF THIS IS RIGHT
    try:
        a = []
        for e in open(exchanges).read().split('\n')[:-1]:
            a.append(e)
        return a
    except IOError:
        print_fail('failed to open exchanges')
        sys.exit(1)


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
