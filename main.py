# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 18:44:08 2023

@author: user
"""

import paho.mqtt.client as mqtt
from cloudant.client import Cloudant
from datetime import datetime
from random import randint, random
import serial
import time
from socket import *
import json
import threading
from joblib import load


# =============================================================================
# Initializations and connecion establishment
# =============================================================================

# Arduino board
ser = serial.Serial("", 115200, timeout=1.0)
time.sleep(3)
ser.reset_input_buffer()
print("Board ready")

# Model and Weather condition mapping table
model = load('model.joblib')
weather_map_table = {1: 'Mostly Cloudy', 2: 'Fair', 3: 'Partly Cloudy', 4: 'Cloudy', 5: 'Thunder', 6: 'Light Rain', 7: 'Light Rain Shower', 8: 'Fog', 9: 'Rain Shower', 10: 'Light Drizzle', 11: 'Rain'}

# IBM Watson IOT
device_type = "RaspberryPi"
device_id = "Device0001"
org_id = "flhgbn"

url = "{}.messaging.internetofthings.ibmcloud.com".format(org_id)
port = 8883
client_id = "d:{}:{}:{}".format(org_id, device_type, device_id)

topic_name = "iot-2/evt/sensor_data/fmt/json"

username = "use-token-auth"
token = "Device0001"

def on_connect(client, userdata, flags, rc):
        print("Connecting to... " + url)
        print("Connection returned result: " + mqtt.connack_string(rc))

def on_disconnect(client, userdata, rc):
        print("Disconnected from... " + url)

def on_publish(client, userdata, mid):
        print("Published a message: " + str(mid))

def on_log(client, userdata, level, buf):
        print("LOG: ", buf)

client = mqtt.Client(client_id)
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_publish = on_publish

try:
    client.username_pw_set(username=username, password=token)
    client.tls_set()
    client.connect(url, port, 60)
except:
    print("Watson IOT Connection failed:")
    
# IBM Cloudant
URL = 'https://8c5d6aa9-3760-4133-a2af-67b19e8e8139-bluemix.cloudantnosqldb.appdomain.cloud'
API_KEY = 'Z9YhLhqkCJr0cFqsErZnzrm0uuCxExZUWGfx2mmByz16'

try:
    cloudant_client = Cloudant.iam(None, API_KEY, url= URL, connect=True)
    db = cloudant_client['iot_data']
except:
    print("Cloudant Connection failed:")    

# Local Website
serversocket=socket(AF_INET, SOCK_STREAM)
try:
    serversocket.bind(('localhost', 8000))
    serversocket.listen(5)
    print("serving from localhost:8000")
except:
    print("Socket Connection Error")


# =============================================================================
# Data forwarding functions
# =============================================================================

def send_forward(data):
    data=json.loads(data)
    
    device_id = data['device_id']    
    temperature = data['temperature']
    pressure = data['pressure']
    humidity = data['humidity']
    rain = data['rain']
    day_or_night = data['day_or_night']
    timestamp=datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f%z")
    
    # [temperature	pressure	humidity	rain	day_or_night]
    prediction = model.predict([[temperature, pressure, humidity, rain, day_or_night]])
    weather = weather_map_table[prediction[0]]
    
    transmit_data={'device_id': device_id, 'timestamp': timestamp, 'temperature': temperature, 'pressure': pressure, 'humidity': humidity, 'rain': rain, 'day_or_night': day_or_night, 'weather': weather}
    transmit_data=json.dumps(transmit_data)
    
    t1=threading.Thread(target=send_to_watson, args=(transmit_data))
    t2=threading.Thread(target=send_to_cloudant, args=(transmit_data))
    t3=threading.Thread(target=send_to_local, args=(transmit_data))
    t1.start()
    t2.start()
    t3.start()


def send_to_watson(transmit_data):
    (rc, mid) = client.publish(topic_name, payload=transmit_data)

def send_to_cloudant(transmit_data):
    db.create_document(transmit_data)
    
def send_to_local(transmit_data):
    (clientsocket, address)=serversocket.accept()
    rawdata=clientsocket.recv(1024).decode()
    info=rawdata.split('\r\n')
    if len(info)>0:
        for i in info:
            print(i.strip('\r\n'))
    
    clientsocket.sendall(transmit_data.encode())
    clientsocket.shutdown(SHUT_WR)
    
    

# =============================================================================
# Main Context
# =============================================================================

try:
    while True:
        time.sleep(0.01)
        if ser.inWaiting()>0:
            line = ser.readline().decode().strip()
            print("Data from arduino:", line)
            
            t=threading.Thread(target=send_forward, args=(data))
            t.start()
        
except Exception as e:
    ser.close()
    client.disconnect()
    cloudant_client.disconnect()
    serversocket.close()
    print(e)
