from django.contrib import admin
from django.urls import path
import app.views

urlpatterns = [
    path('', view=app.views.index, name='index'),
]
