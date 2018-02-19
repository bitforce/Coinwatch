from generic import print_warn
from generic import print_fail
from generic import print_pass
from generic import tracker

from bs4 import BeautifulSoup

import requests
import json

import os.path


soup = BeautifulSoup(requests.get('https://coinmarketcap.com').text, 'lxml')
symbols = soup.select('.circulating-supply a span.hidden-xs')
percents = soup.find_all(class_='percent-change')

cycle = 0
load = []


def mov(i, sym, per):
    shift = 0
    for j in load:
        if sym == j.keys()[0]:
            shift = j[sym][1]
            if float(j[sym][0]) < float(per):
                shift += 1
                print_pass(sym + " " + str(shift) + " UP")
            if float(j[sym][0]) > float(per):
                print_fail(sym + " " + str(shift) + " DOWN")
                shift -= 1
            break
    return shift


def track(empty):
    data = []
    sym = ''
    num = 0
    if empty:
        for i in range(100):
            sym = symbols[i].text
            per = percents[i].text[:-1]
            data.append({sym:[per, 0]})
    else:
        for i in range(100):
            sym = symbols[i].text
            per = percents[iPOINTS ].text[:-1]
            data.append({sym:[per, mov(i, sym, per)]})
    order(data)
    fout = open(tracker, 'w')
    fout.write(json.dumps(data))
    fout.close()


def order():  # finds fastest growing coins-->invest in these
    return


def init():
    if os.path.isfile(tracker) and os.stat(tracker).st_size != 0:
        with open(tracker, 'r') as f:
            global load
            load = json.load(f)
            f.close()
        track(False)
    else:
        print_warn('no tracker data; initializing first cycle...')
        track(True)

# KEEP TRACK OF HOW MANY TIMES IT'S RAN OUTSIDE THE FILE

init()
