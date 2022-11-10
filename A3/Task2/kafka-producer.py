import sys
from time import sleep
from json import dumps
from kafka import KafkaProducer
import csv

producer = KafkaProducer(bootstrap_servers='localhost:9092',
                         value_serializer=lambda x: dumps(x).encode('utf-8'))
tn = sys.argv[1]
main = dict()
# for _ in range(100):
#    producer.send('foobar', b'some_message_bytes')
for line in sys.stdin:
    # print(file)
    l = list(csv.reader([line]))[0]
    # print(l)
    if l[0] == "EOF":
        for key in sorted(main.keys()):
            ack = producer.send(tn, value={key: [main[key][0], main[key][1]]})
            meta = ack.get()
        ack = producer.send(tn, value={"msg": "End of transmission"})
        meta = ack.get()
    else:
        d = [float(l[6]), float(l[7]), 1]
        if l[0] not in main.keys():
            main[l[0]] = d
        else:
            count = main[l[0]][2]
            new_val = [round((((main[l[0]][0]*count)+d[0])/(count+1)), 2),
                       round((((main[l[0]][1]*count)+d[1])/(count+1)), 2), count+1]
            main.update({l[0]: new_val})

# for key,value in main.items():
#    new_val=[value[0],value[1]]
#    ack=producer.send(tn,value={key:new_val})
#    meta=ack.get()
