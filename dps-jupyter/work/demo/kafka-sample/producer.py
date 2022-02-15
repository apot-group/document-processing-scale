import random 
import json
from kafka import KafkaProducer
from datetime import datetime
import time

from confluent_kafka.admin import AdminClient, NewTopic


bootstrap_servers='kafka:9092'
admin_client = AdminClient({
    "bootstrap.servers": bootstrap_servers
})
topic_list = []
topic_1='kafka-sample'
topic_list.append(NewTopic(topic_1, 1, 1))
admin_client.create_topics(topic_list)


user_ids = list(range(1, 101))
recipient_ids = list(range(1, 101))

# Messages will be serialized as JSON 
def serializer(message):
    return json.dumps(message).encode('utf-8')

# Kafka Producer
producer = KafkaProducer(
    bootstrap_servers=[bootstrap_servers],
    value_serializer=serializer
)

# Create Message sample
def generate_message() -> dict:
    random_user_id = random.choice(user_ids)
    # Copy the recipients array
    recipient_ids_copy = recipient_ids.copy()
    # User can't send message to himself
    recipient_ids_copy.remove(random_user_id)
    random_recipient_id = random.choice(recipient_ids_copy)
    return {
        'time': str(datetime.now()),
        'user_id': random_user_id,
        'recipient_id': random_recipient_id,
        'data': {"image_path": "./demo/data/test.jpeg"}
    }

if __name__ == '__main__':
    i = 1
    # Infinite loop - runs until you kill the program
    while True:
        # Generate a message
        dummy_message = generate_message()
        
        # Send it to our 'messages' topic
        print(f'Producing message @ {datetime.now()} | Message = {str(dummy_message)}')
        producer.send('kafka-sample', dummy_message)
        
        # Sleep for a random number of seconds
        # time_to_sleep = random.randint(1, 30)
        time_to_sleep = 5
        time.sleep(time_to_sleep)
        i += 1
        if i == 10:
            break