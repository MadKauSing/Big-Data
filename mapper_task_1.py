#!/usr/bin/env python3
import json
import sys

#just setting max no of records to be read
count=100000

#preloading functions just for speed
json_dict=json.loads


for line in sys.stdin:
  try:
    if count==0: break
    count=count-1
    
    data_dict=json_dict(line)
    #print(data_dict) 
    
    if (data_dict['location']>1700 and data_dict['location']<2500) and data_dict['sensor_id']< 5000 and data_dict['pressure']>=93500.00 and data_dict['humidity']>= 72.00 and data_dict['temperature'] >=12.00:
      print(data_dict['timestamp'],1)
  except:
    #I removed the exception cuz it would lead to problems in reducer
    pass