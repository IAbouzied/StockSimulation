from DataList import DataList
import math

class StockBroker:
    'Uses Stock data to simulate an account, where commands can be issued to buy and sell stocks'

    def __init__(self, balance, fees):
        self.stocks = {}
        self.balance = balance

        #Applied each trade
        self.fees = fees

        self.stockCount = 0
        self.day = 0
        self.tradesPerformed = 0

    def buy(self, purchaseAmount, stockName, loud=False):
        if purchaseAmount == 0:
            return

        cost = self.stocks[stockName].stockCost * purchaseAmount + self.fees

        #Complete entire order
        if cost <= self.balance:
            self.balance -= cost
            self.stocks[stockName].stockCount += purchaseAmount
            self.stocks[stockName].amountSpent += cost
            self.stocks[stockName].stockValue = self.stocks[stockName].stockCount * self.stocks[stockName].stockCost
            self.tradesPerformed += 1
            if loud:
                print "Purchased " + str(purchaseAmount) + " " + stockName + " stocks for a total of " + str(cost) + " on " + self.stocks[stockName].DataPoints[self.day].date
        else:
            #Lower order to affordable amount
            purchaseAmount = int(math.floor(self.balance / self.stocks[stockName].stockCost))
            if (purchaseAmount <= 0):
                if loud:
                    print "Not enough funds"
                return
            cost = purchaseAmount * self.stocks[stockName].stockCost + self.fees
            self.balance -=  cost
            self.stocks[stockName].stockCount += purchaseAmount
            self.stocks[stockName].amountSpent += cost
            self.stocks[stockName].stockValue = self.stocks[stockName].stockCount * self.stocks[stockName].stockCost
            self.tradesPerformed += 1
            if loud:
                print "Not enough funds, instead purchased " + str(purchaseAmount) + " " + stockName + " stocks for a total of " + str(cost) + " on " + self.stocks[stockName].DataPoints[self.day].date
        
        if loud:
            print "The stock count is now " + str(self.stocks[stockName].stockCount)
            print "Current balance is " + str(self.balance) + "\n"

    def sell(self, sellAmount, stockName, loud=False):
        if sellAmount == 0:
            return
        if sellAmount > self.stocks[stockName].stockCount:
            sellAmount = self.stocks[stockName].stockCount
        
        profit = sellAmount * self.stocks[stockName].stockCost - self.fees
        self.balance += profit
        self.stocks[stockName].stockCount -= sellAmount
        self.stocks[stockName].amountSpent -= profit
        self.stocks[stockName].stockValue = self.stocks[stockName].stockCount * self.stocks[stockName].stockCost

        if loud:
            print "Sold " + str(sellAmount) + " " + stockName +" stocks for a total of " + str(profit) + " on " + self.stocks[stockName].DataPoints[self.day].date
            print "The stock count is now " + str(self.stocks[stockName].stockCount)
            print "Current balance is " + str(self.balance) + "\n"

    def addStock(self, filename, name):
        self.stocks[name] = DataList(filename, name)

    def nextDay(self):
        self.day += 1
        for stock in self.stocks:
            self.stocks[stock].nextDay()
    
        
            

            
        
