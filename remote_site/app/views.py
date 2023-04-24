from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse, FileResponse
import json
import datetime
import os

from cloudant.client import Cloudant

URL = 'https://apikey-v2-2porvk0ltjx250fch5349iijd7z20mmkvm2cgao48mkf:70d9628dc2173b2ea7f6749ff06b1575@b2cf2182-108f-4d74-99d3-027d6846c573-bluemix.cloudantnosqldb.appdomain.cloud'
API_KEY = 'PQ79KqrbVKEFLkTorUdqxKun1CkU0fikbDI4KephQh1-'

client = Cloudant.iam(None, API_KEY, url= URL, connect=True)

db = client['iot_data']

# Create your views here.

def index(request):
    return render(request, 'index.html')

def send(request):
    device_id = request.POST.get('device_id')
    result = db.get_query_result(selector={'device_id': {'$eq': device_id}}, 
                           fields = ['_id', 'timestamp', 'temperature', 'humidity', 'rain', 'pressure', 'day_or_night', 'weather'],
                           limit= 5,  
                           raw_result=True
                           )
    for doc in result['docs']:
        print(doc)
    return JsonResponse(result['docs'], safe=False)