from parser import scrape_historical_data
from parser import scrape_market_caps
from parser import scrape_exchanges


# ------------------------------------------------------------------------------
# ASSIST FUNCTIONS
# ------------------------------------------------------------------------------
def extract(rows, col):
    data = []
    for i in range(0, len(cols)):
        r = []
        for j in range(0, len(rows)):
            r.append(rows[j][i])
        print r
        data.append({cols[i].lower(): r})
    return data


# ------------------------------------------------------------------------------
# MAIN FUNCTIONS
# ------------------------------------------------------------------------------
def extract_main(top):
    cols = scrape_market_caps()[1]
    if top / 100 <= 1:
        rows = scrape_market_caps()[0]
    else:
        top = top / 100
        pages = top if int else int(top) + 1  # potential bug
        rows = []
        for page in range(0, pages):
            rows.append(scrape_market_caps(str(page + 1)))  # potential bug
    return


def extract_historical(coin, scope):
    rows = scrape_historical_data(coin, scope)[0]
    cols = scrape_historical_data(coin, scope)[1]
    return extract(rows, cols)


def extract_exchanges(coin):
    rows = scrape_exchanges(coin)[0]
    cols = scrape_exchanges(coin)[1]
    return extract(rows, cols)
