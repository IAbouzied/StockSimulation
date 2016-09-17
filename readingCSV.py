import csv
from DataPoint import DataPoint

#Setting up the file from which the data will come
AAPL = open("AAPL.csv")
csv_AAPL = csv.reader(AAPL)

#Forming the list of data points
AAPLDataPoints = []
for row in csv_AAPL:
    theName = "Apple"
    theDate = row[0]
    theOpen = row[1]
    theHigh = row[2]
    theLow = row[3]
    theClose = row[4]
    theVolume = row[5]
    AAPLDataPoints.append(DataPoint(theName, theDate, theOpen, theHigh, theLow, theClose, theVolume))
    
print AAPLDataPoints[5]    
        
