#youtube.com/watch?v=19CZM4aM-8U

import json
import requests
from kafka import KafkaProducer
from time import sleep

producer=KafkaProducer(bootstrap_servers=['kafka:9092'], api_version=(0,10,2), value_serializer=lambda x: json.dumps(x).encode('utf-8'))
for i in range(5):
    res=requests.get('http://api.open-notify.org/iss-now.json')
    data=json.loads(res.content.decode('utf-8'))
    print(data)
    producer.send("testtopic2",value=data)
    sleep(5)
    producer.flush()
    producer.close()