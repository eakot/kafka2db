from kafka import KafkaConsumer

def run_listener(bootstrap_server, topic):
    consumer = KafkaConsumer(topic, bootstrap_servers=bootstrap_server)
    for msg in consumer:
         print (msg)