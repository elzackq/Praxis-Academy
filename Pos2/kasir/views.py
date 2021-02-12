from django.shortcuts import render, redirect

from .models import Barang, Suplier, Customer, Transaksi

# Data Barang
def h_screen(rq):
    barangs = Barang.objects.all()
    return render(rq, 'dbarang/barang.html',{
        'datum': barangs,
    })

def tambahbarang(rq):
    form = FormTambahBarang
    return render(rq, 'dbarang/barang.html', {
        'form' : form,
    })


# Data Suplier
def sup_creen(rq):
    supliers = Suplier.objects.all()
    return render(rq, 'suplier/suplier.html',{
        'datumsup' : supliers,
    })

def tambahsuplier(rq):
    form = FormTambahSuplier
    return render(rq, 'suplier/suplier.html', {
        'form' : form,
    })

# Data Customer
def cus_screen(rq):
    customrs = Customer.objects.all()
    return render(rq, 'dcustomer/customer.html',{
        'datumcus' : customrs,
    })

def tambahcuplier(rq):
    form = FormTambahCust
    return render(rq, 'dcustomer/customer.html', {
        'form' : form,
    })

# Data Transaksi
def tr_screen(rq):
    transk = Transaksi.objects.all()
    return render(rq, 'dtransaksi/trans.html',{
        'datumtran' : transk,
    })

def tambahcuplier(rq):
    form = FormTambahCust
    return render(rq, 'dtransaksi/trans.html', {
        'form' : form,
    })
    