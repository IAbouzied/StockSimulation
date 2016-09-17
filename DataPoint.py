class DataPoint:
    'A collection of data for a stock on a particular day'

    def __init__(self, name, date, open, high, low, close, volume):
        self.name = name
        self.date = date
        self.open = open
        self.high = high
        self.low = low
        self.close = close
        self.volume = volume

    def name(self):
        return self.name
    def date(self):
        return self.date
    def theOpen(self):
        return self.open
    def high(self):
        return self.high
    def low(self):
        return self.low
    def close(self):
        return self.close
    def volume(self):
        return self.volume
    def __repr__(self):
        return str(self.name + " " + self.date + " " + self.open + " " + self.high + " " + self.low + " " + self.close + " " + self.volume)
    
