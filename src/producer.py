from datetime import datetime
from time import sleep
from json import dumps
from kafka import KafkaProducer
from loguru import logger
from .model.message import Message


def run_infinite_generator(bootstrap_server, topic):
    logger.info("Producer infinite generation. Bootstrap server: {}".format(bootstrap_server))
   
    logger.info("Producer infinite generation. Bootstrap server: {}".format(bootstrap_server))
    producer = KafkaProducer(
        bootstrap_servers=bootstrap_server,
        value_serializer=lambda x: dumps(x).encode('utf-8')
    )

    j = 0
    while True:
        new_event = Message(id=j)
        new_event.event_ts = datetime.now()
        data = new_event.json()

        logger.debug("Message {}".format(data))

        producer.send(topic, value=data)
        j += 1
        sleep(0.5)
