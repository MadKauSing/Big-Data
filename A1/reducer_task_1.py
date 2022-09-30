#!/usr/bin/env python3
import sys
dictionary = {}
keys = []
for line in sys.stdin:

    # faster lookups
    try:
        (word, values) = line.split()
        value = int(values.strip())

        if word not in dictionary.keys():
            dictionary[word] = value
        else:
            dictionary[word] = dictionary[word]+value
    except:
        pass
for date in dictionary:
  print(date,dictionary[date])
