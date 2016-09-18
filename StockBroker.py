from DataList import DataList
import math

class StockBroker:
    'Uses Stock data to simulate an account, buying and selling stocks'

    def __init__(self, balance, fees):
        self.stocks = {}
        self.balance = balance
        self.fees = fees
        self.stockCount = 0
        self.day = 0

    def buy(self, x, stockName):
        cost = self.stocks[stockName].stockCost * x + self.fees
        if (cost <= self.balance) and (x != 0):
            self.balance -= cost
            self.stocks[stockName].stockCount += x
            print "Purchased " + str(x) + " stocks for a total of " + str(cost)
        else:
            x = int(math.floor(self.balance / self.stocks[stockName].stockCost))
            if (x <= 0):
                print "Not enough funds"
                return
            cost = x * self.stocks[stockName].stockCost + self.fees
            self.balance -=  cost
            self.stocks[stockName].stockCount += x
            print "Not enough funds, instead purchased " + str(x) + " stocks for a total of " + str(cost)
        
        print "The stock count is now " + str(self.stocks[stockName].stockCount)
        print "Current balance is " + str(self.balance)

    def sell(self, x, stockName):
        if x > self.stocks[stockName].stockCount:
            x = self.stocks[stockName].stockCount
        profit = x * self.stocks[stockName].stockCost - self.fees
        self.balance += profit
        self.stocks[stockName].stockCount -= x

        print "Sold " + str(x) + " stocks for a total of " + str(profit)
        print "The stock count is now " + str(self.stocks[stockName].stockCount)
        print "Current balance is " + str(self.balance)

    def addStock(self, filename, name):
        self.stocks[name] = DataList(filename, name)

    def nextDay(self):
        self.day += 1
        for stock in self.stocks:
            self.stocks[stock].nextDay()
    
        
            

            
        
