from bs4 import BeautifulSoup

from generic import fetch_watchlist
from generic import print_pass

import datetime
import requests


link = 'https://coinmarketcap.com'


# ------------------------------------------------------------------------------
# assist functions
# ------------------------------------------------------------------------------
def scrape_cols(soup):
    cols = []
    for column in soup.find("thead").find('tr').find_all('th'):
        cols.append(str(column.text))
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


def today():
    now = datetime.datetime.now()
    month = str(now.month)
    if len(month) == 1:
        month = '0' + month
    return str(now.year) + month + str(now.day)


# ------------------------------------------------------------------------------
# main functions
# ------------------------------------------------------------------------------
def scrape_all_exchanges():
    url = link + '/exchanges/volume/24-hour/all/'
    soup = BeautifulSoup(requests.get(url).text, 'lxml')
    return soup.find('table', class_='table').find_all('tr')


def scrape_exchanges(coin):
    url = link + '/' + coin + '/#markets'
    rows = scrape_rows(BeautifulSoup(requests.get(url).text, 'lxml'))
    cols = scrape_cols(BeautifulSoup(requests.get(url).text, 'lxml'))
    return [rows, cols]


def scrape_market_caps(*args):
    if len(args) == 0:
        rows = scrape_rows(BeautifulSoup(requests.get(url).text, 'lxml'))
        cols = scrape_cols(BeautifulSoup(requests.get(url).text, 'lxml'))
        return [rows, cols]
    rows = scrape_rows(BeautifulSoup(requests.get(url + args[0]).text, 'lxml'))
    cols = scrape_cols(BeautifulSoup(requests.get(url + args[0]).text, 'lxml'))
    return [rows, cols]


def scrape_historical_data(coin):
    url = link + '/currencies/' + coin + '/historical-data/?start=20130428&end=' + today()
    rows = scrape_rows(BeautifulSoup(requests.get(url).text, 'lxml'))
    cols = scrape_cols(BeautifulSoup(requests.get(url).text, 'lxml'))
    return [rows, cols]
