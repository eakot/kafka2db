Список топиков:
sudo docker exec -it c1b26bbbdb04 /opt/bitnami/kafka/bin/kafka-topics.sh --bootstrap-server localhost:9092 --list

Создать топик:
sudo docker exec -it c1b26bbbdb04 /opt/bitnami/kafka/bin/kafka-topics.sh --create --zookeeper zookeeper:2181 --replication-factor 1 --partitions 1 --topic testtopic

Писать в топик:
sudo docker exec -it c1b26bbbdb04 /opt/bitnami/kafka/bin/kafka-console-producer.sh --topic testtopic --bootstrap-server kafka:9092 --broker-list kafka:9092

JSON строка:
{"title":"The Matrix","year":1999,"cast":["Keanu Reevs","Laurence Fishburne"],"genres":["Science Fiction"]}

Читать из топика:
sudo docker exec -it c1b26bbbdb04 /opt/bitnami/kafka/bin/kafka-console-consumer.sh --topic testtopic --from-beginning --bootstrap-server localhost:9092

Открыть Spark Master Web UI:
http://etltest:8079/

Запустить Спарк из докера:
sudo docker exec -it 21d6ddfd677a /bin/bash
bin/spark-shell spark://21d6ddfd677a:7077 - запуск Spark Scala 
spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.2.0 /data/consumer_habr.py - запускается приложение
spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.2.0 --jars /data/postgresql-42.5.1.jar /data/consumer_master.py - запускается приложение

Запустить Producer:
python ....py

Неочевидные моменты:
1. Запуск продьюсера через команду python ....py
2. Необходимость прописать пакеты в сторке запуска приложения на Спарк --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.2.0
3. Необходимость прописать jars и скачать jdbc --jars /data/postgresql-42.5.1.jar
4. Необходимость положить инструкции для запуская Спарк и Кафки в один компоуз, иначе не подключается даже с настройкой сети
5. Сам код примера на Спарке пришлось комбинировать из разных источников, так как не было известно, что нужна схема для json, как пересохранить json и записать в postgres, использование foreachBatch. 
6. В продьюсере прописать api_version?