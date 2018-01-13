from aux.generic import fetch_watchlist
from aux.generic import print_bold
from aux.generic import print_pass
from aux.generic import watchhist
from aux.extract import *

import csv


def backfill(scope):
    # SHOULD ONLY BACKFILL MISSING DATA TO CURRENT
    print_bold('backfilling data...')
    backfill = []
    for coin in fetch_watchlist():
        backfill.append({coin: extract_historical(coin, scope)})
    # write backfill to csv
    return


def backfilled():  # checks to see if current data is up to date
    # get current date in format that csv is written to
    # pull most recent date from csv
    # if you can't pull format, it means no backfill data exist!
    current = False
    # match both strings (if same date, condition should be true)
    # return condition output (boolean)
    return current

# use time import to compare current date to data last scraped and then perform a function
# to only scrape data from the page that's necessary (up to that limit); otherwise, we'd
# be performing whole scrapes for nothing --> this can also be improved to be a daily
# crontab function that pre-fills the data for you


def extract_historical_data_rows(coin):  # DELETE ME LATER
    data = []
    # this goes in backfill.py
    for coin in fetch_watchlist():
        url = linkp1 + coin + linkp2
        soup = BeautifulSoup(requests.get(url).text, 'lxml')
        data.append({coin: scrape_rows(soup)})
        print_pass('{:20} {}'.format(coin.upper(), ' backfill complete'))
    print
    return data
