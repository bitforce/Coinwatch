from generic import print_warn
from generic import tracker

from bs4 import BeautifulSoup

import requests
import json

import os.path


soup = BeautifulSoup(requests.get('https://coinmarketcap.com').text, 'lxml')
symbols = soup.select('.circulating-supply a span.hidden-xs')
change = soup.find_all(class_='percent-change')

cycle = 0
load = []


def mov(i, sym):
    # here what we want to get is the past keys using the old vals[0], 
    # so by finding the symbol, we know what the past % was -- we get 
    # the current % by passing through the data
    print load[i].items()[0][1][0]

    shift = int(load[i][load[i].keys()[0]][1])
    #print str(shift) + " " + load[i][load[i].keys()[0]][0]
    if float(load[i].keys()[0]) < percent:
        shift += 1
    if float(load[i].keys()[0]) > percent:
        shift -= 1
    return shift


def track(empty):
    data = []
    sym = ''
    if empty:
        for i in range(100):
            sym = symbols[i].text
            data.append({float(change[i].text[:-1]):sym, sym:0})
    else:
        for i in range(100):
            sym = symbols[i].text
            data.append({float(change[i].text[:-1]):sym, sym:mov(i, sym)]})
    fout = open(tracker, 'w')
    #fout.write(str(cycle+1))
    fout.write(json.dumps(sorted(data, reverse=True)))
    fout.close()


def init():
    if os.path.isfile(tracker) and os.stat(tracker).st_size != 0:
        #cycle = int([x for x in open(tracker, 'r')][0][0])
        with open(tracker, 'r') as f:
            global load
            load = json.load(f)
            f.close()
        track(False)
    else:
        print_warn('no tracker data; initializing first cycle...')
        track(True)

# what I essentially want to see are a list of symbols highlighted 
# green, red, or default indicating that the trailing is working, 
# perhaps, what I'll do is just place a + or - sign next to my 
# portfolio coins when their ROC is significantly moving in 
# some direction
init()
