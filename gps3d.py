# i want to try to manually record the total distance of a gps track from a gps 
# taking into account elevation.  The datafile will be a text file genrated from
# Minnesota dnrGarmin Progmram (version 6.1.0.6 ) -  https://www.dnr.state.mn.us/mis/gis/DNRGPS/DNRGPS.html

import csv
import geopy
import os
import sys

def loadCSV2List (textFile):
    csvList = []
    with open(textFile, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar=None)
        for row in spamreader:
            # print(', '.join(row))
            # print(row)
            csvList.append(', '.join(row))

    return csvList

def generateCommaindxes(record):
    rawList = []
    filteredList = []
    counter = 0
    for elem in record:
        if elem == ',':
            rawList.append(counter)
        
        counter += 1
    
    
    filteredList.append(rawList[3])
    filteredList.append(rawList[4])
    filteredList.append(rawList[5])
    filteredList.append(rawList[12])
    filteredList.append(rawList[13])
    return filteredList



gpsList = loadCSV2List('testdata.csv')
for record in gpsList:
    commaLocations = generateCommaindxes(record)
    print('Lat: ' + record[commaLocations[0] + 1:commaLocations[1]-1] + ', Long: ' + record[commaLocations[1] + 1:commaLocations[2]-1] + ', Altitude : ' + record[commaLocations[3] + 1:commaLocations[4]])
    


# my goal
# take each line, get teh index of each comma then pass that data to a list where i can use the index numbers of commas i need ot read the csv
# so record [indexlist(3):indexlist(6)] = lat