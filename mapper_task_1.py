#!/usr/bin/env python3

import json
import sys
for line in sys.stdin:
  try:
    tweet=json.loads(line)
    tokenset=[x.lower() for x in tweet['analysis']['tokens']['all']]
    tokens=set(tokenset)
    for token in tokens:
      print json.dumps(token.lower()),'\t',1
  except:
    pass