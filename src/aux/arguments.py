from generic import print_fail

import argparse
import sys


def capture_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--percent-change',
                        help='find out percent change of coin',
                        nargs='+')
    parser.add_argument('-d', '--delay',
                        help='delay of http request; in seconds',
                        default=60,
                        type=long)
    parser.add_argument('-c', '--cycles',
                        help='total number of http requests',
                        default=100,
                        type=long)
    parser.add_argument('-r', '--remove',
                        help='remove cryptos from watchlist',
                        nargs='+')
    parser.add_argument('-a', '--add',
                        help='add cryptos to watchlist',
                        nargs='+')
    parser.add_argument('--low',
                        help='returns lowest price--use ticker symbol',
                        nargs='+')
    parser.add_argument('--high',
                        help='returns lowest price--use ticker symbol',
                        nargs='+')
    parser.add_argument('--exchange',
                        help='add exchange(s) that you trade on',
                        nargs='+')
    parser.add_argument('-w', '--wipe',
                        help='wipe watchlist.txt clean',
                        action='store_true')
    parser.add_argument('-e', '--erase',
                        help='wipe watchlist.csv clean',
                        action='store_true')
    parser.add_argument('--show-watchlist',
                        help='prints watchlist.txt contents',
                        action='store_true')
    parser.add_argument('--show-watchdata',
                        help='prints watchlist.csv contents',
                        action='store_true')
    parser.add_argument('--show-stddev',
                        help='shows asset\'s standard deviation',
                        nargs='+')
    parser.add_argument('--set-path',
                        help='sets the watchlists\' location path')
    parser.add_argument('--get-path',
                        help='sets the watchlists\' location path',
                        action='store_true')
    parser.add_argument('--run',
                        help='runs watch daemon',
                        action='store_true')
    return parser


def arguments():
    args = capture_args()
    if len(sys.argv) == 1:
        args.print_help()
        sys.exit()
    args = args.parse_args()
    if args.low:
        for arg in args.low:
            arg = arg.upper()
            if low(arg) < 0:
                print_fail(arg + ' : no pricing data to be read')
                continue
            print arg + ' : ' + str(low(arg))
    if args.high:
        for arg in args.high:
            arg = arg.upper()
            if high(arg) < 0:
                print_fail(arg + ' : no pricing data to be read')
                continue
            print arg + ' : ' + str(high(arg))
    if args.set_path:  # MAYBE USE A CONFIG FILE?
        set_path(args.set_path)  # FIGURE OUT WAY TO SET PATH SO THAT EVEN AFTER PROGRAM RUNS
    if args.get_path:
        print get_path()
    if args.show_watchlist:
        for name in open(watchlist, 'r'):
            print name,
    if args.show_watchdata:
        for data in open(watchdata, 'r'):
            print data,
    if args.show_stddev:
        for dev in args.show_stddev:
            if stddev(dev) != 0:
                print str(stddev(dev))
    if args.percent_change:
        percent_change(args.percent_change)
    if args.wipe:
        print_warn('wiping watchlist.txt contents')
        open(watchlist, 'w').close()
    if args.erase:
        print_warn('wiping watchlist.csv contents')
        open(watchdata, 'w').close()
    if args.remove:
        for arg in args.remove:
            remove_crypto(arg)
    if args.add:
        for arg in args.add:
            add_crypto(arg)
    return args
