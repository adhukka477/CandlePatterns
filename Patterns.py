from metrics import *
from stock_history import Ticker

class Patterns(Ticker):

    def __init__(self, ticker) -> None:
        Ticker.__init__(self, ticker)
        self.getHistory()        
        self.calculator = Metrics()

    def flagType(self):
        self.data["Type"] = [1 if self.data.loc[i, "Close"] >= self.data.loc[i, "Open"] else 0 for i in range(len(self.data))]
    
    def longFlag(self, x = 20, alpha = 2):
        #   Calculate ATR(x)
        atr = self.calculator.calculateATR(self.data, x)
        self.data["LongFlag"] = [1 if abs(self.data.loc[i, "Close"]-self.data.loc[i, "Open"]) >= alpha*atr[i] else 0 for i in range(len(self.data))]

    def shortFlag(self, x = 20, alpha = 0.5):
        #   Calculate ATR(x)
        atr = self.calculator.calculateATR(self.data, x)
        self.data["ShortFlag"] = [1 if abs(self.data.loc[i, "Close"]-self.data.loc[i, "Open"]) <= alpha*atr[i] else 0 for i in range(len(self.data))]

    def marubozuFlag(self):
        pass

    def closingMarubozuFlag(self):
        pass

    def openingMarubozuFlag(self):
        pass

    def spinningTopFlag(self):
        pass

    def dojiFlag(self):
        pass

    def longLeggedDojiFlag(self):
        pass

    def crossDojiFlag(self):
        pass

    def dragonflyDojiFlag(self):
        pass

    def hammerFlag(self):
        pass

    def shootingStarFlag(self):
        pass

    def engulfingFlag(self):
        pass

    def piercingFlag(self):
        pass

    def haramiFlag(self):
        pass

    def kickerFlag(self):
        pass

    def morningStarFlag(self):
        pass

    def abandonedBabyFlag(self):
        pass

    def triStarFlag(self):
        pass

    def threeWhiteSoldiersFlag(self):
        pass

    def twoCrowsFlag(self):
        pass

    def threeInsideFlag(self):
        pass

    def threeOutsideFlag(self):
        pass

    def meetingLineFlag(self):
        pass

    def stickSandwhichFlag(self):
        pass

    def matchingFlag(self):
        pass
    
    def tweezerFlag(self):
        pass

    def breakawayFlag(self):
        pass

    def tasukiFlag(self):
        pass

    def threeMethodFlag(self):
        pass

    def seperatingLinesFlag(self):
        pass

    def sideBySideFlag(self):
        pass


