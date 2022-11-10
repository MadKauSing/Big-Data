from kafka import KafkaConsumer
import sys
import json

tn = sys.argv[1]
consumer = KafkaConsumer(tn, bootstrap_servers=[
                         'localhost:9092'], value_deserializer=lambda x: json.loads(x.decode('utf-8')))
main = dict()

try:
    for message in consumer:
        msg = message.value
        print(msg)
        if msg == {"msg": "End of trasmission"}:
            print("transaction ended")
            obj = json.dumps(main, indent=3)
            print(obj)
            # break
        (key, value), = msg.items()
        # print(msg)
        m = dict()
        d = {"Min": value[0], "Max": value[1]}
        m[key] = d
        # print(m)
        main[key] = d
        # print(main)
        # obj=dumps(m)
        # print(type(obj))
        # print(obj)
    # print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,message.offset, message.key,message.value))
        # print(main)
except KeyboardInterrupt:
    sys.exit()
