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
        input = sys.argv[1].upper()
        if input in STOCKS:
            print(key(COMPANIES, input),STOCKS[input])
        else:
            print("Uknown company")
            
def key(comp, val):
    for key, value in comp.items():
        if val == value:
            return key

if __name__ == "__main__":
    stock_price()