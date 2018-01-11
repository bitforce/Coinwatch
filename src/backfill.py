from helper import fetch_watchlist
from helper import print_pass

from bs4 import BeautifulSoup

import requests


def timelapse():  # verifies whether there exists missing data due to time lapsed
    print


def pull_data():  # maybe add a loader to let user know how long this would take
    # actually, this process should be automatic, where the interval is just the missing
    # amount of time that data has been filled for on the current currencies
    linkp1 = 'https://coinmarketcap.com/currencies/'
    linkp2 = '/historical-data/?start=20130428&end=20180110'
    data = []
    for coin in fetch_watchlist():  # add interval property and scheduler param
        url = linkp1 + coin + linkp2
        soup = BeautifulSoup(requests.get(url).text, 'lxml')
        columns = soup.find("thead").find('tr').find_all('th')
        rows = soup.find("tbody").find_all('tr')
        grid_data = []
        for column in columns:
            row_data = []
            for row in rows:
                row_data.append(str(row.text))
            grid_data.append({str(column.text): row_data})
        data.append(grid_data)
        print_pass(coin.upper() + ' backfill complete')
    return data


def export_data(data):
    data = pull_data()
    if not data:
        print_fail('no data available to export')
    with open(watchhist) as f:
        f.write(data)  # think on how you would like to organize this


def backfill():
    print_bold('backfilling data...')
    export_data()

# use time import to compare current date to data last scraped and then perform a function
# to only scrape data from the page that's necessary (up to that limit); otherwise, we'd
# be performing whole scrapes for nothing --> this can also be improved to be a daily
# crontab function that pre-fills the data for you
