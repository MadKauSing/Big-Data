import sys
from time import sleep
from json import dumps
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='localhost:9092',
                         value_serializer=lambda x: dumps(x).encode('utf-8'))
tn = sys.argv[1]
# for _ in range(100):
#    producer.send('foobar', b'some_message_bytes')
for line in sys.stdin:
    # print(file)
    l = line.strip().split(',')
    if l[0] != "EOF":
        d = {l[0]: [l[6], l[7]]}
        ack = producer.send(tn, value=d)
        meta = ack.get()
        print(meta.topic)
        print(meta.partition)
        print("sent to consumer")
