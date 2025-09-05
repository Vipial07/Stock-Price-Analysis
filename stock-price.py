import requests
from bs4 import BeautifulSoup
from datetime import datetime
import time

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
        rec = [current_time, price]
        print(rec)
    else:
        print("Price not found")

    time.sleep(5)  # wait 5 seconds before fetching again