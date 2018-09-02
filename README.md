# StockSimulation
This project parses stock data from CSV files to be used in trading algorithms. These algorithms use a genetic algorithm in which "Traders" use randomized criteria to initiate buy/sell offers. The highest performer is then taken as the base model for the next generation of traders. After many generations, what started as random criteria will converge to the most optimal trading practices over the historical data of the stocks selected.

## The Files
**DataPoint.py** and **DataList.py**: This is where the data from the CSV files is parsed into useful datapoints, each one representing a single trading day. As the DataList runs through each trading day, it will track useful technical indicators such as moving averages and volume momentum.

**StockBroker.py**: This is a platform where trades can be initiated. Commands can be issued to buy/sell a stock, and iterate to the next trade day.

**Trader.py**: This is where the decision on whether to buy or sell a stock occurs. Each Trader uses a StockBroker to initiate trades. The Trader makes the decisions based on a few different parameters, such as risk tolerance, when to cash in profits, and tracking moving averages. To change how the Trader makes these decisions, a good place to start is the **think()** function.

**Evolution.py**: This class creates a _population_ of traders that are fed randomized parameters for their trading decisions. A trading cycle is simulated for each of the traders. The most effects trader can be used as a starting point for the next population of traders, and will be modified according to the designated mutation rate. 

**Playground.py**: This file need not be included. It demonstrates an evolution cycle of traders.

**StockData/**: This folder holds some CSV files to use in the project.

## How to get the CSV files
This project parses CSV files offered by the Yahoo Finance platform. For each trading day, it offers the following data points:
Date, Open Price, High Price, Low Price, Closing Price, Adjusted Closing Price, and Volume. **The parsing is based on the included csv files from when Yahoo Finance ordered these data points slightly differently.** Any new csv files will require minor adjustments on the variable ordering.

**To download a CSV File**:
1. Go to the page of the desired stock on the Yahoo Finance site.
2. Click on "Historical Data".
3. Select the desired time period.
4. Set the frequency to "Daily".
5. Click on "Download Data".

## Demo
This is a population of 7 traders undergoing 3 evolution cycles with a starting balance of $10,000, and a $10 fee per trade.
```
Simulating generation #1...
Trader #1 finished with a balance of 9929.820012 with 2 trades
Trader #2 finished with a balance of 9878.559992 with 7 trades
Trader #3 finished with a balance of 10072.730013 with 6 trades
Trader #4 finished with a balance of 10000 with 0 trades
Trader #5 finished with a balance of 9271.400005 with 44 trades
Trader #6 finished with a balance of 7632.329909 with 119 trades
Trader #7 finished with a balance of 8610.779621 with 46 trades
Most fit trader of this generation is had a balance of: $10072.730013

Simulating generation #2...
Trader #1 finished with a balance of 9922.180083 with 6 trades
Trader #2 finished with a balance of 10039.199941 with 5 trades
Trader #3 finished with a balance of 10072.730013 with 6 trades
Trader #4 finished with a balance of 10072.730013 with 6 trades
Trader #5 finished with a balance of 9906.860078 with 5 trades
Trader #6 finished with a balance of 10072.730013 with 6 trades
Trader #7 finished with a balance of 10000 with 0 trades
Most fit trader of this generation is had a balance of: $10072.730013

Simulating generation #3...
Trader #1 finished with a balance of 10072.730013 with 6 trades
Trader #2 finished with a balance of 9892.480024 with 6 trades
Trader #3 finished with a balance of 9580.790046 with 33 trades
Trader #4 finished with a balance of 10041.419931 with 3 trades
Trader #5 finished with a balance of 10137.929991 with 5 trades
Trader #6 finished with a balance of 10072.730013 with 6 trades
Trader #7 finished with a balance of 9919.92001 with 6 trades
Most fit trader of this generation is had a balance of: $10072.730013

Simulating generation #4...
Trader #1 finished with a balance of 9580.790046 with 33 trades
Trader #2 finished with a balance of 10072.730013 with 6 trades
Trader #3 finished with a balance of 10045.659979 with 1 trades
Trader #4 finished with a balance of 9893.100081 with 6 trades
Trader #5 finished with a balance of 10039.760072 with 1 trades
Trader #6 finished with a balance of 9892.96002 with 6 trades
Trader #7 finished with a balance of 10099.96991 with 6 trades
Most fit trader of this generation is had a balance of: $10099.96991
```
