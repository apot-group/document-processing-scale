# necessary import 
from pyspark.sql import SparkSession
from pyspark.ml.image import ImageSchema
from pyspark.sql.functions import lit
from functools import reduce
from pyspark.sql.types import *
from pyspark.sql.functions import *
from pyspark import SparkFiles


spark  = SparkSession.builder.master("spark://spark-master:7077").getOrCreate()
# spark.conf.set("spark.shuffle.blockTransferService", "nio")
print(spark)


sc = spark.sparkContext
print(sc)

df = spark \
  .readStream \
  .format("kafka") \
  .option("kafka.bootstrap.servers", "kafka:9092") \
  .option("subscribe", "kafka-sample") \
  .load()
df.selectExpr("CAST(key AS STRING)", "CAST(value AS STRING)")

print(df)


# textFile = spark.read.text("/opt/spark-data/README.md")

# print("HEEEEEERRRR", textFile.count())