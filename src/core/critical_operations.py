from aux.extract import extract_historical
from aux.generic import fetch_watchlist
from aux.generic import print_bold
from aux.generic import print_pass
from aux.generic import backfills

import csv


# backfilling
# -----------
def is_backfilled():  # checks to see if current data is up to date
    global date
    # get current date in format that csv is written to
    # pull most recent date from csv
    # if you can't pull format, it means no backfill data exist!
    # change missing value to something
    # match both strings (if same date, condition should be true)
    # return condition output (boolean)
    return True


def backfill():
    # SHOULD ONLY BACKFILL MISSING DATA TO CURRENT
    # DEAL WITH SCOPE LATER TOO
    if is_backfilled():
        return
    print_bold('backfilling data...')
    with open(backfills, 'a') as f:
        for coin in fetch_watchlist():
            f.write(coin)
            for extract in extract_historical(coin):
                for key in extract:
                    print extract[key][0] + ' ' + key
                print '--------'
            f.write('\n')
            print_pass('{:20} {}'.format(coin.upper(), ' backfill complete'))
        f.close()

# use time import to compare current date to data last scraped and then perform a function
# to only scrape data from the page that's necessary (up to that limit); otherwise, we'd
# be performing whole scrapes for nothing --> this can also be improved to be a daily
# crontab function that pre-fills the data for you


def backup():
    return
