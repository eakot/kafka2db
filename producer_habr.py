#habr.com/ru/post/451160

from numpy.random import choice, randint

def get_random_value():
	new_dict = {}

	branch_list = ['Kazan', 'SPB', 'Novosibirsk', 'Surgut']
	currency_list = ['RUB', 'USD', 'EUR', 'GBP']

	new_dict['branch'] = choice(branch_list)
	new_dict['currency'] = choice(currency_list)
	new_dict['amount'] = randint(-100, 100)

	return new_dict

from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers=['localhost:9093'], api_version=(2,7,0), value_serializer=lambda x:dumps(x).encode('utf-8'), compression_type='gzip')

my_topic = 'testtopic2'

data = get_random_value()

try:
	future = producer.send(topic = my_topic, value = data)
	record_metadata = future.get(timeout=10)

	print('--> The message has been sent to topic: \
		{}, partition: {}, offset: {}' \
		.format(record_metadata.topic,
		    record_metadata.partition,
		    record_metadata.offset))

except Exception as e:
	print('--> It seems an Error occured: {}'.format(e))

finally:
	producer.flush()