#!/usr/bin/env python3
import sys
import math

dictionary = {}
keys = []

d = float(sys.argv[1])
lat = float(sys.argv[2])
lon = float(sys.argv[3])

for line in sys.stdin:
    # faster lookups
    try:
        line = line.strip()
        # print(line)
        word, data_lat, data_lon, values = line.rsplit(",")
        # print(word,data_lat,data_lon,values)

        value = int(values.strip())
        dist = math.sqrt((lat - float(data_lat.strip()))**2 + (lon - float(data_lon.strip()))**2)
        if dist < d:
            if word not in dictionary.keys():
                dictionary[word] = value
            else:
                dictionary[word] = dictionary[word]+value
    except Exception as e:
        print(e)
for date in dictionary:
  print(date,dictionary[date])