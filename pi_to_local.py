# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 14:55:08 2023

@author: user
"""

from socket import *
import json
from datetime import datetime
from random import *

serversocket=socket(AF_INET, SOCK_STREAM)

try:
    serversocket.bind(('localhost', 8000))
    serversocket.listen(5)
    print("serving from localhost:8000")
except:
    print("Connection Error")
    quit()

time = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f%z")
# data='{'+'"device_id": "None", "timestamp": {}, "temperature": 0, "pressure": 0, "rain": 0, "humidity": 0'.format(time)+'}'
weather_map = ['Mostly Cloudy', 'Fair', 'Partly Cloudy', 'Cloudy', 'Thunder', 'Light Rain', 'Light Rain Shower', 'Fog', 'Rain Shower', 'Light Drizzle', 'Rain']

try:
    while 1:
        (clientsocket, address)=serversocket.accept()
        rawdata=clientsocket.recv(1024).decode()
        info=rawdata.split('\r\n')
        if len(info)>0:
            for i in info:
                print(i.strip('\r\n'))
        
        # string='{"device_id": "Device0001", "temperature": 85, "pressure": 29.5, "rain": 0, "humidity": 55, "weather": "Light Rain Shower"}'
        device_id = "Device0001"
        temperature = randint(50, 100)
        humidity = randint(0, 100)
        rain = randint(0, 100)
        pressure = round(29+random(), 1)
        weather = choice(weather_map)

        time = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f%z")

        string={
            'device_id': device_id, 
            'timestamp': time, 
            'temperature': temperature,
            'humidity': humidity, 
            'pressure': pressure, 
            'rain': rain, 
            'weather': weather
        }

        string["timestamp"]=time

        data=json.dumps(string)
        
        clientsocket.sendall(data.encode())
        clientsocket.shutdown(SHUT_WR)
except Exception as e:
    print(e)
    serversocket.close()
    # quit()
    
