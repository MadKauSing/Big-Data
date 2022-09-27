import sys

print_function=print

for line in sys.stdin:
    try:
        source,dest=line.split()
        dest=dest.strip()
        print_function(source,dest)
    except:
        pass
