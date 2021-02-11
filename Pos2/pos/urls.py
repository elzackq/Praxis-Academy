from django.contrib import admin
from django.urls import path, include

from django.shortcuts import render

def index(rq):
    return render(rq, 'index.html')

def cont(rq):
    return render(rq, 'contact.html')
    
urlpatterns = [
    path('', index),
    path('cont/', cont),
    path('kasir/', include('kasir.urls')),
    path('admin/', admin.site.urls),
]
