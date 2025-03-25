import sys

def stock_price():
    COMPANIES = {
    'Apple': 'AAPL',
    'Microsoft': 'MSFT',
    'Netflix': 'NFLX',
    'Tesla': 'TSLA',
    'Nokia': 'NOK'
    }

    STOCKS = {
    'AAPL': 287.73,
    'MSFT': 173.79,
    'NFLX': 416.90,
    'TSLA': 724.88,
    'NOK': 3.37
    }

    if len(sys.argv) == 2:
        input = sys.argv[1].capitalize()
        if input in COMPANIES:
            print(STOCKS[COMPANIES[input]])
        else:
            print("Uknown company")

if __name__ == "__main__":
    stock_price()