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

* Python 2.7 
* `$ pip install -r requirements.txt`

### Configure and Run
* `$ python3 kafka-example`

