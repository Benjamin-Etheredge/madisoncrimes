#!/usr/bin/env

import sys
import os, string, shutil, glob, time, datetime, socket

inFileName = "out.txt"
inFile = open(inFileName, 'r')
lines = inFile.readlines()
inFile.close()
caseNo = []
time = []
shift = []
date = []
location = []
incident = []

row = -1
for line in lines:
    words = line.split()
    if len(words) > 0:
        #print(line)
        if line.find('Case') >= 0:
            #print(words)
            row = row + 1
            caseRow = row
            incidents = -1
            for i in range(len(words)):
                #print(words[i].lower())
                if (words[i].lower() == 'no.:'):
                    caseNo.append(words[i+1])
                elif (words[i].lower() == 'time:'):
                    time.append(words[i+1] + words[i+2])
                elif (words[i].lower() == 'shift:'):
                    shift.append(words[i+1])

        elif line.find('Date') >= 0:
            #print(words)
            for i in range(len(words)):
                if (words[i].lower() == 'reported:'):
                    date.append(words[i+1] + words[i + 2] + words[i+3])
                elif (words[i].lower() == 'location:'):
                    pos = line.rfind(':')
                    endPos = len(line)
                    location.append(line[pos + 1:endPos - 1])
        
        elif line.find('Incident') >= 0:
            #print(words)
            pos = line.rfind(':')
            incidents = incidents + 1
            row = row + incidents
            if (caseRow == row):
                incident.append(line[pos + 1:])
            elif (caseRow < row):
                caseNo.append(caseNo[caseRow])
                time.append(time[caseRow])
                shift.append(shift[caseRow])
                date.append(shift[caseRow])
                location.append(location[caseRow])
                incident.append(line[pos + 1:])
                    
#print(row)
#print(caseNo)
outFileName = "madison_crime_record.csv"
outFile = open(outFileName, 'w')
outFile.write("id,case_no,time,shift,date,location,type"+'\n')

for i in range(row):
    outFile.write(str(i) + ',' + caseNo[i] + ',' + time[i] + ',' + shift[i] + ',' + date[i] + ',' + location[i] + ',' + incident[i])
        
outFile.close()