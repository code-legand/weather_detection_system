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
URL = 'https://8c5d6aa9-3760-4133-a2af-67b19e8e8139-bluemix.cloudantnosqldb.appdomain.cloud'
API_KEY = 'Z9YhLhqkCJr0cFqsErZnzrm0uuCxExZUWGfx2mmByz16'

# client = Cloudant.iam(ACCOUNT_NAME, API_KEY, connect=True)
client = Cloudant.iam(None, API_KEY, url= URL, connect=True)

db = client['iot_data']

device_id = "Device0001"
temperature = randint(50, 100)
humidity = randint(0, 100)
rain = randint(0, 100)
pressure = 29+random()
weather_map = ['Mostly Cloudy', 'Fair', 'Partly Cloudy', 'Cloudy', 'Thunder', 'Light Rain', 'Light Rain Shower', 'Fog', 'Rain Shower', 'Light Drizzle', 'Rain']
weather = choice(weather_map)

_id = str(uuid.uuid4()).replace('-', '')
time = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f%z")

db.create_document({
    'id': _id, 
    'device_id': device_id, 
    'timestamp': time, 
    'temperature': temperature,
    'humidity': humidity, 
    'pressure': pressure, 
    'rain': rain, 
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
