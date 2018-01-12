from aux.generic import watchdata

import math
import csv


# =============================================================================
# ASSIST FUNCTIONS
# =============================================================================
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


# =============================================================================
# MAIN FUNCTIONS
# =============================================================================
def low(symbol):  # no price parameter b/c not part of for loop, so we use slower method
    prices = read_prices(symbol)
    low = prices[-1]  # last element in list -> V pythonic
    for price in prices:
        if low > price:
            low = price
    return low


def high(symbol):  # add an interval parameter, but accept daily low as default
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


def percent_change(data):
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


# =============================================================================
# RESULT FUNCTIONS
# =============================================================================
def sell(symbol, current_price):  # statistically calculated buy price
    return mean(symbol, current_price) - stddev(symbol)


def buy(symbol, current_price):  # statistically calculated buy price
    return mean(symbol, current_price) + stddev(symbol)
