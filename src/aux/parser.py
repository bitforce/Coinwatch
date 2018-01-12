"""
Consists of methods for accessing, extracting, and formatting coinmarketcap data.
"""
from bs4 import BeautifulSoup

from generic import fetch_watchlist
from generic import print_pass

import requests


url = 'https://coinmarketcap.com/'


def extract_cols(soup):  # doesn't appear immediately useful, but who knows
    """
    Extracts column headers from table.

    @param soup: BeautifulSoup object with specific url
    @return: a string-type list consisting of the colum categories
    """
    cols = []
    for column in soup.find("thead").find('tr').find_all('th'):
        col.append(str(column.text))
    return cols


def extract_rows(soup):
    """
    Extracts rows data from table.

    @param soup: BeautifulSoup object with specific url
    @return: a list of type-string lists consisting of row data
    """
    rows = []
    for row in soup.find('tbody').find_all('tr'):
        r = []
        for data in row.find_all('td'):
            r.append(str(data.text))
        rows.append(r)
    return rows
    # just note that there are nested 'td's for /#markets, but you can probs
    # still get the text as done above


def scrape_markets(coin):
    url = url + coin + '/#markets'
    return extract_rows(BeautifulSoup(requests.get(url).text, 'lxml'))


def scrape_market_caps():  # returns rows scraped from top X coins url
    return extract_rows(BeautifulSoup(requests.get(url).text, 'lxml'))


def scrape_market_caps(page):  # returns rows scraped from top X coins url
    return extract_rows(BeautifulSoup(requests.get(url + page).text, 'lxml'))


def scrape_historical_data(coin):
    linkp1 = url + 'currencies/'
    linkp2 = '/historical-data/?start=20130428&end=20180110'
    data = []
    for coin in fetch_watchlist():
        url = linkp1 + coin + linkp2
        soup = BeautifulSoup(requests.get(url).text, 'lxml')
        data.append({coin: extract_rows(soup)})
        print_pass('{:20} {}'.format(coin.upper(), ' backfill complete'))
    print
    return data


def pull_market_caps(top):  # extracts ....?
    if top / 100 < 1:
        return scrape_market_caps()
    top = top / 100
    pages = top if int else int(top) + 1
    rows = []
    for page in pages:
        rows.append(scrape_market_caps(str(page)))
    return rows


def pull_historical_data(coin):
    print


def pull_markets(coin):
    print
