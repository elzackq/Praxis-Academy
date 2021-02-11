from django.shortcuts import render, redirect

from .models import Barang, Suplier, Customer, Transaksi

# Data Barang
def h_screen(rq):
    barangs = Barang.objects.all()
    return render(rq, 'dbarang/dbarang.html',{
        'datum': barangs,
    })


# Data Suplier
def sup_creen(rq):
    pass

# Data Customer
def cus_screen(rq):
    pass

# Data Transaksi
def tr_screen(rq):
    pass
    