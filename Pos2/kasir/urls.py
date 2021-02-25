from django.urls import path

from . import views

urlpatterns = [
  path('', views.h_screen),
  path('barang/', views.h_screen),
  path('input/', views.simpan_barang),
  
  
  path('customer/', views.cus_screen),
  path('inputcus/', views.simpancus),

  path('suplier/', views.sup_creen),
  path('inputsup/', views.simpansuplier),
  
  path('dtransaksi/', views.tr_screen),
]