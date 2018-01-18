from statistics import *


# =============================================================================
# assist functions
# =============================================================================
def exists_on_my_exchange(name):
    return

# =============================================================================
# ultimate strategy
# =============================================================================


# =============================================================================
# actions
# =============================================================================
def sell(symbol, current_price):  # statistically calculated buy price
    return mean(symbol, current_price) - stddev(symbol)


def buy(symbol, current_price):  # statistically calculated buy price
    return mean(symbol, current_price) + stddev(symbol)
