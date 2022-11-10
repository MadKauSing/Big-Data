from kafka import KafkaConsumer
import sys
from json import loads

tn = sys.argv[1]
print(tn)
consumer = KafkaConsumer(tn, bootstrap_servers=[
                         'localhost:9092'], value_deserializer=lambda x: loads(x.decode('utf-8')))

try:
    for message in consumer:
        print("%s:%d:%d: key=%s value=%s" % (message.topic,
              message.partition, message.offset, message.key, message.value))
except KeyboardInterrupt:
    sys.exit()
