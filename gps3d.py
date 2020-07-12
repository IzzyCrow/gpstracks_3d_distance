# i want to try to manually record the total distance of a gps track from a gps 
# taking into account elevation.  The datafile will be a text file genrated from
# Minnesota dnrGarmin Program (version 6.1.0.6 ) -  https://www.dnr.state.mn.us/mis/gis/DNRGPS/DNRGPS.html


import csv
import decimal
import geopy
import os
import sys
from bs4 import BeautifulSoup
from datetime import datetime, timezone
from dateutil import tz
from decimal import Decimal

class myTrackPoint:
    def __init__(self,lat,ylong,ele,utcd,locald,temp):
        # self.name = name
        # self.age = age
        self.longtitude = ylong
        self.latitude = lat
        self.elevation = ele
        self.gpstime = utcd
        self.localtime = locald
        self.temperature = temp
        self.model = 'Garmin GPSMAP 64sx' 




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
    
    x = myTrackPoint(latitude, longitude, elevation,utc,createLocalTimeObject(utc), temp)
    return x
    
    print('Lat: ' + str(latitude) + ' | Longitude = ' + str(longitude) + ' | Elevation = ' + str(elevation) + ' | Date = ' + utc.strftime ('%d-%b-%Y %H:%M:%S') + ' | ' + createLocalTimeObject(utc).strftime ('%d-%b-%Y %H:%M:%S') + '| Temperature = ' + str(temp))


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
        distinctTrackPoint = parseGPXLine(str(trackPoints[i].get_text))
        print('Model: ' + distinctTrackPoint.model)
        print('Latitude: ' + str(distinctTrackPoint.latitude))
        print('Longitude: ' + str(distinctTrackPoint.longtitude))
        print('Elevation: ' + str(distinctTrackPoint.elevation))
        print('GPS Time: ' + distinctTrackPoint.gpstime.strftime ('%d-%b-%Y %H:%M:%S'))
        print('Local Time: ' + distinctTrackPoint.localtime.strftime ('%d-%b-%Y %H:%M:%S'))
        if distinctTrackPoint.temperature != None:
            print('Temperature (f): ' + str(round(distinctTrackPoint.temperature,2)))
        else:
            print ('Temperature (f): N/A')
        print('---------------------------------------')

def createLocalTimeObject(utcDate):
    return utcDate.astimezone(tz.gettz())

def createUTCTimeObject(xTime,xDate):
    year = int(xDate[0:4])
    month = int(xDate[5:7])
    day = int(xDate[8:])
    hour = int(xTime[0:2])
    minute = int(xTime[3:5])
    second = int(xTime[6:])

    return datetime(year, month, day, hour, minute, second, 0, tzinfo=timezone.utc)

    
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


