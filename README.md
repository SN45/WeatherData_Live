Weather Data Analysis Pipeline

Overview

This project demonstrates an end-to-end real-time data pipeline for analyzing weather data using modern data engineering and visualization tools. The pipeline fetches live weather information from the OpenWeather API, processes it through Apache Kafka for real-time data streaming, stores it in PostgreSQL for persistent storage, and visualizes the data in Tableau for actionable insights.

Features

Real-Time Data Retrieval: Fetches live weather data (temperature, humidity, and timestamps) using the OpenWeather API.
Scalable Data Streaming: Utilizes Apache Kafka to stream weather data efficiently in real time.
Reliable Data Storage: Stores structured data in a PostgreSQL database for long-term analysis and querying.
Interactive Dashboards: Visualizes weather trends and insights in Tableau, enabling dynamic exploration of data.
Modular Design: Separates data retrieval, processing, storage, and visualization into independent, reusable components.

Architecture

The pipeline consists of the following stages:

Data Retrieval:
The OpenWeather API fetches real-time weather data for specified cities in JSON format.
Example Data Fields: city, temperature, humidity, timestamp.
Data Streaming:
A Kafka producer streams the data into a topic (weather_data).
The data is consumed by a Kafka consumer for further processing.
Data Storage:
The Kafka consumer writes the processed data into a PostgreSQL database.
Database Schema:
city (VARCHAR)
temperature (FLOAT)
humidity (INTEGER)
timestamp (TIMESTAMP)
Data Visualization:
Tableau connects to PostgreSQL to visualize trends and insights in real-time.
Dashboards include:
Temperature trends over time.
Humidity levels comparison by city.
Technologies Used

Programming Language: Python
API Integration: OpenWeather API
Data Streaming: Apache Kafka
Database: PostgreSQL
Visualization: Tableau
Libraries: kafka-python, psycopg2, requests
How It Works

Setup:
Configure the API key and cities in the producer script.
Set up Kafka with the topic weather_data.
Create the PostgreSQL database and table schema.
Run the Pipeline:
Start the Kafka producer to stream data.
Run the Kafka consumer to process and store data in PostgreSQL.
Visualize the data in Tableau.
Output:
A PostgreSQL table (weather_data) with up-to-date weather information.
Tableau dashboards providing actionable insights into temperature and humidity trends.
Getting Started

Prerequisites
Python 3.x
PostgreSQL installed and running
Apache Kafka installed and configured
Tableau Desktop or Tableau Public for visualization
Installation
Clone the repository:
git clone https://github.com/your-username/weather-data-pipeline.git
cd weather-data-pipeline
Install dependencies:
pip install -r requirements.txt
Set up PostgreSQL:
Create the database and table schema using the provided SQL script.
Configure the OpenWeather API key:
Replace your_api_key in the producer script with your OpenWeather API key.
Run the pipeline:
Start Kafka and create the weather_data topic.
Run the producer and consumer scripts.

Future Enhancements:
Add support for multiple weather data sources.
Implement machine learning models for weather prediction.
Automate dashboard updates with Tableau Server.
