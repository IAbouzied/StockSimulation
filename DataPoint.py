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
        return name
    def date(self):
        return date
    def theOpen(self):
        return open
    def high(self):
        return high
    def low(self):
        return low
    def close(self):
        return close
    def volume(self):
        return volume
    def __str__(self):
        return str(self.name + " " + self.date + " " + self.open + " " + self.high + " " + self.low + " " + self.close + " " + self.volume)
    
