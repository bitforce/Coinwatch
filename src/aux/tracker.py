from generic import print_warn
from generic import print_fail
from generic import print_pass
from generic import tracker

from bs4 import BeautifulSoup

import requests
import json
import time

import os.path


soup = BeautifulSoup(requests.get('https://coinmarketcap.com').text, 'lxml')
symbols = soup.select('.circulating-supply a span.hidden-xs')
percents = soup.find_all(class_='percent-change')

cycle = 0
load = []
ordered = []


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


def order(data):
    return data


def munge(empty):
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
            per = percents[i].text[:-1]
            data.append({sym:[per, mov(i, sym, per)]})
    fout = open(tracker, 'w')
    fout.write(json.dumps(order(data)))
    fout.close()


def track():
    if os.path.isfile(tracker) and os.stat(tracker).st_size != 0:
        i = 1
        while(i < 1000):
            print 'tracker cycle ' + str(i)
            with open(tracker, 'r') as f:
                global load
                load = json.load(f)
                f.close()
            munge(False)
            time.sleep(360)
            i += 1
    else:
        print_warn('no tracker data; initializing first cycle...')
        munge(True)
