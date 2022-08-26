#!/usr/bin/env python3
import json
import sys


for line in sys.stdin:
    try:
        data = json.loads(line)
        # print(data)

        if((data["humidity"] > 48 and data["humidity"] < 54) and (data["temperature"] > 20 and data["temperature"] < 24)):
            print(f"{data['timestamp']},{data['lat']},{data['lon']},1")
    except:
        pass