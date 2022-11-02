from metrics import *
from stock_history import Ticker
import numpy as np

class Patterns(Ticker):

    def __init__(self, ticker) -> None:
        Ticker.__init__(self, ticker)
        self.getHistory()        
        self.calculator = Metrics()

    def flagType(self):
        self.data["Type"] = [1 if self.data.loc[i, "Close"] >= self.data.loc[i, "Open"] else 0 for i in range(len(self.data))]
    
    def longFlag(self, n = 20, alpha = 2):
        #   Calculate ATR(x)
        atr = self.calculator.calculateATR(self.data, n)
        self.data["LongFlag"] = [1 if abs(self.data.loc[i, "Close"]-self.data.loc[i, "Open"]) >= alpha*atr[i] else 0 for i in range(len(self.data))]

    def shortFlag(self, n = 20, alpha = 0.5):
        #   Calculate ATR(x)
        atr = self.calculator.calculateATR(self.data, n)
        self.data["ShortFlag"] = [1 if abs(self.data.loc[i, "Close"]-self.data.loc[i, "Open"]) <= alpha*atr[i] else 0 for i in range(len(self.data))]

    def marubozuFlag(self, alpha = 2, n = 20):
        atr = self.calculator.calculateATR(self.data, n)
        long = [True if abs(self.data.loc[i, "Close"]-self.data.loc[i, "Open"]) >= alpha*atr[i] else False for i in range(len(self.data))]
        max_body = [self.data.loc[i, "Open"] if self.data.loc[i, "Open"] >= self.data.loc[i, "Close"] else self.data.loc[i, "Close"] for i in range(len(self.data))]
        min_body = [self.data.loc[i, "Open"] if self.data.loc[i, "Open"] <= self.data.loc[i, "Close"] else self.data.loc[i, "Close"] for i in range(len(self.data))]        
        upper_shadow = [max_body[i]/self.data.loc[i, "High"] for i in range(len(self.data))]
        lower_shadow = [min_body[i]/self.data.loc[i, "Low"]  for i in range(len(self.data))]
        no_upper_shadow = [True if x >= 0.95 else False for x in upper_shadow]
        no_lower_shadow = [True if x <= 1.05 else False for x in lower_shadow]
        self.data["MarubozuFlag"] = [1 if no_upper_shadow[i] and no_lower_shadow[i] and long[i] else 0 for i in range(len(self.data))]


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


