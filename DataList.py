import csv
from DataPoint import DataPoint

class DataList:
    'Groups many Data Points together, where functions can be performed'

    def __init__(self, fileLocation, name):
        self.stockCount = 0
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
        self.stockCost = self.DataPoints[0].close
    def __getitem__(self, key):
        return self.DataPoints[key]

    def setDay(self, x):
        self.stockCost = self.DataPoints[x].close
