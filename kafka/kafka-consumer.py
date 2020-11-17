from pykafka import KafkaClient
from pymongo import MongoClient
import json
import sys

K_client = KafkaClient(hosts='localhost:9092')
topic = K_client.topics['dataets']	 
consumer = topic.get_simple_consumer(consumer_timeout_ms=5000)
	 
M_client = MongoClient('localhost',27017)
db = M_client.records
collection = db.data

counter = 1
for i in consumer:
	i = {str(counter):str(i.value.decode("utf-8")) }
	collection.insert_one(i)
	counter = counter + 1


