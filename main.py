from Patterns import *
from StockHistory import *

if __name__ == "__main__":

    x = Ticker("AAPL")
    x.getHistory()
    print(x.data)
