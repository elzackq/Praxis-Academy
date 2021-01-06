from django.contrib import admin
from django.urls import path, include

from django.shortcuts import render

def index(req):
    return render(req, 'index.html')

urlpatterns = [
    path('', index),
    path('registrasi/', include('registrasi.urls')),
    path('admin/', admin.site.urls),
]
