from kafka import KafkaConsumer
import sys
from json import dumps, loads

tn = sys.argv[1]
consumer = KafkaConsumer(tn, bootstrap_servers=[
                         'localhost:9092'], value_deserializer=lambda x: loads(x.decode('utf-8')))
main = dict()
print("{")

for message in consumer:
    msg = message.value
    (key, value), = msg.items()
    m = dict()
    d = {"Min": value[0], "Max": value[1]}
    main[key] = d
    print("""
{
"%s" : {"min" : %f,"max" : %f}
},
""" % (key,value[0],value[1]),end="")
    # obj = dumps(m)
    # print(obj)
    # print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,message.offset, message.key,message.value))
# print(main)
obj=dumps(main)
print(obj)
# print(obj)

print("}")