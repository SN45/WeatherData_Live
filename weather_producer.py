from kafka import KafkaProducer
import requests
import json
import time

# Kafka Producer setup
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# OpenWeather API setup
API_KEY = "d4d7fa7699980bd4c97172d9287f6024"  # Replace with your API key
CITY = "Dallas"
URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}"

while True:
    try:
        # Fetch weather data
        response = requests.get(URL)
        weather_data = response.json()

        # Send data to Kafka
        producer.send('weather_data', weather_data)
        print(f"Produced: {weather_data}")

        # Wait for 10 seconds before fetching again
        time.sleep(10)
    except Exception as e:
        print(f"Error: {e}")

response = requests.get(URL)
weather_data = response.json()
print(f"Fetched Data: {weather_data}")

