from aux.generic import read_prices


def simple_mean(symbol, current_price):
    mean = current_price
    prices = read_prices(symbol)
    if len(prices) > 1:
        mean = sum(prices) / len(prices)
    return mean
