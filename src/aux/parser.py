from bs4 import BeautifulSoup

from generic import fetch_watchlist
from generic import print_pass

import requests


url = 'https://coinmarketcap.com/'


def scrape_cols(soup):  # UNUSED?
    cols = []
    for column in soup.find("thead").find('tr').find_all('th'):
        col.append(str(column.text))
    return cols


def scrape_rows(soup):
    rows = []
    for row in soup.find('tbody').find_all('tr'):
        r = []
        for data in row.find_all('td'):
            r.append(str(data.text))
        rows.append(r)
    return rows
    # just note that there are nested 'td's for /#markets, but you can probs
    # still get the text as done above


# SO WE ARE CLEAR, THERE ARE ONLY 3 MAIN THINGS TO SCRAPE MAIN PAGE, #MARKETS, AND HISTORICAL
def scrape_exchanges(coin):
    url = url + coin + '/#markets'
    return scrape_rows(BeautifulSoup(requests.get(url).text, 'lxml'))


def scrape_market_caps():
    return scrape_rows(BeautifulSoup(requests.get(url).text, 'lxml'))


def scrape_market_caps(page):
    return scrape_rows(BeautifulSoup(requests.get(url + page).text, 'lxml'))


def scrape_historical_data(coin, scope):
    if scope is '':
        scope = 'start=20130428&end=20180112'
    url = url + 'currencies/' + coin + '/historical-data/?' + scope
    return scrape_rows(BeautifulSoup(requests.get(url).text, 'lxml'))
