from django.urls import path

from . import views

urlpatterns = [
  path('', views.h_screen),
  path('dbarang/', views.simpan_barang),
  path('suplier/', views.sup_creen),
  path('dcustomer/', views.cus_screen),
  path('dtransaksi/', views.tr_screen),
  
  path('input/', views.simpan_barang)
]