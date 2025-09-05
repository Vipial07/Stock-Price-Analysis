from kafka import KafkaProducer
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import time
import json
import random

# Create Kafka producer
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    key_serializer=lambda k: k.encode('utf-8'),
    value_serializer=lambda v: v.encode('utf-8')
)

ticker = 'INFY'
url = f'https://www.google.com/finance/quote/{ticker}:NSE'

class_infy = 'YMlKec fxKbKc'  # class for stock price

while True:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    price_tag = soup.find(class_=class_infy)

    if price_tag:
        price = price_tag.text
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        rec = {
            "time": current_time,
            "price": random.randint(100, 1000)
        }
        print(rec)
        # Serialize to JSON string before sending
        producer.send('stock-topic', key='key1', value=json.dumps(rec))
        producer.flush()
        # print("Message sent successfully")
    else:
        print("Price not found")

    time.sleep(5)  # wait 5 seconds before fetching again
