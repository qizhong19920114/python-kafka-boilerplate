#!/usr/bin/env python
from kafka import KafkaProducer
from time import sleep

class Producer():
	def __init__(self):
		producer = KafkaProducer(bootstrap_servers=['127.0.0.1:9092'], retries=5)
		for e in range(1000):
			producer.send('messages', b'Whiteblock Eth simulation log')
			print("Published msg -> 'super-duper-message' on Topic -> 'messages'")
			sleep(5)

		# block until all async messages are sent
		producer.flush()
		# tidy up the producer connection
		producer.close()
