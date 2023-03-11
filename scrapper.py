# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 09:40:06 2023

@author: user
"""

from urllib import request
import json

full_data=[]
for i in range(20, 23):
    for j in range(1, 12):
        request_url = request.urlopen('https://api.weather.com/v1/location/VOML:9:IN/observations/historical.json?apiKey=e1f10a1e78da46f5b10a1e78da96f525&units=e&startDate=20{}{:02d}01&endDate=20{}{:02d}28'.format(i, j, i, j))
        raw_data = request_url.read()
        json_data = json.loads(raw_data)
        for data in json_data['observations']:
            full_data.append(data)
        with open("data.json", "w") as file:
            json.dump(full_data, file)

# print(request_url.read())
# print(json.dumps(json_data, indent=4))
# json_data['observations'][0]
len(full_data)
