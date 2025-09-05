from kafka import KafkaConsumer
import json
import base64

# Kafka consumer
consumer = KafkaConsumer(
    'stock-topic',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='beginning',
    enable_auto_commit=True,
    group_id='my-group'
)

print("Listening for messages...")

for message in consumer:
    byte_data = message.value

    try:
        # Decode bytes to string
        json_str = byte_data.decode('utf-8')

        # Parse JSON string to dict
        data = json.loads(json_str)

        # Extract values
        time = data.get("time")
        price = data.get("price")
        print(time)
        print(price[1:])

    except Exception as e:
        print(f"Error processing message: {e}")

