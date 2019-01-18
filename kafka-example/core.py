from multiprocessing import Process
from kafkaLib import producer as KP
from kafkaLib import consumer as KC

def run_consumer():
    KC.Consumer()

def run():
	p = Process(target=run_consumer)
	p.start()

    # Start the Kafka producer
	KP.Producer()
    # print "run Consumer"
    # # Start the Kafka Consumer
    # KC.Consumer()

	p.join()
