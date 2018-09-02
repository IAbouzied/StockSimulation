from Trader import Trader
import random

class Evolution:
    def __init__(self, population, balance, fees):
        self.balance = balance
        self.fees = fees
        self.traders = []
        self.generationNumber = 1

        #How many traders run each generation
        self.population = population
        self.firstGeneration()
        self.tradeYear()

    def firstGeneration(self):
        #The ranges here can be played around with to expand the room for mutations
        for x in range(self.population):
            cutlosses = float(random.randrange(85, 99)) / 100
            getprofit = float(random.randrange(101, 111)) / 100
            minimumM = float((random.randrange(-200, 300, 5))) / 100
            risk = random.randrange(7,20,1)
            MA15Lead = float((random.randrange(-200, 300, 5))) / 100
            MA30Lead = float((random.randrange(-200, 300, 5))) / 100

            newTrader = Trader(self.balance, self.fees, cutlosses, getprofit, minimumM, risk, MA15Lead, MA30Lead)
            newTrader.addStock("StockData/AAPL.csv", "Apple")
            newTrader.addStock("StockData/ATVI.csv", "Activision")
            newTrader.addStock("StockData/FB.csv", "Facebook")
            newTrader.addStock("StockData/CSCO.csv", "Cisco")
            newTrader.addStock("StockData/FOXA.csv", "Fox")
            newTrader.addStock("StockData/INTC.csv", "Intel")
            newTrader.addStock("StockData/MSFT.csv", "Microsoft")
            newTrader.addStock("StockData/MU.csv", "Micron")
            newTrader.addStock("StockData/NFLX.csv", "Netflix")
            newTrader.addStock("StockData/NVDA.csv", "Nividia")
            self.traders.append(newTrader)

    #Used for all generations after the 1st. Takes in a trader to base mutations off
    def newGeneration(self, mutationrate, fitTrader):
        #Mutation rate is a percentage
        self.traders = []
        for x in range(self.population):
            cutlosses = 0
            getprofit = 0
            minimumM = 0
            risk = 0
            MA15Lead = 0
            MA30Lead = 0

            #Each trader either keeps a trait or mutates a new one depending on the mutation rate
            if random.randrange(1, 100) > mutationrate:
                cutlosses = fitTrader.cutlosses
            else:
                cutlosses = float(random.randrange(85, 99)) / 100
            if random.randrange(1, 100) > mutationrate:
                getprofit = fitTrader.getprofit
            else:
                getprofit = float(random.randrange(101, 111)) / 100
            if random.randrange(1, 100) > mutationrate:
                minimumM = fitTrader.minimumM
            else:
                minimumM = float((random.randrange(-200, 300, 5))) / 100
            if random.randrange(1, 100) > mutationrate:
                risk = fitTrader.risk
            else:
                risk = random.randrange(7,20,1)
            if random.randrange(1, 100) > mutationrate:
                MA15Lead = fitTrader.MA15Lead
            else:
                MA15Lead = float((random.randrange(-200, 300, 5))) / 100
            if random.randrange(1, 100) > mutationrate:
                MA30Lead = fitTrader.MA30Lead
            else:
                MA30Lead = float((random.randrange(-200, 300, 5))) / 100

            
            newTrader = Trader(self.balance, self.fees, cutlosses, getprofit, minimumM, risk, MA15Lead, MA30Lead)
            newTrader.addStock("StockData/AAPL.csv", "Apple")
            newTrader.addStock("StockData/ATVI.csv", "Activision")
            newTrader.addStock("StockData/FB.csv", "Facebook")
            newTrader.addStock("StockData/CSCO.csv", "Cisco")
            newTrader.addStock("StockData/FOXA.csv", "Fox")
            newTrader.addStock("StockData/INTC.csv", "Intel")
            newTrader.addStock("StockData/MSFT.csv", "Microsoft")
            newTrader.addStock("StockData/MU.csv", "Micron")
            newTrader.addStock("StockData/NFLX.csv", "Netflix")
            newTrader.addStock("StockData/NVDA.csv", "Nividia")
            self.traders.append(newTrader)
        

    #Simulates a full trade year for all traders
    def tradeYear(self):
        print "Simulating generation #%s..." % (self.generationNumber)
        count = 1
        for trader in self.traders:
            for x in range(245):
                trader.nextDay()
            trader.getOut()
            print "Trader #%s finished with a balance of %s" % (count, trader.broker.balance)
            count += 1
        print "Most fit trader of this generation is had a balance of: $%s\n" % (self.mostFitTrader().broker.balance)
            
    #Returns the trader that made the most profit
    def mostFitTrader(self):
        profits = []
        mostFit = Trader(0, 0, 0, 0, 0, 0, 0, 0)
        #Best trader that made at least 5 trades
        for trader in self.traders:
            if (trader.broker.balance > mostFit.broker.balance) and (trader.broker.tradesPerformed > 5):
                mostFit = trader
        #If no trader made 5 trades, lower criteria to one trade
        if mostFit == Trader(0, 0, 0, 0, 0, 0, 0, 0):
            for trader in self.traders:
                if (trader.broker.balance > mostFit.broker.balance) and (trader.broker.tradesPerformed != 0):
                    mostFit = trader
        return mostFit

    def evolveCycle(self, mutationrate):
        #Mutation rate is a percentage
        self.generationNumber += 1
        self.newGeneration(mutationrate, self.mostFitTrader())
        self.tradeYear()
        
        
        
            
            
            
            
        
        
        
