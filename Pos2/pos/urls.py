from django.contrib import admin
from django.urls import path, include

from django.shortcuts import render

def index(rq):
    return render(rq, 'index.html')
    
urlpatterns = [
    path('', index),
    path('admin/', admin.site.urls),
]
