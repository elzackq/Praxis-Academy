from django.urls import path

from . import views

urlpatterns = [
  path('barang/', views.h_screen),
  path('input/', views.simpan_barang),
  
  path('barang/hapusbarang/<int:id>', views.hapusbarang),
  
  path('suplier/', views.sup_creen),
  path('inputsup/', views.simpansuplier),
  path('suplier/hapussup/<int:id>', views.hapussup),

  path('customer/', views.cus_screen),
  path('inputcus/', views.simpancus),
  path('customer/hapuscus/<int:id>', views.hapuscus),

  
  path('transaksi/', views.tr_screen),
]