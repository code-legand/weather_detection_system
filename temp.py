# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 14:55:08 2023

@author: user
"""

from socket import *
import json
from datetime import datetime
import threading

serversocket=socket(AF_INET, SOCK_STREAM)

try:
    serversocket.bind(('localhost', 8000))
    serversocket.listen(5)
    print("serving from localhost:8000")
except:
    print("Connection Error")
    quit()

def send_data(data):   
    try:
        # listen for 5 seconds and then quit
        # serversocket.settimeout(5)
        (clientsocket, address)=serversocket.accept()
        rawdata=clientsocket.recv(1024).decode()
        info=rawdata.split('\r\n')
        if len(info)>0:
            for i in info:
                print(i.strip('\r\n'))
        
        string=data
        json_data=json.loads(string)
        json_data["timestamp"]=time

        data=json.dumps(json_data)
        
        clientsocket.sendall(data.encode())
        clientsocket.shutdown(SHUT_WR)
    except Exception as e:
        print(e)
        serversocket.close()
        # quit()
        

time = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f%z")
data='{"device_id": "Device0001", "temperature": 85, "pressure": 29.5, "rain": 0, "humidity": 55}'

for i in range(3):
    t=threading.Thread(target=send_data, args=(data,))
    t.start()

    
print("Done")





