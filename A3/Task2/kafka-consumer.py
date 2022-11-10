from kafka import KafkaConsumer
import sys
from json import dumps, loads

tn = sys.argv[1]
consumer = KafkaConsumer(tn, bootstrap_servers=[
                         'localhost:9092'], value_deserializer=lambda x: loads(x.decode('utf-8')))
main = dict()
try:
    for message in consumer:
        msg = message.value
        (key, value), = msg.items()
        m = dict()
        d = {"Min": value[0], "Max": value[1]}
        m[key] = d
        obj = dumps(m)
        print(obj)
        # print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,message.offset, message.key,message.value))
    # print(main)
    # obj=json.dumps(main)
    # print(obj)
except KeyboardInterrupt:
    sys.exit()
