from parser import scrape_historical_data
from parser import scrape_market_caps
from parser import scrape_exchanges


top = 100  # import this and set it from the backfill.py file / do I make it global?


# ------------------------------------------------------------------------------
# ASSIST FUNCTIONS
# ------------------------------------------------------------------------------
def extract_main_page_rows():
    """
    This function is called separately in the backfill.py file and
    effects the rest of the main page extract functions.
    """
    if top / 100 < 1:
        return scrape_market_caps()
    top = top / 100
    pages = top if int else int(top) + 1  # potential bug
    rows = []
    for page in range(0, pages):
        rows.append(scrape_market_caps(str(page + 1)))  # potential bug
    return rows  # turn 2D list into 1D


def column(category):  # remember to use string.lower()
    return 0  # match column from scrape to category, return correct index number


# ------------------------------------------------------------------------------
# EXTRACT MAIN PAGE DATA
# ------------------------------------------------------------------------------
def extract_main_page_header():
    return


def extract_main_page_number(coin):
    # THE NUMBER SHOULD COME WHATEVER THE COLUMN DICTIONARY RETURNS
    return extract_main_page_rows()[column('#')]


def extract_main_page_name(coin):
    return extract_main_page_rows()[column('name')]


def extract_main_page_market_cap(coin):
    return extract_main_page_rows()[column('market cap')]


def extract_main_page_price(coin):
    return extract_main_page_rows()[column('price')]


def extract_main_page_24h_volume(coin):
    return extract_main_page_rows()[column('volume (24h)')]


def extract_main_page_circulating_supply(coin):
    return extract_main_page_rows()[column('circulating supply')]


def extract_main_page_24h_change(coin):
    return extract_main_page_rows()[column('change (24h)')]


def extract_main_page_price_graph(coin):
    return extract_main_page_rows()[column('price graph (7d)')]


# ------------------------------------------------------------------------------
# EXTRACT HISTORICAL DATA
# ------------------------------------------------------------------------------
def extract_historical_header():
    return


def extract_historical_date(coin):
    return


def extract_historical_open(coin):
    return


def extract_historical_high(coin):
    return


def extract_historical_low(coin):
    return


def extract_historical_close(coin):
    return


def extract_historical_volume(coin):
    return


def extract_historical_market_cap(coin):
    return


# ------------------------------------------------------------------------------
# EXTRACT EXCHANGE DATA
# ------------------------------------------------------------------------------
def extract_exchange_header():
    return


def extract_exchange_number(coin):
    data = scrape_exchanges(coin)

    return


def extract_exchange_source(coin):
    return


def extract_exchange_pair(coin):
    return


def extract_exchange_volume_usd(coin):
    return


def extract_exchange_price(coin):
    return


def extract_exchange_volume_percent(coin):
    return


def extract_exchange_updated(coin):
    return
