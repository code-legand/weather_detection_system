# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 22:42:42 2023

@author: user
"""

from cloudant.client import Cloudant
from datetime import datetime
from random import randint, random, choice
import uuid

# ACCOUNT_NAME = 
URL = 'https://apikey-v2-2porvk0ltjx250fch5349iijd7z20mmkvm2cgao48mkf:70d9628dc2173b2ea7f6749ff06b1575@b2cf2182-108f-4d74-99d3-027d6846c573-bluemix.cloudantnosqldb.appdomain.cloud'
API_KEY = 'PQ79KqrbVKEFLkTorUdqxKun1CkU0fikbDI4KephQh1-'

# client = Cloudant.iam(ACCOUNT_NAME, API_KEY, connect=True)
client = Cloudant.iam(None, API_KEY, url= URL, connect=True)

db = client['iot_data']

device_id = "Device0001"
temperature = randint(50, 100)
humidity = randint(0, 100)
rain = randint(0, 100)
pressure = 29+random()
day_or_night = choice([0, 1])
weather_map = ['Mostly Cloudy', 'Fair', 'Partly Cloudy', 'Cloudy', 'Thunder', 'Light Rain', 'Light Rain Shower', 'Fog', 'Rain Shower', 'Light Drizzle', 'Rain']
weather = choice(weather_map)

# _id = str(uuid.uuid4()).replace('-', '')
time = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f%z")

#     transmit_data={'device_id': device_id, 'timestamp': timestamp, 'temperature': temperature, 'pressure': pressure, 'humidity': humidity, 'rain': rain, 'day_or_night': day_or_night, 'weather': weather}
db.create_document({
    'device_id': device_id, 
    'timestamp': time, 
    'temperature': temperature,
    'pressure': pressure,
    'humidity': humidity, 
    'rain': rain, 
    'day_or_night': day_or_night,
    'weather': weather
})


# selector = {'device_id': {'$eq': 'Device0001'}}
# docs = db.get_query_result(selector)
# for doc in docs:
#     print(doc)

# query = {'fields': ['temperature', 'humidity', 'rain', 'pressure'], 
#          'sort':[{'temperature':'desc'}], 
#          'limit': 3
#          }   
result = db.get_query_result(selector={'device_id': {'$eq': 'Device0001'}}, 
                           fields = ['_id', 'temperature', 'humidity', 'rain', 'pressure'],
                           limit= 1, 
                           skip=2,   
                           raw_result=True
                           )
# print(docs)
for doc in result['docs']:
    print(doc)

# print(db[_id])

client.disconnect()
