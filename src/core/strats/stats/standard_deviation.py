from core.strats.stats.mean import simple_mean
from aux.generic import watchdata

import math
import csv


def simple_standard_deviation(symbol):
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
        sq += math.pow(price - simple_mean(symbol, price), 2)
    return math.sqrt(sq / len(prices))
