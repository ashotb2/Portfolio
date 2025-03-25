import sys

def stock():
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
        input_list = sys.argv[1].split(',')
        for i in input_list:
            i = i.strip()
            if check(input_list) is True:
                if i.capitalize() in COMPANIES:
                    print(i.capitalize(),'stock price is',STOCKS[COMPANIES[i.capitalize()]])
                elif i.upper() in STOCKS:
                    print(i.upper(),'is a ticker symbol for',key(COMPANIES, i.upper()))
                else:
                    print(i,'is an unknown company or an unknown ticker symbol')

def check(inp):
    flag=True
    for i in inp:
        i = i.strip()
        if i=='':
            flag=False
    return flag

def key(comp, val):
    for key, value in comp.items():
        if val == value:
            return key

if __name__ == '__main__':
    stock()