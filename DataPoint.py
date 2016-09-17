class DataPoint:
    'A collection of data for a stock on a particular day'
    n = 0
    average = 0

    def __init__(self, name, date, open, high, low, close, volume):
        self.name = name
        self.date = str(date)
        self.open = open
        self.high = high
        self.low = low
        self.close = close
        self.volume = volume
        DataPoint.n += 1
        DataPoint.average = (DataPoint.average + self.close) / DataPoint.n

    def __repr__(self):
        return str(self.name + " " + self.date + " " + self.open + " " + self.high + " " + self.low + " " + self.close + " " + self.volume)
    
