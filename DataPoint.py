class DataPoint:
    'A collection of data for a stock on a particular day'

    def __init__(self, name, date, open, high, low, close, volume):
        self.name = str(name)
        self.date = str(date)
        self.open = float(open)
        self.high = float(high)
        self.low = float(low)
        self.close = float(close)
        self.volume = float(volume)

    def __repr__(self):
        return str(self.name + " " + self.date + " " + str(self.open) + " " + str(self.high) + " " + str(self.low) + " " + str(self.close) + " " + str(self.volume))
    
