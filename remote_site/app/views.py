from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse, FileResponse
import json
import datetime
import os
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def index(request):
    return render(request, 'index.html')