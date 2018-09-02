import csv
from DataPoint import DataPoint

class DataList:
    'Groups many Data Points together, iterates through the days and compiles technical data'

    def __init__(self, fileLocation, name):
        #Owned Shares
        self.stockCount = 0
        self.amountSpent = 0

        self.day = 0

        #For prividing data on most recent days
        self.last90 = []

        #Moving averages
        self.MA15 = 0
        self.MA30 = 0
        self.MA90 = 0

        #Volumes
        self.last15V = []

        #Momentum
        self.momentum = 0
        self.volumeMomentum = 0

        #Reading the data from the CSV File
        theCSV = open(fileLocation)
        theReader = csv.reader(theCSV)
        self.DataPoints = []
        for row in theReader:
            name = name
            date = row[0]
            openPrice = row[1]
            high = row[2]
            low = row[3]
            close = row[4]
            volume = row[5]
            self.DataPoints.append(DataPoint(name, date, openPrice, high, low, close, volume))
        self.DataPoints.reverse()

        #Initial conditions
        self.stockCost = self.DataPoints[self.day].close
        self.volume = self.DataPoints[self.day].volume

        self.last15V.append(self.volume)
        self.last90.append(self.stockCost)
        self.stockValue = self.stockCost * self.stockCount

    def __getitem__(self, key):
        return self.DataPoints[key]

    def nextDay(self):
        #Incrementing to most recent data
        self.day += 1
        self.stockCost = self.DataPoints[self.day].close
        self.stockValue = self.stockCost * self.stockCount
        self.volume = self.DataPoints[self.day].volume

        #Update list of most recent days
        self.last90.append(self.stockCost)
        self.last15V.append(self.volume)
        if len(self.last90) > 90:
                self.last90.pop(0)
        if len(self.last15V) > 15:
                self.last15V.pop(0)

        #Update Moving averages
        self.MA90 = sum(self.last90) / len(self.last90)
        last30 = self.last90[len(self.last90)-30:len(self.last90)]
        last15 = self.last90[len(self.last90)-15:len(self.last90)]
        self.MA30 = sum(last30) / len(last30)
        self.MA15 = sum(last15) / len(last15)

        #Calculating price momentum
        last10 = last15[-10:]
        differences = []
        for x in last10:
            if last10.index(x) == 0:
                lastx = x
            else:
                lastx = last10[last10.index(x) - 1]
            differences.append(x - lastx)
            if differences[0] == 0:
                differences.pop(0)
            else:
                self.momentum = sum(differences) / len(differences)

        #Calculating volume momentum
        last10V = self.last15V[-10:]
        differencesV = []
        for x in last10V:
            if last10V.index(x) == 0:
                lastx = x
            else:
                lastx = last10V[last10V.index(x) - 1]
            differencesV.append(x - lastx)
            if differencesV[0] == 0:
                differencesV.pop(0)
            else:
                self.volumeMomentum = sum(differencesV) / len(differencesV)
        
        
            
        
        
