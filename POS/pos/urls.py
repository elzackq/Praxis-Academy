from django.contrib import admin
from django.urls import path

from django.shortcuts import render

def index(req):
    return render(req, 'index.html')

urlpatterns = [
    path('', index),
    path('admin/', admin.site.urls),
]