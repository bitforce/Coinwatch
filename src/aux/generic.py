YELLOW = '\033[93m'
GREEN = '\033[92m'
WHITE = '\033[1m'
RED = '\033[91m'
END = '\033[0m'

backfill = '.watch/backfill.csv'
exchanges = '.watch/exchanges.txt'
watchlist = '.watch/watchlist.txt'
watchdata = '.watch/watchlist.csv'


def print_warn(string):
    print YELLOW + string + END


def print_bold(string):
    print WHITE + string + END


def print_pass(string):
    print GREEN + string + END


def print_fail(string):
    print RED + string + END


def fetch_watchlist():
    try:
        a = []
        for e in open(watchlist).read().split('\n')[:-1]:
            a.append(e.split()[:-1][0])  # becomes a list when you split it, so you take [0]
        return a
    except IOError:
        print_fail('failed to open watchlist')
        sys.exit(1)
