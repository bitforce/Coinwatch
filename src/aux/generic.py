import os.path


YELLOW = '\033[93m'
GREEN = '\033[92m'
WHITE = '\033[1m'
RED = '\033[91m'
END = '\033[0m'

backfills = '.watch/backfill.csv'
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


def file_exists(f, msg):
    if not os.path.isfile(f):
        print_bold(msg)
        open(f, 'w').close()


def dir_exists(d, msg):
    if not os.path.isdir(d):
        print_bold(msg)
        os.makedirs(d)


def show(*options):
    if len(options) == 2 and options[0] == 'low':
        for arg in options[1]:
            arg = arg.upper()
            if low(arg) < 0:
                print_fail(arg + ' : no pricing data to be read')
                continue
            print arg + ' : ' + str(low(arg))
    elif len(options) == 2 and options[0] == 'high':
        for arg in args.high:
            arg = arg.upper()
            if high(arg) < 0:
                print_fail(arg + ' : no pricing data to be read')
                continue
            print arg + ' : ' + str(high(arg))
    elif len(options) == 2 and options[0] == 'delta':
        for dev in args.show_stddev:
            if stddev(dev) != 0:
                print str(get_standard_deviation(dev))
    else:
        for item in open(options[0]):
            print item,
