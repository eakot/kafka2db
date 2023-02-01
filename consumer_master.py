#habr.com/ru/company/neoflex/blog/674944/ + GPT

#Import the necessary libraries
from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql.functions import *
import os
import sys
import json
from pyspark.sql import functions as F 

#Create a spark session
spark = (SparkSession
	    .builder
		.config("spark.jars", "/-/-/-/postgresql-42.5.1.jar")
		.appName('streaming-kafka')
	    .getOrCreate())

#Read the data from Kafka topic
kafka_df = (spark
    	.readStream
    	.format('kafka')
    	.option('kafka.bootstrap.servers', 'kafka:9092')
    	.option('subscribe','testtopic')
    	.option("startingOffsets", "earliest")
    	.load())

#Создание схемы для JSON
schema = StructType([
    	StructField("title", StringType(),True),
    	StructField("years", IntegerType(),True),
    	StructField("casted", StringType(),True),
    	StructField("genres", StringType(),True)])

#Parse the JSON data from Kafka message to create a dataframe  
json_df =kafka_df.selectExpr("CAST(value AS STRING)").select(from_json(col("value"),schema).alias("data"))
json_df=json_df.select('data.*')
json_df=json_df.withColumn('timestamp',F.current_timestamp())
print(json_df)

#Write to Postgres
def writeToPostgres(json_df, epoch_id):
	json_df.write \
		.format('jdbc') \
		.option('url', 'jdbc:postgresql://-.-.-.-:5432/-') \
		.option("driver", "org.postgresql.Driver") \
		.option('dbtable', '-."-"') \
		.option('user', '-') \
		.option('password', '-') \
		.mode('append') \
		.save()

query = json_df.writeStream \
	    .foreachBatch(writeToPostgres) \
		.trigger(processingTime='10 seconds') \
		.start()

query.awaitTermination()