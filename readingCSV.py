import csv
from DataPoint import DataPoint

#Setting up the file from which the data will come
AAPL = open("AAPL.csv")
csv_AAPL = csv.reader(AAPL)

#Forming the list of data points
DPs = []
for row in csv_AAPL:
    theName = "Apple"
    theDate = str(row[0])
    theOpen = float(row[1])
    theHigh = float(row[2])
    theLow = float(row[3])
    theClose = float(row[4])
    theVolume = float(row[5])
    print DataPoint.average
    print DataPoint.n
    print theClose
    DPs.append(DataPoint(theName, theDate, theOpen, theHigh, theLow, theClose, theVolume))

#Testing
print DPs[5].name   
        
