print("===========================")
print("Step 1: Import Libraries")
print("===========================")

# from pyspark import SparkContext, SparkConf
from pyspark.sql import SQLContext, SparkSession
# from pyspark.ml import Pipeline
# import pandas as pd
import os
# import pickle


os.environ['PYSPARK_SUBMIT_ARGS'] = '--packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.0.2,' \
                                    + 'org.apache.spark:spark-streaming-kafka-0-10_2.12:3.0.2,' \
                                    + 'org.apache.kafka:kafka-clients:3.1.0,org.apache.spark:spark-core_2.12:3.0.2,' \
                                    + 'org.apache.spark:spark-streaming_2.12:3.0.2,' \
                                    + 'org.apache.spark:spark-token-provider-kafka-0-10_2.12:3.0.2,' \
                                    + 'org.apache.hadoop:hadoop-core:1.2.1' \
                                    + ' pyspark-shell'
                                    

print("===========================")
print("Step 2: Start Spark Session")
print("===========================")

TOPIC = 'kafka-sample'
SPARK_SERVER="local"


ss  = SparkSession.builder.master(SPARK_SERVER) \
                  .appName("0747 Pipeline") \
                  .config("spark.executor.memory", "2g") \
                  .config("spark.driver.memory", "2g") \
                  .config("spark.executor.cores", "2") \
                  .config("spark.driver.cores", "2") \
                  .getOrCreate()
                  
sc = ss.sparkContext
sql_c = SQLContext(sc)


print("===========================")
print("Step 3: Load Data")
print("===========================")
columns = ["name", "path"]
data = [("test1.jpg", "/opt/spark-data/test1.jpg"), ("test2.jpg", "/opt/spark-data/test2.jpg")]

rdd = ss.sparkContext.parallelize(data)
df = rdd.toDF(columns)
df.printSchema()
df.show(truncate=False)

