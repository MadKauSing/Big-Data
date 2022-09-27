#!/usr/bin/env python3
import sys

print_function=print

for line in sys.stdin:
    try:

        temp=line.split()
        if temp[0]!='#':
            source,dest=temp
            source=int(source)
            dest=dest.strip()
            print_function(source,dest)
    except:
        pass
