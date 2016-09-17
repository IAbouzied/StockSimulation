import csv
from DataPoint import DataPoint

class DataList:
    'Groups many Data Points together, where functions can be performed'

    def __init__(self, fileLocation, name):
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
    def __getitem__(self, key):
        return self.DataPoints[key]
