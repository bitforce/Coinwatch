from parser import scrape_historical_data
from parser import scrape_market_caps
from parser import scrape_exchanges


# ------------------------------------------------------------------------------
# ASSIST FUNCTIONS
# ------------------------------------------------------------------------------
def extract(rows, cols):
    data = []
    for i in range(0, len(cols)):
        r = []
        for j in range(0, len(rows)):
            r.append(rows[j][i])
        data.append({cols[i].lower(): r})
    return data


# ------------------------------------------------------------------------------
# MAIN FUNCTIONS
# ------------------------------------------------------------------------------
def extract_main(*top):
    cols = scrape_market_caps()[1]
    if not top or float(top) / 100 <= 1:
        rows = scrape_market_caps()[0]
    else:
        rows = []
        for page in range(0, top / 100 + 1):
            rows.append(scrape_market_caps(str(page + 1))[0])
    rows = strip([r for row in rows for r in row])
    # UNFINISHED
    return


def extract_historical(coin):
    rows = scrape_historical_data(coin)[0]
    cols = scrape_historical_data(coin)[1]
    return extract(rows, cols)


def extract_exchanges(coin):
    rows = scrape_exchanges(coin)[0]
    cols = scrape_exchanges(coin)[1]
    return extract(rows, cols)
