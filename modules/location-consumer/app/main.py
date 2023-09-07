import os
from kafka import KafkaConsumer
import json
import datetime

from models import Location
from services import LocationService



TOPIC_NAME = 'location'
KAFKA_SERVER = "kafka.default.svc.cluster.local:9092"

print("Sending message Kafka topic: " + TOPIC_NAME)



consumer = KafkaConsumer(TOPIC_NAME,
                         group_id='location',
                         bootstrap_servers=KAFKA_SERVER)


"""Wait for messages to arrive in the kafka broker and store de location in the database"""
for message in consumer:
    print (message)
    location_msg = json.loads(message.value.decode('utf-8'))
    print('{}'.format(location_msg))
    #creation_time = datetime.datetime.utcnow()
    #location = json.loads(location_msg)
    location = {
        'person_id': location_msg["person_id"],
        'longitude': location_msg["longitude"],
        'latitude': location_msg["latitude"],
        #'creation_time': creation_time
    }
    print(location)
    new_location: Location = LocationService.create(location)
    #print(new_location)