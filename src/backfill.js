// ============================================================================
// GLOBAL VARIABLES
// ============================================================================

// ============================================================================
// FUNCTIONS
// ============================================================================
function fetch_watchlist() {
    coins = require("fs").readFileSync(".watchlist.txt", "utf-8").split("\n");
    coins.pop();
    return coins
}

function pull_data() {}

function backfill() {
    console.log("pulling historical data...");
    console.log(fetch_watchlist());
    var linkp1 = 'https://coinmarketcap.com/currencies/'
    var linkp2 = '/historical-data/?start=20130428&end=20180110'
    for(coin in fetch_watchlist()) {
        console.log("scraping coin : " + coin);
        var site = linkp1 + coin + linkp2;
        var webpage = require('webpage').create();
        var obj = webpage.open(site, function(status) {
            if(status !== "success") {
                console.log("site was not reached");
                return;
            }
            phantom.exit();
        });
        if(!obj) {
            console.log("object uninstantiated")
            return
        }
    }
}

// ============================================================================
// RUN
// ============================================================================
backfill()
