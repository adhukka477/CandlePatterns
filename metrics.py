


class Metrics():

    def __init__(self):
        pass


    def calculateATR(self, data, x):
        # Calculate atr and backfill prior data with last known atr(x)
        tr = []
        atr = []
        for i in len(data):
            high_low = data.loc[i, "High"] - data.loc[i, "Low"]
            abs_high_close = abs(data.loc[i, "High"] - data.loc[i, "Close"])
            abs_low_close = abs(data.loc[i, "Low"] - data.loc[i, "Close"])
            tr.append(max(high_low, abs_high_close, abs_low_close))

        return(sum(tr)/len(tr))

    def calculateSMA(self):
        pass

    def calculateEMA(self):
        pass
    