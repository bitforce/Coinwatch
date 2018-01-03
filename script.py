#!/usr/bin/python2

from coinwrap import Market
import argparse
import time
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
cycles = 0
delay = 0
m = Market()

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

# =============================================================================
# MAIN FUNCTIONS
# =============================================================================

def validate():
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
            help='wipe watchlist clean',
            default=False,
            const=True,
            nargs='?',
            type=bool)
    parser.add_argument('-s', '--show',
            help='prints watchlist contents',
            default=False,
            const=True,
            nargs='?',
            type=bool)
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)
    args = parser.parse_args()
    if args.show:
        for name in open(watchlist, 'r'):
            print name, 
    if args.wipe:
        print_warn('wiping watchlist contents')
        open(watchlist, 'w').close()
    if args.remove is not None:
        for arg in args.remove:
            remove_crypto(arg)
    if args.add is not None:
        for arg in args.add:
            add_crypto(arg)
    global cycles
    global delay
    cycles = args.delay
    delay = args.delay


def update():
    for crypto in fetch_watchlist():
        price = m.coin(crypto)[0]['price_usd']
        symbol = m.coin(crypto)[0]['symbol']
        print symbol + ' ' + price # add a highlight conditional
        time.sleep(delay)


def fetch_watchlist():
    try:
        return open(watchlist, 'r').read().split('\n')[:-1]
    except IOError:
       print_fail('failed to open watchlist')


def remove_crypto(name): # *** I know it's not most efficient, but it works
    coins = open(watchlist).read().split('\n')[:-1]
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
    # FIX GLOBAL-LOCAL SCOPE ISSUE
    print cycles
    print delay
    if not os.path.isfile(watchlist):
        print_bold('no watchlist found; creating one now')
        open(watchlist, 'w').close()
    sys.exit(1)
    while cycles > 0:
        cycles -= 1
        update()

# =============================================================================
# RUN
# =============================================================================
run()
