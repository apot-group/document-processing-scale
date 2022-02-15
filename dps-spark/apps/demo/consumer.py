import json 
from kafka import KafkaConsumer

KAFKA_CONSUMER_GROUP='demo'
KAFKA_TOPIC_NAME='kafka-sample'

consumer = KafkaConsumer(
    KAFKA_TOPIC_NAME,
    bootstrap_servers='kafka:9092',
    auto_offset_reset='earliest',
    group_id=KAFKA_CONSUMER_GROUP
)

for message in consumer:
    print("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                          message.offset, message.key,
                                          message.value))
