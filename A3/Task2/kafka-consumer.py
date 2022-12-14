from kafka import KafkaConsumer
import sys
from json import dumps, loads

tn = sys.argv[1]
consumer = KafkaConsumer(tn, bootstrap_servers=[
                         'localhost:9092'], value_deserializer=lambda x: loads(x.decode('utf-8')))
main = dict()

for message in consumer:
    msg = message.value
    (key, value), = msg.items()
    m = dict()
    if(msg=={"msg":"End of transmission"}):
        break
    d = {"Min": value[0], "Max": value[1]}
    main[key] = d    
obj=dumps(main)
print(obj)
