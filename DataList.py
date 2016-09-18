import csv
from DataPoint import DataPoint

class DataList:
    'Groups many Data Points together, where functions can be performed'

    def __init__(self, fileLocation, name):
        self.stockCount = 0
        self.day = 0
        self.last90 = []
        self.last30 = []
        self.last15 = []
        self.last15V = []
        self.MA15 = 0
        self.MA30 = 0
        self.MA90 = 0
        self.momentum = 0
        self.volumeMomentum = 0
        theCSV = open(fileLocation)
        theReader = csv.reader(theCSV)
        self.DataPoints = []
        for row in theReader:
            theName = name
            theDate = row[0]
            theOpen = row[1]
            theHigh = row[2]
            theLow = row[3]
            theClose = row[4]
            theVolume = row[5]
            self.DataPoints.append(DataPoint(theName, theDate, theOpen, theHigh, theLow, theClose, theVolume))
        self.DataPoints.reverse()
        self.stockCost = self.DataPoints[self.day].close
        self.volume = self.DataPoints[self.day].volume
        self.last15V.append(self.volume)
        self.last90.append(self.stockCost)

    def __getitem__(self, key):
        return self.DataPoints[key]

    def nextDay(self):
        self.day += 1
        self.stockCost = self.DataPoints[self.day].close
        self.volume = self.DataPoints[self.day].volume
        self.last90.append(self.stockCost)
        self.last30.append(self.stockCost)
        self.last15.append(self.stockCost)
        self.last15V.append(self.volume)
        if len(self.last90) > 90:
                self.last90.pop(0)
        if len(self.last30) > 30:
                self.last90.pop(0)
        if len(self.last15) > 15:
                self.last15.pop(0)
        if len(self.last15V) > 15:
                self.last15V.pop(0)
        self.MA90 = sum(self.last90) / len(self.last90)
        self.MA30 = sum(self.last30) / len(self.last30)
        self.MA15 = sum(self.last15) / len(self.last15)
        last10 = self.last15[-10:]
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
        
        
            
        
        
