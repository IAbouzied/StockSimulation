from DataList import DataList
import math

class StockBroker:
    'Uses Stock data to simulate an account, buying and selling stocks'

    def __init__(self, filename, name, balance, fees):
        self.stockData = DataList(filename, name)
        self.balance = balance
        self.fees = fees
        self.stockCount = 0
        self.day = 0
        self.stockCost = self.stockData[self.day].close

    def buy(self, x):
        cost = self.stockCost * x + self.fees
        if (cost <= self.balance):
            self.balance -= cost
            self.stockCount += x
            print "Purchased " + str(x) + " stocks for a total of " + str(cost)
        else:
            x = int(math.floor(self.balance / self.stockCost))
            if (x <= 0):
                print "Not enough funds"
                return
            cost = x * self.stockCost + self.fees
            self.balance -=  cost
            self.stockCount += x
            print "Not enough funds, instead purchased " + str(x) + " stocks for a total of " + str(cost)
        
        print "The stock count is now " + str(self.stockCount)
        print "Current balance is " + str(self.balance)

    def sell(self, x):
        if x > self.stockCount:
            x = self.stockCount
        profit = x * self.stockCost - self.fees
        self.balance += profit
        self.stockCount -= x

        print "Sold " + str(x) + " stocks for a total of " + str(profit)
        print "The stock count is now " + str(self.stockCount)
        print "Current balance is " + str(self.balance)
            
            
            
        
