from aux.generic import watchdata
from aux.generic import read_prices

import math
import csv


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


def standard_deviation(symbol):
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
