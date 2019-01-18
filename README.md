# Python Kafka Boilerplate

Python Kafka Consuming and Producing to Kafka topic

## Environment Setup

Follow the instructions below to configure your local machine to run and develop this example Python application.

_Note:_ The instructions are focused on MacOsx however other environments will be supported with a bit of googling.

### Local Docker Environment
The example code relies on a running Kafka service, the repo contains a Docker compose file that will spin up a configured Kafka.

* Install Docker Toolbox - [Instructions](https://www.docker.com/products/docker-toolbox)

* Run the docker environment `docker-compose up`

This will launch a kafka service listening on port `9092` initialised with a Topic called `messages`

### Build dependencies

* Python 2.7.14
* `$ pip install -r requirements.txt`

### Configure and Run
* `$ python kafka-example`

### Note
* [Kafka](https://github.com/wurstmeister/kafka-docker) and [Zookeeper](https://github.com/wurstmeister/zookeeper-docker) Images. 
* Modify the KAFKA_ADVERTISED_HOST_NAME in docker-compose.yml to match your docker host IP (Note: Do not use localhost or 127.0.0.1 as the host ip if you want to run __multiple__ brokers.)

