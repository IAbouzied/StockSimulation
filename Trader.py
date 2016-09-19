from StockBroker import StockBroker
import math

class Trader:
    'AI that comprehends data and initiates trades'

    def __init__(self, balance, fees, cutlosses, getprofit, minimumM, risk, MA15Lead, MA30Lead):
        self.MA15Lead = MA15Lead
        self.MA30Lead = MA30Lead
        self.risk = risk
        self.minimumM = minimumM
        self.cutlosses = cutlosses
        self.getprofit = getprofit
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
        stockname = self.broker.stocks.keys()[self.broker.stocks.values().index(stock)]
        if (stock.stockCount != 0):
            if ((stock.stockValue >= stock.amountSpent * self.getprofit) or (stock.stockValue <= stock.amountSpent * self.cutlosses)):
                self.sell(stock.stockCount, stockname)
        elif ((lastday < now) and (now > self.minimumM) and (self.broker.stocks[stockname].MA15 > self.broker.stocks[stockname].MA30 + self.MA15Lead) and
              (self.broker.stocks[stockname].MA30 > self.broker.stocks[stockname].MA90 + self.MA30Lead)):
            self.buy(math.floor(self.broker.balance / (stock.stockCost * self.risk)), stockname)

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

    def getOut(self):
        for stock in self.broker.stocks:
            self.broker.sell(self.broker.stocks[stock].stockCount, stock)

    def __repr__(self):
        return (str(self.broker.balance) + " " + str(self.broker.fees) + " " + str(self.cutlosses) + " " + str(self.getprofit) + " " +
                str(self.minimumM) + " " + str(self.risk) + " " + str(self.MA15Lead) + " " + str(self.MA30Lead))
