from kafka import KafkaConsumer
import psycopg2
import json
from datetime import datetime

# PostgreSQL connection setup
try:
    conn = psycopg2.connect(
        host="localhost",            # PostgreSQL server address
        database="weather_data_db",  # Name of your database
        user="flash",        # Replace with your PostgreSQL username
        password="1045"     # Replace with your PostgreSQL password
    )
    cursor = conn.cursor()
    print("Connected to PostgreSQL successfully!")
except Exception as e:
    print(f"Error connecting to PostgreSQL: {e}")
    exit(1)

# Kafka Consumer setup
try:
    consumer = KafkaConsumer(
        'weather_data',  # Kafka topic name
        bootstrap_servers='localhost:9092',
        auto_offset_reset='earliest',
        value_deserializer=lambda x: json.loads(x.decode('utf-8'))
    )
    print("Connected to Kafka successfully!")
except Exception as e:
    print(f"Error connecting to Kafka: {e}")
    exit(1)

print("Consumer started. Writing data to PostgreSQL...")

# Consume messages from Kafka and write to PostgreSQL
for message in consumer:
    try:
        # Parse the consumed message
        data = message.value
        city = data['name']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        timestamp = datetime.utcfromtimestamp(data['dt'])  # Convert UNIX timestamp to datetime

        # Insert data into PostgreSQL
        cursor.execute("""
            INSERT INTO weather_data (city, temperature, humidity, timestamp)
            VALUES (%s, %s, %s, %s)
        """, (city, temperature, humidity, timestamp))
        conn.commit()
        print(f"Inserted into database: {data}")
    except Exception as e:
        print(f"Error processing message: {e}")
        conn.rollback()

producer.send('weather_data', weather_data)
print(f"Sent to Kafka: {weather_data}")


# Close the PostgreSQL connection gracefully
cursor.close()
conn.close()
