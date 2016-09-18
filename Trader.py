from StockBroker import StockBroker

class Trader:
    'AI that comprehends data and initiates trades'

    def __init__(self, balance, fees):
        self.lastMomentum = {} 
        self.broker = StockBroker(balance, fees)

    def buy(self, x, stockName):
        self.broker.buy(x, stockName)

    def sell(self, x, stockName):
        self.broker.sell(x, stockName)

    def addStock(self, filename, name):
        self.broker.addStock(filename, name)

    def nextDay(self):
        for stock in self.broker.stocks:
            self.lastMomentum[stock] = self.broker.stocks[stock].momentum
        self.broker.nextDay()

    #def think(self, lastday, now):
        

gary = Trader(10000, 15)
gary.addStock("AAPL.csv", "Apple")
for x in range(4):
    gary.nextDay()
    print gary.lastMomentum
    print gary.broker.stocks["Apple"].momentum
    print "\n"
