import yfinance as yf


class Ticker():

    def __init__(self, ticker) -> None:
        
        self.ticker = ticker
        self.sym = yf.Ticker(self.ticker)
        self.period = 'max'
        self.interval = '1d'
        self.data = None
    
    def getHistory(self):

        self.data = self.sym.history(period = self.period, interval = self.interval, actions = False)
        self.data.sort_index(inplace = True)
        self.data.reset_index(inplace = True)

