#!/usr/bin/env python
from kafka import KafkaConsumer

class Consumer():
    def __init__(self):
        print "in the Consumer"
        consumer = KafkaConsumer('messages',
                                 bootstrap_servers=['127.0.0.1:9092'],
                                 # auto_offset_reset='earliest',
                                 auto_offset_reset='latest',
                                 enable_auto_commit=True,
                                 auto_commit_interval_ms=1000,
                                )

        # consumer = KafkaConsumer('python-test', group_id='demo-group',
        #                 bootstrap_servers=['localhost:9092'])

        for message in consumer:
            print ("Consumed Msg -> '%s' on Topic -> '%s' with Offset -> %d" %
                    (message.value.decode('utf-8'), message.topic, message.offset))
        consumer.close()
