from bs4 import BeautifulSoup

from generic import fetch_watchlist
from generic import print_pass

import requests


def pull_historical():  # maybe add a loader to let user know how long this would take
    # actually, this process should be automatic, where the interval is just the missing
    # amount of time that data has been filled for on the current currencies
    linkp1 = 'https://coinmarketcap.com/currencies/'
    linkp2 = '/historical-data/?start=20130428&end=20180110'
    data = []  # list of dictionaries
    for coin in fetch_watchlist():  # add interval property and scheduler param
        url = linkp1 + coin + linkp2
        soup = BeautifulSoup(requests.get(url).text, 'lxml')
        columns = soup.find("thead").find('tr').find_all('th')  # used to match row[][]
        col_data = []
        for column in columns:
            col_data.append(str(column.text))
        rows = soup.find("tbody").find_all('tr')
        row_data = []
        for row in rows:
            r_data = []
            for r in row.find_all('td'):
                r_data.append(str(r.text))
            row_data.append(r_data)
        data.append({coin: row_data})  # a list of dicionaries  {crypto: list}
        # append col_data so we know how to match
        print_pass('{:20} {}'.format(coin.upper(), ' backfill complete'))
    print
    return data


def pull_market_caps(top):  # gather top N currencies
    # if the user enters 50, get top 100 and only return 50
    # if user enters 200, get top 200 currencies and return them
    print


def pull_markets(coin):
    print
