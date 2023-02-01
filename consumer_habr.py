#habr.com/ru/company/neoflex/blog/674944/

def main():
    from pyspark.sql import SparkSession

    spark = (SparkSession
	    	.builder
	    	.appName('streaming-kafka')
            #.config('spark.jars.packages', 'org.apache.spark:spark-sql-kafka-0-10_2.12:3.2.0')
	    	.getOrCreate())
    #spark.sparkContext.setLogLevel('WARN')

    source = (spark
    		.readStream
    		.format('kafka')
    	    .option('kafka.bootstrap.servers', 'kafka:9092')
    		.option('subscribe','testtopic').
            .option("startingOffsets", "earliest")
    		.load())
    source.printSchema()

    df = (source.selectExpr('CAST(value AS STRING)', 'offset'))

    console = (df
           .writeStream
           .format('console')
           .queryName('console output'))

    query = (df
            .writeStream
            .format('kafka')
            .queryName('kafka-output')
            .option('kafka.bootstrap.servers', 'kafka:9092')
            .option('topic', 'testtopic2')
            .option('checkpointLocation', './.local/checkpoint'))
    console.start()    
    query.start().awaitTermination()

if __name__ == '__main__':
    main()