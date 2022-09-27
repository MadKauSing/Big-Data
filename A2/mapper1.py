


# loading function for optimisation
json_dict = json.loads

for line in sys.stdin:
    try:
        source,dest=line.split()
        dest=dest.strip()
        print(source,dest)
    except:
        pass