from bs4 import BeautifulSoup
from generic import print_warn
from generic import tracker
import requests
import json

import os.path


soup = BeautifulSoup(requests.get('https://coinmarketcap.com').text, 'lxml')
symbols = soup.select('.circulating-supply a span.hidden-xs')
change = soup.find_all(class_='percent-change')

data = []
cycle = 0


def current_percents():
    percents = []
    for i in range(100):
        percents.append(float(change[i].text[:-1]))
    return sorted(percents, reverse=True) 


def movement(index):
    keys = []
    syms = []
    movs = []
    with open(tracker, 'r') as f:
        load = json.load(f)
        for i in range(99):
            key = data[i].keys()
            syms.append(data[i][key[0]][0])
            movs.append(data[i][key[0]][1])
            keys.append(float(key[0]))


def portfolio_matches():  # maybe belongs in a different file
    return


def track(empty):
    if empty:
        for i in range(100):
            data.append({percents[i]:[symbols[i].text, 0]})
    else:
        for i in range(100):
            data.append({percents[i]:[symbols[i].text,
                                      movement(percents[i])]})
    fout = open(tracker, 'w')
    #fout.write(str(cycle+1))
    fout.write(json.dumps(sorted(data, reverse=True)))
    fout.close()


def init():
    if os.path.isfile(tracker) and os.stat(tracker).st_size != 0:
        #cycle = int([x for x in open(tracker, 'r')][0][0])
        track(False)
    else:
        print_warn('no tracker data; initializing first cycle...')
        track(True)

init()
