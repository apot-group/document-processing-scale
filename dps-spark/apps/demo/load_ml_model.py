# necessary import spark
from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql.functions import *


TOPIC = 'kafka-sample'
KAFKA_SERVER='kafka:9092'

SPARK_SERVER="spark://spark-master:7077"
spark_session  = SparkSession.builder.master(SPARK_SERVER).getOrCreate()
spark_context = spark_session.sparkContext

df = spark_session \
  .readStream \
  .format("kafka") \
  .option("kafka.bootstrap.servers", KAFKA_SERVER) \
  .option("subscribe", TOPIC) \
  .load()
df.selectExpr("CAST(key AS STRING)", "CAST(value AS STRING)")

df_json = df.selectExpr('CAST(value AS STRING) as json')

schema = StructType([StructField('data', StringType())])

print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
df_json.select(from_json(df_json.json, schema).alias('raw_data')) \
  .select('raw_data.data') \
  .writeStream \
  .trigger(once=True) \
  .format("console") \
  .start() \
  .awaitTermination()
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")



# textFile = spark.read.text("/opt/spark-data/README.md")

# print("HEEEEEERRRR", textFile.count()