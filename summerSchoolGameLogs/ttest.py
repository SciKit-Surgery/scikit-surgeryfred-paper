#! /usr/bin/python
import csv

categories = []
scores = []
with open("all_logs.log", mode='r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        timestamp = row[0]
        if timestamp == '2020-07-08 18:45:17':
            print ("Skipping " , timestamp, "there were 22 entries in this log")
            continue 
        if timestamp == '2020-07-08 18:45:43':
            print ("Skipping " , timestamp, "there were 22 entries in this log")
            continue

        categories.append(row[2])
        scores.append(row[3])

print ("read ", len(categories), " entries.")
