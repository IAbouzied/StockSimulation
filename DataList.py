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
        self.MA15 = 0
        self.MA30 = 0
        self.MA90 = 0
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
        self.last90.append(self.stockCost)

    def __getitem__(self, key):
        return self.DataPoints[key]

    def nextDay(self):
        self.day += 1
        self.stockCost = self.DataPoints[self.day].close
        self.last90.append(self.stockCost)
        self.last30.append(self.stockCost)
        self.last15.append(self.stockCost)
        if len(self.last90) > 90:
                self.last90.pop(0)
        if len(self.last30) > 30:
                self.last90.pop(0)
        if len(self.last15) > 15:
                self.last15.pop(0)
        self.MA90 = sum(self.last90) / len(self.last90)
        self.MA30 = sum(self.last30) / len(self.last30)
        self.MA15 = sum(self.last15) / len(self.last15)
        
        
