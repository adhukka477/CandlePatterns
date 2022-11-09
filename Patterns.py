from metrics import *
from stock_history import Ticker
import numpy as np

class Patterns(Ticker):

    def __init__(self, ticker) -> None:
        Ticker.__init__(self, ticker)
        self.getHistory()        
        self.calculator = Metrics()

    def flagType(self):
        self.data["Type"] = [1 if self.data.loc[i, "Close"] >= self.data.loc[i, "Open"] else -1 for i in range(len(self.data))]
    
    def longFlag(self, n = 20, alpha = 2):
        #   Calculate ATR(x)
        atr = self.calculator.calculateATR(self.data, n)
        self.data["LongFlag"] = [1 if abs(self.data.loc[i, "Close"]-self.data.loc[i, "Open"]) >= alpha*atr[i] else 0 for i in range(len(self.data))]

    def shortFlag(self, n = 20, alpha = 0.5):
        #   Calculate ATR(x)
        atr = self.calculator.calculateATR(self.data, n)
        self.data["ShortFlag"] = [1 if abs(self.data.loc[i, "Close"]-self.data.loc[i, "Open"]) <= alpha*atr[i] else 0 for i in range(len(self.data))]

    def bullishMarubozuFlag(self, alpha = 1.5, n = 20):
        flag_type = [True if self.data.loc[i, "Close"] >= self.data.loc[i, "Open"] else False for i in range(len(self.data))]
        atr = self.calculator.calculateATR(self.data, n)
        long = [True if abs(self.data.loc[i, "Close"]-self.data.loc[i, "Open"]) >= alpha*atr[i] else False for i in range(len(self.data))]
        max_body = [self.data.loc[i, "Open"] if self.data.loc[i, "Open"] >= self.data.loc[i, "Close"] else self.data.loc[i, "Close"] for i in range(len(self.data))]
        min_body = [self.data.loc[i, "Open"] if self.data.loc[i, "Open"] <= self.data.loc[i, "Close"] else self.data.loc[i, "Close"] for i in range(len(self.data))]        
        upper_shadow = [max_body[i]/self.data.loc[i, "High"] for i in range(len(self.data))]
        lower_shadow = [min_body[i]/self.data.loc[i, "Low"]  for i in range(len(self.data))]
        no_upper_shadow = [True if x >= 0.98 else False for x in upper_shadow]
        no_lower_shadow = [True if x <= 1.02 else False for x in lower_shadow]

        for i in range(len(self.data)):
            if long[i] and no_upper_shadow[i] and flag_type[i] and no_lower_shadow[i]:
                self.data.loc[i, "BullishMarubozuFlag"] = 1
            else:
                self.data.loc[i, "BullishMarubozuFlag"] = 0

    def bearishMarubozuFlag(self, alpha = 1.5, n = 20):
        flag_type = [True if self.data.loc[i, "Close"] >= self.data.loc[i, "Open"] else False for i in range(len(self.data))]
        atr = self.calculator.calculateATR(self.data, n)
        long = [True if abs(self.data.loc[i, "Close"]-self.data.loc[i, "Open"]) >= alpha*atr[i] else False for i in range(len(self.data))]
        max_body = [self.data.loc[i, "Open"] if self.data.loc[i, "Open"] >= self.data.loc[i, "Close"] else self.data.loc[i, "Close"] for i in range(len(self.data))]
        min_body = [self.data.loc[i, "Open"] if self.data.loc[i, "Open"] <= self.data.loc[i, "Close"] else self.data.loc[i, "Close"] for i in range(len(self.data))]        
        upper_shadow = [max_body[i]/self.data.loc[i, "High"] for i in range(len(self.data))]
        lower_shadow = [min_body[i]/self.data.loc[i, "Low"]  for i in range(len(self.data))]
        no_upper_shadow = [True if x >= 0.98 else False for x in upper_shadow]
        no_lower_shadow = [True if x <= 1.02 else False for x in lower_shadow]

        for i in range(len(self.data)):
            if long[i] and no_upper_shadow[i] and not flag_type[i] and no_lower_shadow[i]:
                self.data.loc[i, "BearishMarubozuFlag"] = 1
            else:
                self.data.loc[i, "BearishMarubozuFlag"] = 0
    
    def bullishClosingMarubozuFlag(self, alpha = 1.5, n = 20):
        flag_type = [True if self.data.loc[i, "Close"] >= self.data.loc[i, "Open"] else False for i in range(len(self.data))]
        atr = self.calculator.calculateATR(self.data, n)
        long = [True if abs(self.data.loc[i, "Close"]-self.data.loc[i, "Open"]) >= alpha*atr[i] else False for i in range(len(self.data))]
        max_body = [self.data.loc[i, "Open"] if self.data.loc[i, "Open"] >= self.data.loc[i, "Close"] else self.data.loc[i, "Close"] for i in range(len(self.data))]
        min_body = [self.data.loc[i, "Open"] if self.data.loc[i, "Open"] <= self.data.loc[i, "Close"] else self.data.loc[i, "Close"] for i in range(len(self.data))]        
        upper_shadow = [max_body[i]/self.data.loc[i, "High"] for i in range(len(self.data))]
        lower_shadow = [min_body[i]/self.data.loc[i, "Low"]  for i in range(len(self.data))]
        no_upper_shadow = [True if x >= 0.98 else False for x in upper_shadow]
        no_lower_shadow = [True if x <= 1.02 else False for x in lower_shadow]

        for i in range(len(self.data)):
            if long[i] and no_upper_shadow[i] and flag_type[i] and not no_lower_shadow[i]:
                self.data.loc[i, "ClosingMarubozuFlag"] = 1
            else:
                self.data.loc[i, "ClosingMarubozuFlag"] = 0

    def bearishClosingMarubozuFlag(self, alpha = 1.5, n = 20):
        flag_type = [True if self.data.loc[i, "Close"] >= self.data.loc[i, "Open"] else False for i in range(len(self.data))]
        atr = self.calculator.calculateATR(self.data, n)
        long = [True if abs(self.data.loc[i, "Close"]-self.data.loc[i, "Open"]) >= alpha*atr[i] else False for i in range(len(self.data))]
        max_body = [self.data.loc[i, "Open"] if self.data.loc[i, "Open"] >= self.data.loc[i, "Close"] else self.data.loc[i, "Close"] for i in range(len(self.data))]
        min_body = [self.data.loc[i, "Open"] if self.data.loc[i, "Open"] <= self.data.loc[i, "Close"] else self.data.loc[i, "Close"] for i in range(len(self.data))]        
        upper_shadow = [max_body[i]/self.data.loc[i, "High"] for i in range(len(self.data))]
        lower_shadow = [min_body[i]/self.data.loc[i, "Low"]  for i in range(len(self.data))]
        no_upper_shadow = [True if x >= 0.98 else False for x in upper_shadow]
        no_lower_shadow = [True if x <= 1.02 else False for x in lower_shadow]

        for i in range(len(self.data)):
            if long[i] and no_lower_shadow[i] and not flag_type[i] and not no_upper_shadow[i]:
                self.data.loc[i, "BearishClosingMarubozuFlag"] = 1
            else:
                self.data.loc[i, "BearishClosingMarubozuFlag"] = 0

    def bullishOpeningMarubozuFlag(self, alpha = 1.5, n = 20):
        flag_type = [True if self.data.loc[i, "Close"] >= self.data.loc[i, "Open"] else False for i in range(len(self.data))]
        atr = self.calculator.calculateATR(self.data, n)
        long = [True if abs(self.data.loc[i, "Close"]-self.data.loc[i, "Open"]) >= alpha*atr[i] else False for i in range(len(self.data))]
        max_body = [self.data.loc[i, "Open"] if self.data.loc[i, "Open"] >= self.data.loc[i, "Close"] else self.data.loc[i, "Close"] for i in range(len(self.data))]
        min_body = [self.data.loc[i, "Open"] if self.data.loc[i, "Open"] <= self.data.loc[i, "Close"] else self.data.loc[i, "Close"] for i in range(len(self.data))]        
        upper_shadow = [max_body[i]/self.data.loc[i, "High"] for i in range(len(self.data))]
        lower_shadow = [min_body[i]/self.data.loc[i, "Low"]  for i in range(len(self.data))]
        no_upper_shadow = [True if x >= 0.98 else False for x in upper_shadow]
        no_lower_shadow = [True if x <= 1.02 else False for x in lower_shadow]

        for i in range(len(self.data)):
            if long[i] and no_lower_shadow[i] and flag_type[i] and not no_upper_shadow[i]:
                self.data.loc[i, "BullishOpeningMarubozuFlag"] = 1
            else:
                self.data.loc[i, "BullishOpeningMarubozuFlag"] = 0

    def bearishOpeningMarubozuFlag(self, alpha = 1.5, n = 20):
        flag_type = [True if self.data.loc[i, "Close"] >= self.data.loc[i, "Open"] else False for i in range(len(self.data))]
        atr = self.calculator.calculateATR(self.data, n)
        long = [True if abs(self.data.loc[i, "Close"]-self.data.loc[i, "Open"]) >= alpha*atr[i] else False for i in range(len(self.data))]
        max_body = [self.data.loc[i, "Open"] if self.data.loc[i, "Open"] >= self.data.loc[i, "Close"] else self.data.loc[i, "Close"] for i in range(len(self.data))]
        min_body = [self.data.loc[i, "Open"] if self.data.loc[i, "Open"] <= self.data.loc[i, "Close"] else self.data.loc[i, "Close"] for i in range(len(self.data))]        
        upper_shadow = [max_body[i]/self.data.loc[i, "High"] for i in range(len(self.data))]
        lower_shadow = [min_body[i]/self.data.loc[i, "Low"]  for i in range(len(self.data))]
        no_upper_shadow = [True if x >= 0.98 else False for x in upper_shadow]
        no_lower_shadow = [True if x <= 1.02 else False for x in lower_shadow]

        for i in range(len(self.data)):
            if long[i] and no_upper_shadow[i] and not flag_type[i] and not no_lower_shadow[i]:
                self.data.loc[i, "BearishOpeningMarubozuFlag"] = 1
            else:
                self.data.loc[i, "BearishOpeningMarubozuFlag"] = 0

    def dojiFlag(self):
        max_body = [self.data.loc[i, "Open"] if self.data.loc[i, "Open"] >= self.data.loc[i, "Close"] else self.data.loc[i, "Close"] for i in range(len(self.data))]
        min_body = [self.data.loc[i, "Open"] if self.data.loc[i, "Open"] <= self.data.loc[i, "Close"] else self.data.loc[i, "Close"] for i in range(len(self.data))]        
        upper_shadow = [max_body[i]/self.data.loc[i, "High"] for i in range(len(self.data))]
        lower_shadow = [min_body[i]/self.data.loc[i, "Low"]  for i in range(len(self.data))]
        shadow_ratio = [(upper_shadow[i] - max_body[i])/(min_body[i] - lower_shadow[i]) for i in range(len(self.data))]
        body_shadow_ratio = [(max_body[i] - min_body[i])/(upper_shadow[i] - lower_shadow[i]) for i in range(len(self.data))]

        for i in range(len(self.data)):
            if body_shadow_ratio[i] <= 0.10 and shadow_ratio[i] <= 1.25 and shadow_ratio[i] >= 0.75:
                self.data.loc[i, "DojiFlag"] = 1
            else:
                self.data.loc[i, "DojiFlag"] = 0

    def SpinningTop(self):
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


