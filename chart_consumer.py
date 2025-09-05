from kafka import KafkaConsumer
import json
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from threading import Thread
from queue import Queue
import time

# Initialize shared queue for data between threads
data_queue = Queue()

# In-memory storage for plotting
time_list = []
price_list = []

# Kafka consumer in a background thread
def consume_messages():
    consumer = KafkaConsumer(
        'stock-topic',
        bootstrap_servers=['localhost:9092'],
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        group_id='my-group'
    )
    print("Kafka consumer started...")

    for message in consumer:
        try:
            json_str = message.value.decode('utf-8')
            data = json.loads(json_str)
            time_val = data.get('time')
            price_val = data.get('price')

            # Clean and convert price (₹1,446.00 → 1446.0)
            # price_float = float(price_val.replace('₹', '').replace(',', ''))

            # Put parsed data into the queue
            data_queue.put((time_val, price_val))
        except Exception as e:
            print(f"Error decoding message: {e}")

# Start Kafka consumer thread
consumer_thread = Thread(target=consume_messages, daemon=True)
consumer_thread.start()

# Matplotlib setup
fig, ax = plt.subplots()
bar_container = None

def animate(i):
    # Fetch new data from queue
    while not data_queue.empty():
        time_val, price_val = data_queue.get()

        # Append only new data
        if time_val not in time_list:
            time_list.append(time_val)
            price_list.append(price_val)

            # Optional: Keep last N entries
            if len(time_list) > 20:
                time_list.pop(0)
                price_list.pop(0)

    # Clear and redraw
    ax.clear()
    ax.bar(time_list, price_list, color='skyblue')
    ax.set_xlabel('Time')
    ax.set_ylabel('Price (INR)')
    ax.set_title('Live Stock Prices')
    ax.tick_params(axis='x', rotation=45)
    plt.tight_layout()

# Animate every 1000 ms (1 sec)
ani = animation.FuncAnimation(fig, animate, interval=1000)

print("Launching live chart...")
plt.show()
