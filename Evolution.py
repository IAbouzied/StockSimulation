from Trader import Trader
import random

class Evolution:
    def __init__(self, population, balance, fees):
        self.balance = balance
        self.fees = fees
        self.traders = []
        self.population = population
        self.firstGeneration()
        self.tradeYear()

    def firstGeneration(self):
        for x in range(self.population):
            cutlosses = float(random.randrange(85, 99)) / 100
            getprofit = float(random.randrange(101, 111)) / 100
            minimumM = float((random.randrange(-200, 300, 5))) / 100
            risk = random.randrange(7,20,1)
            MA15Lead = float((random.randrange(-200, 300, 5))) / 100
            MA30Lead = float((random.randrange(-200, 300, 5))) / 100
            newTrader = Trader(self.balance, self.fees, cutlosses, getprofit, minimumM, risk, MA15Lead, MA30Lead)
            newTrader.addStock("AAPL.csv", "Apple")
            newTrader.addStock("ATVI.csv", "Activision")
            newTrader.addStock("FB.csv", "Facebook")
            newTrader.addStock("CSCO.csv", "Cisco")
            newTrader.addStock("FOXA.csv", "Fox")
            newTrader.addStock("INTC.csv", "Intel")
            newTrader.addStock("MSFT.csv", "Microsoft")
            newTrader.addStock("MU.csv", "Micron")
            newTrader.addStock("NFLX.csv", "Netflix")
            newTrader.addStock("NVDA.csv", "Nividia")
            self.traders.append(newTrader)

    def newGeneration(self, mutationrate, fit):
        self.traders = []
        for x in range(self.population):
            cutlosses = 0
            getprofit = 0
            minimumM = 0
            risk = 0
            MA15Lead = 0
            MA30Lead = 0
            if random.randrange(1, 100) > mutationrate:
                cutlosses = fit.cutlosses
            else:
                cutlosses = float(random.randrange(85, 99)) / 100
            if random.randrange(1, 100) > mutationrate:
                getprofit = fit.getprofit
            else:
                getprofit = float(random.randrange(101, 111)) / 100
            if random.randrange(1, 100) > mutationrate:
                minimumM = fit.minimumM
            else:
                minimumM = float((random.randrange(-200, 300, 5))) / 100
            if random.randrange(1, 100) > mutationrate:
                risk = fit.risk
            else:
                risk = random.randrange(7,20,1)
            if random.randrange(1, 100) > mutationrate:
                MA15Lead = fit.MA15Lead
            else:
                MA15Lead = float((random.randrange(-200, 300, 5))) / 100
            if random.randrange(1, 100) > mutationrate:
                MA30Lead = fit.MA30Lead
            else:
                MA30Lead = float((random.randrange(-200, 300, 5))) / 100
            newTrader = Trader(self.balance, self.fees, cutlosses, getprofit, minimumM, risk, MA15Lead, MA30Lead)
            newTrader.addStock("AAPL.csv", "Apple")
            newTrader.addStock("ATVI.csv", "Activision")
            newTrader.addStock("FB.csv", "Facebook")
            newTrader.addStock("CSCO.csv", "Cisco")
            newTrader.addStock("FOXA.csv", "Fox")
            newTrader.addStock("INTC.csv", "Intel")
            newTrader.addStock("MSFT.csv", "Microsoft")
            newTrader.addStock("MU.csv", "Micron")
            newTrader.addStock("NFLX.csv", "Netflix")
            newTrader.addStock("NVDA.csv", "Nividia")
            self.traders.append(newTrader)
        

    def tradeYear(self):
        for trader in self.traders:
            for x in range(245):
                trader.nextDay()
            trader.getOut()
            

    def fitness(self):
        profits = []
        mostFit = Trader(0, 0, 0, 0, 0, 0, 0, 0)
        for trader in self.traders:
            if (trader.broker.balance > mostFit.broker.balance) and (trader.broker.trades > 5):
                mostFit = trader
        if mostFit == Trader(0, 0, 0, 0, 0, 0, 0, 0):
            for trader in self.traders:
                if (trader.broker.balance > mostFit.broker.balance) and (trader.broker.trades != 0):
                    mostFit = trader
        return mostFit

    def evolveCycle(self, mutationrate):
        self.newGeneration(mutationrate, self.fitness())
        self.tradeYear()
        
        
        
            
            
            
            
        
        
        
