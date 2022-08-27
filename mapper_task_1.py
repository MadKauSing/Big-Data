#!/usr/bin/env python3
import json
import sys

# constraint function


def check_constraints(data):
    if data['location'] > 1700 and data['location'] < 2500:
        if data['sensor_id'] < 5000:
            if data['pressure'] >= 93500.00:
                if data['humidity'] >= 72.00:
                    if data['temperature'] >= 12.00:
                        return 1
    return 0


# loading function for optimisation
json_dict = json.loads

for line in sys.stdin:
    try:
        data = json_dict(line)
        if check_constraints(data):
            print(data['timestamp'], 1)
    except:
        pass
