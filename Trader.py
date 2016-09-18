from StockBroker import StockBroker
import math

class Trader:
    'AI that comprehends data and initiates trades'

    def __init__(self, balance, fees):
        self.lastMomentum = {}
        self.lastMA15 = {}
        self.lastMA30 = {}
        self.lastMA90 = {}
        self.lastVMomentum = {}
        self.broker = StockBroker(balance, fees)

    def buy(self, x, stockName):
        self.broker.buy(x, stockName)

    def sell(self, x, stockName):
        self.broker.sell(x, stockName)

    def addStock(self, filename, name):
        self.broker.addStock(filename, name)

    def think(self, stock, lastday, now):
        if (stock.stockCount != 0) and ((stock.stockValue >= stock.amountSpent * 1.05) or (stock.stockValue <= stock.amountSpent * 0.98)):
            self.sell(stock.stockCount, self.broker.stocks.keys()[self.broker.stocks.values().index(stock)])
        elif (lastday < now) and (now > 0):
            self.buy(math.floor(self.broker.balance / (stock.stockCost * 10)), self.broker.stocks.keys()[self.broker.stocks.values().index(stock)])

    def nextDay(self):
        for stock in self.broker.stocks:
            self.lastMomentum[stock] = self.broker.stocks[stock].momentum
            self.lastMA15[stock] = self.broker.stocks[stock].MA15
            self.lastMA30[stock] = self.broker.stocks[stock].MA30
            self.lastMA90[stock] = self.broker.stocks[stock].MA90
            self.lastVMomentum[stock] = self.broker.stocks[stock].volumeMomentum
        self.broker.nextDay()
        for stock in self.broker.stocks:
            self.think(self.broker.stocks[stock], self.lastMomentum[stock], self.broker.stocks[stock].momentum)

        

gary = Trader(10000, 15)
gary.addStock("AAPL.csv", "Apple")
for x in range(100):
    gary.nextDay()
