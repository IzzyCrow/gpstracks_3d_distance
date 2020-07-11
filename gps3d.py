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

gpsList = loadCSV2List('diablo.csv')
for record in gpsList:
    print(record)


