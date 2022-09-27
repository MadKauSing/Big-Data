import sys

for line in sys.stdin:
    try:
        source,dest=line.split()
        dest=dest.strip()
        print(source,dest)
    except:
        pass
