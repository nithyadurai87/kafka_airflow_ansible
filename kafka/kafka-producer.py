from pykafka import KafkaClient
import json
import time

client = KafkaClient(hosts='localhost:9092')
topic = client.topics['dataets']
producer = topic.get_sync_producer()
producer.produce(b'test message')

for e in range(1000):
    data = {'number' : e}
    print(data)
    info_as_json = json.dumps(data)
    producer.produce(info_as_json.encode('ascii'))
    time.sleep(5)
    
