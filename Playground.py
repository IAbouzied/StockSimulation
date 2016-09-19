from Trader import Trader

gary = Trader(10000, 15, .90, 1.05, -1, 10, 0.5, 0.5)
gary.addStock("AAPL.csv", "Apple")
gary.addStock("ATVI.csv", "Activision")
gary.addStock("FB.csv", "Facebook")
gary.addStock("CSCO.csv", "Cisco")
gary.addStock("FOXA.csv", "Fox")
gary.addStock("INTC.csv", "Intel")
gary.addStock("MSFT.csv", "Microsoft")
gary.addStock("MU.csv", "Micron")
gary.addStock("NFLX.csv", "Netflix")
gary.addStock("NVDA.csv", "Nividia")

for x in range(245):
    gary.nextDay()

gary.getOut()
