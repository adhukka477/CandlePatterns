import ta

class Metrics():

    def __init__(self):
        pass


    def calculateATR(self, data, x):
        # Calculate atr and backfill prior data with last known atr(x)
        atr = ta.volatility.AverageTrueRange(high = data.High, 
                                            low = data.Low, 
                                            close = data.Close, 
                                            window = x,
                                            fillna = False).average_true_range()
        atr[:x] = atr[x]
                    
        return(atr)

    def calculateSMA(self):
        pass

    def calculateEMA(self):
        pass
    