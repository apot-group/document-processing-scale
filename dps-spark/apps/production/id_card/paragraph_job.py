
print("===========================")
print("Step 1: Import Libraries")
print("===========================")

from pyspark import SparkContext, SparkConf
from pyspark.sql import SQLContext, SparkSession
from pyspark.ml import Pipeline
import pandas as pd
import os
import pickle



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
SPARK_SERVER="spark://spark-master:7077"

ss  = SparkSession.builder.master(SPARK_SERVER) \
                  .appName("test") \
                  .config("spark.executor.memory", "6g") \
                  .config("spark.driver.memory", "6g") \
                  .config("spark.executor.cores", "6") \
                  .config("spark.driver.cores", "6") \
                  .getOrCreate()
sc = ss.sparkContext
sql_c = SQLContext(sc)
print(sc)


# print("===========================")
# print("Step 3: Load Model")
# print("===========================")
# # Unpickle, pkl file
# model_paragraph_pkl = sc.binaryFiles("/opt/spart-apps/models/paragraph.pkl")
# model_paragraph_data = model_paragraph_pkl.collect()
# # Load and broadcast python object over spark nodes
# creditcardfrauddetection_model = pickle.loads(model_paragraph_data[0][1])
# broadcast_creditcardfrauddetection_model = sc.broadcast(creditcardfrauddetection_model)
# print(broadcast_creditcardfrauddetection_model.value)


# # Create udf and call predict method on broadcasted model
# def predict(*cols):
#     prediction = broadcast_creditcardfrauddetection_model.value.predict_proba((cols,))
#     return float(prediction[0,1])

# # predict_udf = udf(predict, DoubleType())

# # df = df.withColumn("score", predict_udf(*feature_columns))


print("===========================")
print("Step 3: Load Data")
print("===========================")
columns = ["name", "path"]
data = [("test1.jpg", "/opt/spark-data/test1.jpg"), ("test2.jpg", "/opt/spark-data/test2.jpg")]

rdd = ss.sparkContext.parallelize(data)
df = rdd.toDF(columns)
df.printSchema()
df.show(truncate=False)



