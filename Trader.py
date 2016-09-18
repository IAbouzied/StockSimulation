from StockBroker import StockBroker

class Trader:
    'AI that comprehends data and initiates trades'

    def __init__(self, balance, fees):
        self.broker = StockBroker(balance, fees)

    def buy(self, x, stockName):
        self.broker.buy(x, stockName)

    def sell(self, x, stockName):
        self.broker.sell(x, stockName)

    def addStock(self, filename, name):
        self.broker.addStock(filename, name)

    def nextDay(self):
        self.broker.nextDay()
                        
