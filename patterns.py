from metrics import *
from stock_history import Ticker
import numpy as np


class Patterns(Ticker):
    def __init__(self, ticker) -> None:
        Ticker.__init__(self, ticker)
        self.getHistory()
        self.calculator = Metrics()

    def flagType(self):
        self.data["Type"] = [
            1 if self.data.loc[i, "Close"] >= self.data.loc[i, "Open"] else -1 for i in range(len(self.data))
        ]

    def longFlag(self, n=20, alpha=2):
        #   Calculate ATR(x)
        atr = self.calculator.calculateATR(self.data, n)
        self.data["LongFlag"] = [
            1 if abs(self.data.loc[i, "Close"] - self.data.loc[i, "Open"]) >= alpha * atr[i] else 0
            for i in range(len(self.data))
        ]

    def shortFlag(self, n=20, alpha=0.5):
        #   Calculate ATR(x)
        atr = self.calculator.calculateATR(self.data, n)
        self.data["ShortFlag"] = [
            1 if abs(self.data.loc[i, "Close"] - self.data.loc[i, "Open"]) <= alpha * atr[i] else 0
            for i in range(len(self.data))
        ]

    def bullishMarubozuFlag(self, alpha=1.5, n=20):
        flag_type = [
            True if self.data.loc[i, "Close"] >= self.data.loc[i, "Open"] else False for i in range(len(self.data))
        ]
        atr = self.calculator.calculateATR(self.data, n)
        long = [
            True if abs(self.data.loc[i, "Close"] - self.data.loc[i, "Open"]) >= alpha * atr[i] else False
            for i in range(len(self.data))
        ]
        max_body = [
            self.data.loc[i, "Open"]
            if self.data.loc[i, "Open"] >= self.data.loc[i, "Close"]
            else self.data.loc[i, "Close"]
            for i in range(len(self.data))
        ]
        min_body = [
            self.data.loc[i, "Open"]
            if self.data.loc[i, "Open"] <= self.data.loc[i, "Close"]
            else self.data.loc[i, "Close"]
            for i in range(len(self.data))
        ]
        upper_shadow = [max_body[i] / self.data.loc[i, "High"] for i in range(len(self.data))]
        lower_shadow = [min_body[i] / self.data.loc[i, "Low"] for i in range(len(self.data))]
        no_upper_shadow = [True if x >= 0.98 else False for x in upper_shadow]
        no_lower_shadow = [True if x <= 1.02 else False for x in lower_shadow]

        for i in range(len(self.data)):
            if long[i] and no_upper_shadow[i] and flag_type[i] and no_lower_shadow[i]:
                self.data.loc[i, "BullishMarubozuFlag"] = 1
            else:
                self.data.loc[i, "BullishMarubozuFlag"] = 0

    def bearishMarubozuFlag(self, alpha=1.5, n=20):
        flag_type = [
            True if self.data.loc[i, "Close"] >= self.data.loc[i, "Open"] else False for i in range(len(self.data))
        ]
        atr = self.calculator.calculateATR(self.data, n)
        long = [
            True if abs(self.data.loc[i, "Close"] - self.data.loc[i, "Open"]) >= alpha * atr[i] else False
            for i in range(len(self.data))
        ]
        max_body = [
            self.data.loc[i, "Open"]
            if self.data.loc[i, "Open"] >= self.data.loc[i, "Close"]
            else self.data.loc[i, "Close"]
            for i in range(len(self.data))
        ]
        min_body = [
            self.data.loc[i, "Open"]
            if self.data.loc[i, "Open"] <= self.data.loc[i, "Close"]
            else self.data.loc[i, "Close"]
            for i in range(len(self.data))
        ]
        upper_shadow = [max_body[i] / self.data.loc[i, "High"] for i in range(len(self.data))]
        lower_shadow = [min_body[i] / self.data.loc[i, "Low"] for i in range(len(self.data))]
        no_upper_shadow = [True if x >= 0.98 else False for x in upper_shadow]
        no_lower_shadow = [True if x <= 1.02 else False for x in lower_shadow]

        for i in range(len(self.data)):
            if long[i] and no_upper_shadow[i] and not flag_type[i] and no_lower_shadow[i]:
                self.data.loc[i, "BearishMarubozuFlag"] = 1
            else:
                self.data.loc[i, "BearishMarubozuFlag"] = 0

    def bullishClosingMarubozuFlag(self, alpha=1.5, n=20):
        flag_type = [
            True if self.data.loc[i, "Close"] >= self.data.loc[i, "Open"] else False for i in range(len(self.data))
        ]
        atr = self.calculator.calculateATR(self.data, n)
        long = [
            True if abs(self.data.loc[i, "Close"] - self.data.loc[i, "Open"]) >= alpha * atr[i] else False
            for i in range(len(self.data))
        ]
        max_body = [
            self.data.loc[i, "Open"]
            if self.data.loc[i, "Open"] >= self.data.loc[i, "Close"]
            else self.data.loc[i, "Close"]
            for i in range(len(self.data))
        ]
        min_body = [
            self.data.loc[i, "Open"]
            if self.data.loc[i, "Open"] <= self.data.loc[i, "Close"]
            else self.data.loc[i, "Close"]
            for i in range(len(self.data))
        ]
        upper_shadow = [max_body[i] / self.data.loc[i, "High"] for i in range(len(self.data))]
        lower_shadow = [min_body[i] / self.data.loc[i, "Low"] for i in range(len(self.data))]
        no_upper_shadow = [True if x >= 0.98 else False for x in upper_shadow]
        no_lower_shadow = [True if x <= 1.02 else False for x in lower_shadow]

        for i in range(len(self.data)):
            if long[i] and no_upper_shadow[i] and flag_type[i] and not no_lower_shadow[i]:
                self.data.loc[i, "ClosingMarubozuFlag"] = 1
            else:
                self.data.loc[i, "ClosingMarubozuFlag"] = 0

    def bearishClosingMarubozuFlag(self, alpha=1.5, n=20):
        flag_type = [
            True if self.data.loc[i, "Close"] >= self.data.loc[i, "Open"] else False for i in range(len(self.data))
        ]
        atr = self.calculator.calculateATR(self.data, n)
        long = [
            True if abs(self.data.loc[i, "Close"] - self.data.loc[i, "Open"]) >= alpha * atr[i] else False
            for i in range(len(self.data))
        ]
        max_body = [
            self.data.loc[i, "Open"]
            if self.data.loc[i, "Open"] >= self.data.loc[i, "Close"]
            else self.data.loc[i, "Close"]
            for i in range(len(self.data))
        ]
        min_body = [
            self.data.loc[i, "Open"]
            if self.data.loc[i, "Open"] <= self.data.loc[i, "Close"]
            else self.data.loc[i, "Close"]
            for i in range(len(self.data))
        ]
        upper_shadow = [max_body[i] / self.data.loc[i, "High"] for i in range(len(self.data))]
        lower_shadow = [min_body[i] / self.data.loc[i, "Low"] for i in range(len(self.data))]
        no_upper_shadow = [True if x >= 0.98 else False for x in upper_shadow]
        no_lower_shadow = [True if x <= 1.02 else False for x in lower_shadow]

        for i in range(len(self.data)):
            if long[i] and no_lower_shadow[i] and not flag_type[i] and not no_upper_shadow[i]:
                self.data.loc[i, "BearishClosingMarubozuFlag"] = 1
            else:
                self.data.loc[i, "BearishClosingMarubozuFlag"] = 0

    def bullishOpeningMarubozuFlag(self, alpha=1.5, n=20):
        flag_type = [
            True if self.data.loc[i, "Close"] >= self.data.loc[i, "Open"] else False for i in range(len(self.data))
        ]
        atr = self.calculator.calculateATR(self.data, n)
        long = [
            True if abs(self.data.loc[i, "Close"] - self.data.loc[i, "Open"]) >= alpha * atr[i] else False
            for i in range(len(self.data))
        ]
        max_body = [
            self.data.loc[i, "Open"]
            if self.data.loc[i, "Open"] >= self.data.loc[i, "Close"]
            else self.data.loc[i, "Close"]
            for i in range(len(self.data))
        ]
        min_body = [
            self.data.loc[i, "Open"]
            if self.data.loc[i, "Open"] <= self.data.loc[i, "Close"]
            else self.data.loc[i, "Close"]
            for i in range(len(self.data))
        ]
        upper_shadow = [max_body[i] / self.data.loc[i, "High"] for i in range(len(self.data))]
        lower_shadow = [min_body[i] / self.data.loc[i, "Low"] for i in range(len(self.data))]
        no_upper_shadow = [True if x >= 0.98 else False for x in upper_shadow]
        no_lower_shadow = [True if x <= 1.02 else False for x in lower_shadow]

        for i in range(len(self.data)):
            if long[i] and no_lower_shadow[i] and flag_type[i] and not no_upper_shadow[i]:
                self.data.loc[i, "BullishOpeningMarubozuFlag"] = 1
            else:
                self.data.loc[i, "BullishOpeningMarubozuFlag"] = 0

    def bearishOpeningMarubozuFlag(self, alpha=1.5, n=20):
        flag_type = [
            True if self.data.loc[i, "Close"] >= self.data.loc[i, "Open"] else False for i in range(len(self.data))
        ]
        atr = self.calculator.calculateATR(self.data, n)
        long = [
            True if abs(self.data.loc[i, "Close"] - self.data.loc[i, "Open"]) >= alpha * atr[i] else False
            for i in range(len(self.data))
        ]
        max_body = [
            self.data.loc[i, "Open"]
            if self.data.loc[i, "Open"] >= self.data.loc[i, "Close"]
            else self.data.loc[i, "Close"]
            for i in range(len(self.data))
        ]
        min_body = [
            self.data.loc[i, "Open"]
            if self.data.loc[i, "Open"] <= self.data.loc[i, "Close"]
            else self.data.loc[i, "Close"]
            for i in range(len(self.data))
        ]
        upper_shadow = [max_body[i] / self.data.loc[i, "High"] for i in range(len(self.data))]
        lower_shadow = [min_body[i] / self.data.loc[i, "Low"] for i in range(len(self.data))]
        no_upper_shadow = [True if x >= 0.98 else False for x in upper_shadow]
        no_lower_shadow = [True if x <= 1.02 else False for x in lower_shadow]

        for i in range(len(self.data)):
            if long[i] and no_upper_shadow[i] and not flag_type[i] and not no_lower_shadow[i]:
                self.data.loc[i, "BearishOpeningMarubozuFlag"] = 1
            else:
                self.data.loc[i, "BearishOpeningMarubozuFlag"] = 0

    def SpinningTopFlag(self):
        max_body = [
            self.data.loc[i, "Open"]
            if self.data.loc[i, "Open"] >= self.data.loc[i, "Close"]
            else self.data.loc[i, "Close"]
            for i in range(len(self.data))
        ]
        min_body = [
            self.data.loc[i, "Open"]
            if self.data.loc[i, "Open"] <= self.data.loc[i, "Close"]
            else self.data.loc[i, "Close"]
            for i in range(len(self.data))
        ]
        upper_shadow = [self.data.loc[i, "High"] - max_body[i] for i in range(len(self.data))]
        lower_shadow = [min_body[i] - self.data.loc[i, "Low"] for i in range(len(self.data))]
        body_size = [max_body[i] - min_body[i] for i in range(len(self.data))]
        shadow_ratio = [
            (self.data.loc[i, "High"] - max_body[i]) / (min_body[i] - self.data.loc[i, "Low"])
            for i in range(len(self.data))
        ]
        body_shadow_ratio = [
            body_size / (self.data.loc[i, "High"] - self.data.loc[i, "Low"]) for i in range(len(self.data))
        ]

        for i in range(len(self.data)):
            try:
                if (
                    body_shadow_ratio[i]
                    > 0.05 & shadow_ratio[i]
                    <= 1.25 & shadow_ratio[i]
                    >= 0.75 & upper_shadow[i]
                    >= 2 * body_size[i] & lower_shadow[i]
                    >= 2 * body_size[i]
                ):
                    self.data.loc[i, "SpinningTopFlag"] = 1
                else:
                    self.data.loc[i, "SpinningTopFlag"] = 0
            except:
                self.data.loc[i, "SpinningTopFlag"] = 0

    def dojiFlag(self):
        max_body = [
            self.data.loc[i, "Open"]
            if self.data.loc[i, "Open"] >= self.data.loc[i, "Close"]
            else self.data.loc[i, "Close"]
            for i in range(len(self.data))
        ]
        min_body = [
            self.data.loc[i, "Open"]
            if self.data.loc[i, "Open"] <= self.data.loc[i, "Close"]
            else self.data.loc[i, "Close"]
            for i in range(len(self.data))
        ]
        shadow_ratio = [
            (self.data.loc[i, "High"] - max_body[i]) / (min_body[i] - self.data.loc[i, "Low"])
            for i in range(len(self.data))
        ]
        body_shadow_ratio = [
            (max_body[i] - min_body[i]) / (self.data.loc[i, "High"] - self.data.loc[i, "Low"])
            for i in range(len(self.data))
        ]

        for i in range(len(self.data)):
            if body_shadow_ratio[i] <= 0.05 and shadow_ratio[i] <= 1.25 and shadow_ratio[i] >= 0.75:
                self.data.loc[i, "DojiFlag"] = 1
            else:
                self.data.loc[i, "DojiFlag"] = 0

    def longLeggedDojiFlag(self, n=20, alpha=1.5):
        atr = self.calculator.calculateATR(self.data, n)
        long_range = [
            True if self.data.loc[i, "High"] - self.data.loc[i, "Low"] >= alpha * atr[i] else False
            for i in range(len(self.data))
        ]
        max_body = [
            self.data.loc[i, "Open"]
            if self.data.loc[i, "Open"] >= self.data.loc[i, "Close"]
            else self.data.loc[i, "Close"]
            for i in range(len(self.data))
        ]
        min_body = [
            self.data.loc[i, "Open"]
            if self.data.loc[i, "Open"] <= self.data.loc[i, "Close"]
            else self.data.loc[i, "Close"]
            for i in range(len(self.data))
        ]
        shadow_ratio = [
            (self.data.loc[i, "High"] - max_body[i]) / (min_body[i] - self.data.loc[i, "Low"])
            for i in range(len(self.data))
        ]
        body_shadow_ratio = [
            (max_body[i] - min_body[i]) / (self.data.loc[i, "High"] - self.data.loc[i, "Low"])
            for i in range(len(self.data))
        ]
        bool_body_shadow_ratio = [True if x <= 0.05 else False for x in body_shadow_ratio]
        bool_shadow_ratio = [True if x <= 1.25 and x >= 0.75 else False for x in shadow_ratio]

        for i in range(len(self.data)):
            if bool_body_shadow_ratio[i] and bool_shadow_ratio[i] and long_range[i]:
                self.data.loc[i, "LongLeggedDojiFlag"] = 1
            else:
                self.data.loc[i, "LongLeggedDojiFlag"] = 0

    def crossDojiFlag(self, n=20, alpha=1.5):
        atr = self.calculator.calculateATR(self.data, n)
        long_range = [
            True if self.data.loc[i, "High"] - self.data.loc[i, "Low"] >= alpha * atr[i] else False
            for i in range(len(self.data))
        ]
        max_body = [
            self.data.loc[i, "Open"]
            if self.data.loc[i, "Open"] >= self.data.loc[i, "Close"]
            else self.data.loc[i, "Close"]
            for i in range(len(self.data))
        ]
        min_body = [
            self.data.loc[i, "Open"]
            if self.data.loc[i, "Open"] <= self.data.loc[i, "Close"]
            else self.data.loc[i, "Close"]
            for i in range(len(self.data))
        ]
        shadow_ratio = [
            (self.data.loc[i, "High"] - max_body[i]) / (min_body[i] - self.data.loc[i, "Low"])
            for i in range(len(self.data))
        ]
        body_shadow_ratio = [
            (max_body[i] - min_body[i]) / (self.data.loc[i, "High"] - self.data.loc[i, "Low"])
            for i in range(len(self.data))
        ]
        bool_body_shadow_ratio = [True if x <= 0.05 else False for x in body_shadow_ratio]
        bool_shadow_ratio = [True if x <= 0.50 else False for x in shadow_ratio]

        for i in range(len(self.data)):
            if bool_body_shadow_ratio[i] and bool_shadow_ratio[i] and long_range[i]:
                self.data.loc[i, "CrossDojiFlag"] = 1
            else:
                self.data.loc[i, "CrossDojiFlag"] = 0

    def invertedCrossDojiFlag(self, n=20, alpha=1.5):
        atr = self.calculator.calculateATR(self.data, n)
        long_range = [
            True if self.data.loc[i, "High"] - self.data.loc[i, "Low"] >= alpha * atr[i] else False
            for i in range(len(self.data))
        ]
        max_body = [
            self.data.loc[i, "Open"]
            if self.data.loc[i, "Open"] >= self.data.loc[i, "Close"]
            else self.data.loc[i, "Close"]
            for i in range(len(self.data))
        ]
        min_body = [
            self.data.loc[i, "Open"]
            if self.data.loc[i, "Open"] <= self.data.loc[i, "Close"]
            else self.data.loc[i, "Close"]
            for i in range(len(self.data))
        ]
        shadow_ratio = [
            (self.data.loc[i, "High"] - max_body[i]) / (min_body[i] - self.data.loc[i, "Low"])
            for i in range(len(self.data))
        ]
        body_shadow_ratio = [
            (max_body[i] - min_body[i]) / (self.data.loc[i, "High"] - self.data.loc[i, "Low"])
            for i in range(len(self.data))
        ]
        bool_body_shadow_ratio = [True if x <= 0.05 else False for x in body_shadow_ratio]
        bool_shadow_ratio = [True if x >= 1.50 else False for x in shadow_ratio]

        for i in range(len(self.data)):
            if bool_body_shadow_ratio[i] and bool_shadow_ratio[i] and long_range[i]:
                self.data.loc[i, "InvertedCrossDojiFlag"] = -1
            else:
                self.data.loc[i, "InvertedCrossDojiFlag"] = 0

    def hammerFlag(self, n=20, alpha=1.5):
        atr = self.calculator.calculateATR(self.data, n)
        long_range = [
            True if self.data.loc[i, "High"] - self.data.loc[i, "Low"] >= alpha * atr[i] else False
            for i in range(len(self.data))
        ]
        max_body = [
            self.data.loc[i, "Open"]
            if self.data.loc[i, "Open"] >= self.data.loc[i, "Close"]
            else self.data.loc[i, "Close"]
            for i in range(len(self.data))
        ]
        min_body = [
            self.data.loc[i, "Open"]
            if self.data.loc[i, "Open"] <= self.data.loc[i, "Close"]
            else self.data.loc[i, "Close"]
            for i in range(len(self.data))
        ]
        shadow_ratio = [
            (self.data.loc[i, "High"] - max_body[i]) / (min_body[i] - self.data.loc[i, "Low"])
            for i in range(len(self.data))
        ]
        body_shadow_ratio = [
            (max_body[i] - min_body[i]) / (self.data.loc[i, "High"] - self.data.loc[i, "Low"])
            for i in range(len(self.data))
        ]
        bool_body_shadow_ratio = [True if x <= 0.10 else False for x in body_shadow_ratio]
        bool_shadow_ratio = [True if x <= 0.25 else False for x in shadow_ratio]
        trend_n = self.calculator.calculatePctChange(self.data, n)
        bool_trend = [True if x <= 0 else False for x in trend_n]

        for i in range(len(self.data)):
            if bool_body_shadow_ratio[i] and bool_shadow_ratio[i] and long_range[i] and bool_trend[i]:
                self.data.loc[i, "HammerFlag"] = 1
            else:
                self.data.loc[i, "HammerFlag"] = 0

    def hangingManFlag(self, n=20, alpha=1.5):
        atr = self.calculator.calculateATR(self.data, n)
        long_range = [
            True if self.data.loc[i, "High"] - self.data.loc[i, "Low"] >= alpha * atr[i] else False
            for i in range(len(self.data))
        ]
        max_body = [
            self.data.loc[i, "Open"]
            if self.data.loc[i, "Open"] >= self.data.loc[i, "Close"]
            else self.data.loc[i, "Close"]
            for i in range(len(self.data))
        ]
        min_body = [
            self.data.loc[i, "Open"]
            if self.data.loc[i, "Open"] <= self.data.loc[i, "Close"]
            else self.data.loc[i, "Close"]
            for i in range(len(self.data))
        ]
        shadow_ratio = [
            (self.data.loc[i, "High"] - max_body[i]) / (min_body[i] - self.data.loc[i, "Low"])
            for i in range(len(self.data))
        ]
        body_shadow_ratio = [
            (max_body[i] - min_body[i]) / (self.data.loc[i, "High"] - self.data.loc[i, "Low"])
            for i in range(len(self.data))
        ]
        bool_body_shadow_ratio = [True if x <= 0.10 else False for x in body_shadow_ratio]
        bool_shadow_ratio = [True if x <= 0.25 else False for x in shadow_ratio]
        trend_n = self.calculator.calculatePctChange(self.data, n)
        bool_trend = [True if x >= 0 else False for x in trend_n]

        for i in range(len(self.data)):
            if bool_body_shadow_ratio[i] and bool_shadow_ratio[i] and long_range[i] and bool_trend[i]:
                self.data.loc[i, "HangingManFlag"] = -1
            else:
                self.data.loc[i, "HangingManFlag"] = 0

    def invertedHammerFlag(self, n=20, alpha=1.5):
        atr = self.calculator.calculateATR(self.data, n)
        long_range = [
            True if self.data.loc[i, "High"] - self.data.loc[i, "Low"] >= alpha * atr[i] else False
            for i in range(len(self.data))
        ]
        max_body = [
            self.data.loc[i, "Open"]
            if self.data.loc[i, "Open"] >= self.data.loc[i, "Close"]
            else self.data.loc[i, "Close"]
            for i in range(len(self.data))
        ]
        min_body = [
            self.data.loc[i, "Open"]
            if self.data.loc[i, "Open"] <= self.data.loc[i, "Close"]
            else self.data.loc[i, "Close"]
            for i in range(len(self.data))
        ]
        shadow_ratio = [
            (self.data.loc[i, "High"] - max_body[i]) / (min_body[i] - self.data.loc[i, "Low"])
            for i in range(len(self.data))
        ]
        body_shadow_ratio = [
            (max_body[i] - min_body[i]) / (self.data.loc[i, "High"] - self.data.loc[i, "Low"])
            for i in range(len(self.data))
        ]
        bool_body_shadow_ratio = [True if x <= 0.10 else False for x in body_shadow_ratio]
        bool_shadow_ratio = [True if x <= 1.75 else False for x in shadow_ratio]
        trend_n = self.calculator.calculatePctChange(self.data, n)
        bool_trend = [True if x <= 0 else False for x in trend_n]

        for i in range(len(self.data)):
            if bool_body_shadow_ratio[i] and bool_shadow_ratio[i] and long_range[i] and bool_trend[i]:
                self.data.loc[i, "InvertedHammerFlag"] = 1
            else:
                self.data.loc[i, "InvertedHammerFlag"] = 0
    
    def shootingStarFlag(self, n=20, alpha=1.5):
        atr = self.calculator.calculateATR(self.data, n)
        long_range = [
            True if self.data.loc[i, "High"] - self.data.loc[i, "Low"] >= alpha * atr[i] else False
            for i in range(len(self.data))
        ]
        max_body = [
            self.data.loc[i, "Open"]
            if self.data.loc[i, "Open"] >= self.data.loc[i, "Close"]
            else self.data.loc[i, "Close"]
            for i in range(len(self.data))
        ]
        min_body = [
            self.data.loc[i, "Open"]
            if self.data.loc[i, "Open"] <= self.data.loc[i, "Close"]
            else self.data.loc[i, "Close"]
            for i in range(len(self.data))
        ]
        shadow_ratio = [
            (self.data.loc[i, "High"] - max_body[i]) / (min_body[i] - self.data.loc[i, "Low"])
            for i in range(len(self.data))
        ]
        body_shadow_ratio = [
            (max_body[i] - min_body[i]) / (self.data.loc[i, "High"] - self.data.loc[i, "Low"])
            for i in range(len(self.data))
        ]
        bool_body_shadow_ratio = [True if x <= 0.10 else False for x in body_shadow_ratio]
        bool_shadow_ratio = [True if x <= 1.75 else False for x in shadow_ratio]
        trend_n = self.calculator.calculatePctChange(self.data, n)
        bool_trend = [True if x > 0 else False for x in trend_n]

        for i in range(len(self.data)):
            if bool_body_shadow_ratio[i] and bool_shadow_ratio[i] and long_range[i] and bool_trend[i]:
                self.data.loc[i, "ShootingStarFlag"] = -1
            else:
                self.data.loc[i, "ShootingStarFlag"] = 0

    def bullishEngulfingFlag(self, n=20):
        trend_n = self.calculator.calculatePctChange(self.data, n)
        trend = [True if x < 0 else False for x in trend_n]
        prior_candle_red = [False] + [True if self.data.loc[i-1, "Close"] < self.data.loc[i-1, "Open"] else False for i in range(1,len(self.data),1)]
        current_candle_green = [False] + [True if self.data.loc[i, "Close"] > self.data.loc[i, "Open"] else False for i in range(1,len(self.data),1)]
        body_engulfed = [False] + [True if (self.data.loc[i, "Close"] > self.data.loc[i-1, "Close"] and 
                                            self.data.loc[i, "Open"] < self.data.loc[i-1, "Open"])
                                        else False for i in range(1,len(self.data),1)]
        shadows_engulfed = [False] + [True if (self.data.loc[i, "High"] > self.data.loc[i-1, "High"] and
                                                self.data.loc[i, "Low"] < self.data.loc[i-1, "Low"])
                                            else False for i in range(1,len(self.data),1)]
        
        for i in range(len(self.data)):
            if prior_candle_red[i] and current_candle_green[i] and body_engulfed[i] and shadows_engulfed[i] and trend[i]:
                self.data.loc[i, "BullishEngulfingFlag"] = 1
            else:
                self.data.loc[i, "BullishEngulfingFlag"] = 0
          
    def bearishEngulfingFlag(self, n=20):
        trend_n = self.calculator.calculatePctChange(self.data, n)
        trend = [True if x > 0 else False for x in trend_n]
        prior_candle_green = [False] + [True if self.data.loc[i-1, "Open"] < self.data.loc[i-1, "Close"] else False for i in range(1,len(self.data),1)]
        current_candle_red = [False] + [True if self.data.loc[i, "Open"] > self.data.loc[i, "Close"] else False for i in range(1,len(self.data),1)]
        body_engulfed = [False] + [True if (self.data.loc[i, "Open"] > self.data.loc[i-1, "Close"] and 
                                            self.data.loc[i, "Close"] < self.data.loc[i-1, "Open"])
                                        else False for i in range(1,len(self.data),1)]
        shadows_engulfed = [False] + [True if (self.data.loc[i, "High"] > self.data.loc[i-1, "High"] and
                                                self.data.loc[i, "Low"] < self.data.loc[i-1, "Low"])
                                            else False for i in range(1,len(self.data),1)]
        
        for i in range(len(self.data)):
            if prior_candle_green[i] and current_candle_red[i] and body_engulfed[i] and shadows_engulfed[i] and trend[i]:
                self.data.loc[i, "BearishEngulfingFlag"] = -1
            else:
                self.data.loc[i, "BearishEngulfingFlag"] = 0

    def piercingFlag(self, n=20):
        
        trend_n = self.calculator.calculatePctChange(self.data, n)
        trend = [True if x < 0 else False for x in trend_n]
        prior_candle_red = [False] + [True if self.data.loc[i-1, "Close"] < self.data.loc[i-1, "Open"] else False for i in range(1,len(self.data),1)]
        current_candle_green = [False] + [True if self.data.loc[i, "Close"] > self.data.loc[i, "Open"] else False for i in range(1,len(self.data),1)]
        body_pierced = [False] + [True if (self.data.loc[i, "Close"] > sum(self.data.loc[i-1, ["Open", "Close"]].values)/2 and 
                                            self.data.loc[i, "Close"] < self.data.loc[i-1, "Open"])
                                        else False for i in range(1,len(self.data),1)]
        gap_down = [False] + [True if self.data.loc[i, "Open"] < self.data.loc[i-1, "Low"]
                                    else False for i in range(1,len(self.data),1)]

        for i in range(len(self.data)):
            if prior_candle_red[i] and current_candle_green[i] and body_pierced[i] and gap_down[i] and trend[i]:
                self.data.loc[i, "PiercingFlag"] = 1
            else:
                self.data.loc[i, "PiercingFlag"] = 0

    def darkCloudFlag(self, n=20):
        trend_n = self.calculator.calculatePctChange(self.data, n)
        trend = [True if x > 0 else False for x in trend_n]
        prior_candle_green = [False] + [True if self.data.loc[i-1, "Close"] > self.data.loc[i-1, "Open"] else False for i in range(1,len(self.data),1)]
        current_candle_red = [False] + [True if self.data.loc[i, "Close"] < self.data.loc[i, "Open"] else False for i in range(1,len(self.data),1)]
        body_pierced = [False] + [True if (self.data.loc[i, "Close"] < sum(self.data.loc[i-1, ["Open", "Close"]].values)/2 and 
                                            self.data.loc[i, "Close"] > self.data.loc[i-1, "Open"])
                                        else False for i in range(1,len(self.data),1)]
        gap_up = [False] + [True if self.data.loc[i, "Open"] > self.data.loc[i-1, "High"]
                                 else False for i in range(1,len(self.data),1)]

        for i in range(len(self.data)):
            if prior_candle_green[i] and current_candle_red[i] and body_pierced[i] and gap_up[i] and trend[i]:
                self.data.loc[i, "DarkCloudFlag"] = -1
            else:
                self.data.loc[i, "DarkCloudFlag"] = 0

    def bullishHaramiFlag(self, n=20, alpha = 0.50):
        atr = self.calculator.calculateATR(self.data, n)
        short_flag = [
            1 if abs(self.data.loc[i, "High"] - self.data.loc[i, "Low"]) <= alpha * atr[i] else 0
            for i in range(len(self.data))
        ]
        body_ratio = [False] + [True if abs(self.data.loc[i, "Open"] - self.data.loc[i, "Close"])/abs(self.data.loc[i-1, "Open"] - self.data.loc[i-1, "Close"]) <= 0.25 
                                     else False for i in range(1,len(self.data), 1)]
        trend_n = self.calculator.calculatePctChange(self.data, n)
        trend = [True if x < 0 else False for x in trend_n]
        prior_candle_red = [False] + [True if self.data.loc[i-1, "Close"] < self.data.loc[i-1, "Open"] else False for i in range(1,len(self.data),1)]
        current_candle_green = [False] + [True if self.data.loc[i, "Close"] > self.data.loc[i, "Open"] else False for i in range(1,len(self.data),1)]
        shadows_engulfed = [False] + [True if (self.data.loc[i, "High"] < self.data.loc[i-1, "Open"] and
                                                self.data.loc[i, "Low"] > self.data.loc[i-1, "Close"])
                                            else False for i in range(1,len(self.data),1)]
        
        for i in range(len(self.data)):
            if prior_candle_red[i] and current_candle_green[i] and short_flag[i] and shadows_engulfed[i] and trend[i] and body_ratio[i]:
                self.data.loc[i, "BullishHaramiFlag"] = 1
            else:
                self.data.loc[i, "BullishHaramiFlag"] = 0

    def bearishHaramiFlag(self, n=20, alpha = 0.50):
        atr = self.calculator.calculateATR(self.data, n)
        short_flag = [
            1 if abs(self.data.loc[i, "Close"] - self.data.loc[i, "Open"]) <= alpha * atr[i] else 0
            for i in range(len(self.data))
        ]
        body_ratio = [False] + [True if abs(self.data.loc[i, "Open"] - self.data.loc[i, "Close"])/abs(self.data.loc[i-1, "Open"] - self.data.loc[i-1, "Close"]) <= 0.25 
                                else False for i in range(1,len(self.data), 1)]
        trend_n = self.calculator.calculatePctChange(self.data, n)
        trend = [True if x > 0 else False for x in trend_n]
        prior_candle_green = [False] + [True if self.data.loc[i-1, "Close"] > self.data.loc[i-1, "Open"] else False for i in range(1,len(self.data),1)]
        current_candle_red = [False] + [True if self.data.loc[i, "Close"] < self.data.loc[i, "Open"] else False for i in range(1,len(self.data),1)]
        shadows_engulfed = [False] + [True if (self.data.loc[i, "High"] < self.data.loc[i-1, "Close"] and
                                                self.data.loc[i, "Low"] > self.data.loc[i-1, "Open"])
                                            else False for i in range(1,len(self.data),1)]
        
        for i in range(len(self.data)):
            if prior_candle_green[i] and current_candle_red[i] and short_flag[i] and shadows_engulfed[i] and trend[i] and body_ratio[i]:
                self.data.loc[i, "BearishHaramiFlag"] = -1
            else:
                self.data.loc[i, "BearishHaramiFlag"] = 0
        
    def bullishFickerFlag(self):
        pass

    def bearishKickerFlag(self):
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
