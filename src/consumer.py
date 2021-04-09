from kafka import KafkaConsumer
from json import loads
from loguru import logger
from .model.message import Message
from sqlalchemy import create_engine


class Buffer:
    # Create
    db.execute("CREATE TABLE IF NOT EXISTS films (title text, director text, year text)")
    db.execute("INSERT INTO films (title, director, year) VALUES ('Doctor Strange', 'Scott Derrickson', '2016')")

    def __init__(self, size=10, connection):
        _size = size
        _connection = connection




def get_connection(host, port, login, password, db):
    db_string = "postgres://{login}:{password}@{host}:{port}/{db}".format(host=host, port=port, login=login,
                                                                          password=password, db=db)

    return create_engine(db_string)


def run_listener(bootstrap_server, topic):
    logger.info("Bootstrap server: {}".format(bootstrap_server))

    consumer = KafkaConsumer(
        topic,
        bootstrap_servers=[bootstrap_server],
        auto_offset_reset='latest',
        enable_auto_commit=True,
        value_deserializer=lambda x: loads(x.decode('utf-8')))

    for message in consumer:
        logger.info("Message received: {}".format(Message.parse_raw(message.value)))
