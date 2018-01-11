# Coinwatch

Overview
---
A cryptocurrency trend tracker that uses statistics to illuminate price-action 
trends via statistical analysis and trade monitoring.

Setup
---
```
git clone https://github.com/bitforce/Coinwatch
cd Coinwatch/
./install
```

Usage
---
see `./script.py --help`

Note
---
This program will create the watchlists in the current directory (wherever you run it), unless 
specified by the `--set-path` option. If you're not sure where the data is being read/written, 
use the `--get-path` option to find out. You can also search this in the configuration file: 
_.coinwatch.conf_; located in the home directory.

All data that you get through the program is relative; while there exist advantages with this 
form of tracking, a major complication is relative asset value, as for example, say the all-
time high for a currency you are monitoring may not be the actual coin's ATH, as perhaps you 
may have only a certain amount of historical data and it doesn't go back far enough to 
measure this.

When using the --high/low, enter the coin's ticker symbol, not the name


TODO
---
- create a _.coinwatch.conf_ file if it doesn't exist and be able to set permanent configs
 via commands like this: ./script.py -c 10000 -d 45 --preset
- the program should attempt to read from the config file first if preset commands aren't 
 in place
- create time intervals for mean() and stddev() calculator: make it so that you can put 
 any time period in place (10m, 1h, 3d , 2w, 1M, 5Y) <- 1m is finest granularity, and 
- use low market caps for high volatility gains, something with a $B+ market cap will 
 only move up slowly compared to others
- find way perform a --backup
- let's do normal run is relative mean/avg of accrued pricing data since scrape, and the
 --last option says how much price/percent went up since last look/scrape
- create hidden watchdir containing watchlist, watchdata, and history > how to create dir in py
 
use beautiful soup and scrape coinmarketcap for data, you'll need to dynamically
change the preset, but the normal for
https://coinmarketcap.com/currencies/COINNAME/historical-data/
is 30 days

if you get all-time data, you can then use it to find out ICO date and choose
any interval you want

you can even create loading bar by finding out how many elements are on the page and
then counting them as you scrape

import all the data you are trying to backfill into backfill.csv since watchdata.csv is
a relevant historical tracker

License
---
Licensed under the WTFPL - see [LICENSE](./doc/LICENSE) for explicit details.

Version
---
1.0.0

Author
---
[LinkedIn](https://www.linkedin.com/in/brandonjohnsonxyz/)
[Personal](https://brandonjohnson.life)
[GitHub](https://github.com/bitforce)
