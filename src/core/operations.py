from aux.tracker import *


# =============================================================================
# assist functions
# =============================================================================


# =============================================================================
# main functions
# =============================================================================

# commandline
# ----------------------------------------
def add(crypto):
    if type(m.coin(crypto)) is not list:
        print_bold('{} : coin crypto non-existent or mispelled'.format(crypto))
        return
    f = open(watchlist, 'a')
    if crypto not in open(watchlist).read():
        f.write(str(crypto + ' (' + m.coin(crypto)[0]['symbol'] + ')\n'))
    else:
        print_warn(crypto + ' is already being tracked')
    f.close()


def remove(crypto):
    coins = fetch_watchlist()
    for coin in coins:
        if coin == crypto:
            coins.remove(coin)
    f = open(watchlist, 'w')
    for coin in coins:
        f.write(str(coin + ' (' + m.coin(coin)[0]['symbol'] + ')\n'))
    f.close()


def include(exchanges):
    return


# data storage
# ----------------------------------------
def backfill():
    return


# configuration manipulation
# ----------------------------------------
def get_path():
    return path


def set_path(newpath):
    global path
    path = ''
    # get os type and then appropriate use '$HOME' or '$home', etc...


# numeric return type
# ----------------------------------------
def get_low(crypto):
    return


def get_high(crypto):
    return


def get_standard_deviation(crypto):
    return


def get_percent_change(crypto, interval):
    return
