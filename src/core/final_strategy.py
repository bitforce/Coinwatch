from coinwrap import Market

from core.strats.arbitrage import *
from core.strats.monitor import *
from core.strats.trailer import *
from core.strats.stats.standard_deviation import *
from core.strats.stats.mean import *
from core.strats.nlp import *
from core.commandline_operations import get_simple_percent_changes
from aux.generic import fetch_exchanges
from aux.generic import fetch_watchlist
from aux.generic import print_pass_single_line
from aux.generic import print_fail_single_line
from aux.generic import print_bold
from aux.generic import YELLOW
from aux.generic import GREEN
from aux.generic import RED
from aux.generic import END
from aux.generic import watchdata

import datetime
import csv


# =============================================================================
# assist functions
# =============================================================================
def exchanges_match(name):
    tradable = []
    my_exchanges = fetch_exchanges()
    for exchange in extract_exchanges(name):
        if exchange in my_exchanges:
            tradable.append(exchange)


def hue(percent):
    if float(percent) > 0:
        return GREEN + str(percent) + '%' + END
    if float(percent) < 0:
        return RED + str(percent) + '%' + END
    return YELLOW + str(percent) + '%' + END


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
        price = float(Market().coin(crypto)[0]['price_usd'])
        symbol = str(Market().coin(crypto)[0]['symbol'])
        csv.writer(f).writerow([date, price, symbol])
        print_symbol = '{:8}'.format(symbol)
        if price > 10:
            print_price = '{:>4}'.format('$') + '{:<10.2f}'.format(price)
        else:
            print_price = '{:>4}'.format('$') + '{:<10.3f}'.format(price)
        hour = hue(get_simple_percent_changes(crypto)[0])
        day = hue(get_simple_percent_changes(crypto)[1])
        week = hue(get_simple_percent_changes(crypto)[2])
        percents = '|    {:18} {:18} {}'.format(hour, day, week)
        if price < sell(symbol, price):
            print_fail_single_line(print_symbol + print_price)
            print percents
        elif price > buy(symbol, price):
            print_pass_single_line(print_symbol + print_price)
            print percents
        else:
            print print_symbol + print_price,
            print percents
    f.write('\n')
    f.close()

    # maybe this can be optimized so you don't have to open the file every update
    # also perhaps add how much price has changed in last hour
