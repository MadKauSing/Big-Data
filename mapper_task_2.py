#!/usr/bin/env python3
import json
import sys
import math

# command line arguments
d = float(sys.argv[1])
lat = float(sys.argv[2])
lon = float(sys.argv[3])


def check_constraints(data):
    if data["humidity"] > 48 and data["humidity"] < 54:
        if data["temperature"] > 20 and data["temperature"] < 24:
            return 1
    return 0


def check_distance(data):
    dist = math.sqrt((lat - data["lat"])**2 + (lon - data["lon"])**2)
    if dist < d:
        return 1
    return 0


for line in sys.stdin:
    try:
        data = json.loads(line)
        # print(data)

        if check_constraints(data):
            if check_distance(data):
                print(data['timestamp'],1)
    except:
        pass
