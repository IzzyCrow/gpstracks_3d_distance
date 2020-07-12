# i want to try to manually record the total distance of a gps track from a gps 
# taking into account elevation.  The datafile will be a text file genrated from
# Minnesota dnrGarmin Progmram (version 6.1.0.6 ) -  https://www.dnr.state.mn.us/mis/gis/DNRGPS/DNRGPS.html


import csv
import decimal
import geopy
import os
import sys

from bs4 import BeautifulSoup
from datetime import datetime, timezone
from decimal import Decimal

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

def parseGPXLine(record):
    # <bound method Tag.get_text of <trkpt lat="37.8150756843" lon="-122.2536893003"><ele>27.15</ele><time>2020-07-11T18:49:59Z</time><extensions><gpxtpx:TrackPointExtension><gpxtpx:atemp>23.6</gpxtpx:atemp></gpxtpx:TrackPointExtension></extensions></trkpt>>
    # <trkpt lat="37.8150304221" lon="-122.2539115045"><ele>28.96</ele><time>2020-07-11T23:39:41Z</time></trkpt>
    trackPoint = []
    latitude = Decimal(record[42:55])
    longitude = Decimal(record[62:77])
    elevation = Decimal(record[84:89])
    utcDate =  record[101:111]
    utcTime = record [112:120]
    utc = createUTCTimeObject(utcTime,utcDate)
    if len(record) == 252:
        temp = (Decimal((record[182:186])) * Decimal(9.0/5.0)) + 32 
    else:
        temp = None
    
    # temp = record[182:186]
    
    # temp1 = Decimal(9.0/5.0)

    # temperature = (temp * temp1) + 32
    # * (9/5)) + 32.0 
    # temp = record[84:88]
# print today.strftime('We are the %d, %b %Y')
    # print('Lat: ' + str(latitude) + ' | Longitude = ' + str(longitude) + ' | Elevation = ' + str(elevation) + ' | Date = ' + utcDate + ' | Time = ' + utcTime + ' | Temperature = ' + str(temp))
    print('Lat: ' + str(latitude) + ' | Longitude = ' + str(longitude) + ' | Elevation = ' + str(elevation) + ' | Date = ' + utc.strftime ('%d-%b-%Y %H:%M:%S') + '| Temperature = ' + str(temp))



def readGPX(targetGPX):
    gpx = open(targetGPX,'r')
    contents = gpx.read()
    soup = BeautifulSoup(contents,'xml')
    trackPoints = soup.find_all('trkpt')
    time = soup.find_all('time')
    elevation = soup.find_all('ele')
    temp = soup.find_all('gpxtpx:atemp')
    for i in range(0, len(trackPoints)):
        # print (str(trackPoints[i].get_text) + ' | ' + str(len(str(trackPoints[i].get_text))))
        parseGPXLine(str(trackPoints[i].get_text))
        # print (time[i].get_text)
        # print (elevation[i].get_text)
        # print (temp[i].get_text)

def createUTCTimeObject(xTime,xDate):
    year = int(xDate[0:4])
    month = int(xDate[5:7])
    day = int(xDate[8:])
    hour = int(xTime[0:2])
    minute = int(xTime[3:5])
    second = int(xTime[6:])

    return datetime(year, month, day, hour, day, second, 0, tzinfo=timezone.utc)

    # print(year + ' ' + month + ' ' + day + ' | ' + hour + ':' + minute + ':' + second)

    # infile = open("books.xml","r")
    # contents = infile.read()
    # soup = BeautifulSoup(contents,'xml')
    # titles = soup.find_all('title')
    # authors = soup.find_all('author')
    # prices = soup.find_all('price')
    # for i in range(0, len(titles)):
    #     print(titles[i].get_text(),"by",end=' ')
    #     print(authors[i].get_text(),end=' ')
    #     print("costs $" + prices[i].get_text())

    
    # filteredList.append(rawList[3])
    # filteredList.append(rawList[4])
    # filteredList.append(rawList[5])
    # filteredList.append(rawList[12])
    # filteredList.append(rawList[13])
    # return filteredList



# gpsList = loadCSV2List('testdata.csv')
# for record in gpsList:
#     commaLocations = generateCommaindxes(record)
#     # print('Lat: ' + record[commaLocations[0] + 1:commaLocations[1]-1] + ', Long: ' + record[commaLocations[1] + 1:commaLocations[2]-1] + ', Altitude : ' + record[commaLocations[3] + 1:commaLocations[4]])
#     latitude = Decimal(record[commaLocations[0] + 1:commaLocations[1]-1])
#     longitude = Decimal(record[commaLocations[1] + 1:commaLocations[2]-1])
#     altitude = Decimal(record[commaLocations[3] + 1:commaLocations[4]])
    

readGPX('Track_NEW.gpx')


# my goal
# take each line, get teh index of each comma then pass that data to a list where i can use the index numbers of commas i need ot read the csv
# so record [indexlist(3):indexlist(6)] = lat


