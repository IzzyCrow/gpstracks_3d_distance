# i want to try to mannually record the distance 

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
    for elem in record:
        print(elem)



gpsList = loadCSV2List('testdata.csv')
for record in gpsList:
    # print(record)
    


