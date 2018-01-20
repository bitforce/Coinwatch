from scraper import scrape_historical_data
from scraper import scrape_all_exchanges
from scraper import scrape_market_caps
from scraper import scrape_exchanges


# =============================================================================
# assist functions
# =============================================================================
def extract(rows, cols):
    data = []
    for i in range(0, len(cols)):
        r = []
        for j in range(0, len(rows)):
            r.append(rows[j][i])
        data.append({cols[i].lower(): r})
    return data


# =============================================================================
# main functions
# =============================================================================
def extract_main_page(*top):
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


def extract_all_exchanges():
    exchanges = []
    for row in scrape_all_exchanges():
        if row.has_attr('id'):
            exchanges.append(row.text.strip().split('.')[1][1:].lower())
    return exchanges
