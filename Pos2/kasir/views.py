from django.shortcuts import render, redirect

from .forms import FormTambahBarang, FormTambahCust, FormTambahSuplier, FormTambahTrans
from .models import Barang, Suplier, Customer, Transaksi
from . import forms


# <--- Data Barang --->
def h_screen(rq):
    barangs = Barang.objects.all()
    return render(rq, 'barang/barang.html',{
        'datum': barangs,
    })

# def tambahbarang(rq):
#     form = FormTambahBarang()
#     return render(rq, 'dbarang/barang.html', {
#         'form' : form,
#     })

def simpan_barang(rq):
    form = FormTambahBarang()
    if rq.POST:
        form = FormTambahBarang(rq.POST)
        if form.is_valid():
            form.save()
            return redirect('/kasir/barang')
        #print(form.errors)
    return render(rq,'barang/addbarang.html',{
        'form': form,
    })

def hapusbarang(rq, id):
    Barang.objects.filter(id=id).delete()
    return redirect('/kasir/barang')

# <--- Data Suplier --->
def sup_creen(rq):
    supliers = Suplier.objects.all()
    return render(rq, 'suplier/suplier.html',{
        'datumsup' : supliers,
    })

# def tambahsuplier(rq):
#     form = FormTambahSuplier
#     return render(rq, 'suplier/addsup.html', {
#         'form' : form,
#     })

def simpansuplier(rq):
    form = FormTambahSuplier()
    if rq.POST:
        form = FormTambahSuplier(rq.POST)
        if form.is_valid():
            form.save()
            return redirect('/kasir/suplier')
        #(form.errors)
    return render(rq, 'suplier/addsupply.html',{
        'form' : form,
    })

def hapussup(rq, id):
    Suplier.objects.filter(id=id).delete()
    return redirect('/kasir/suplier')


# <--- Data Customer --->
def cus_screen(rq):
    customrs = Customer.objects.all()
    return render(rq, 'customer/customer.html',{
        'datumcus' : customrs,
    })

# def tambahcus(rq):
#     form = FormTambahCust
#     return render(rq, 'dcustomer/customer.html', {
#         'form' : form,
#     })

def simpancus(rq):
    form = FormTambahCust()
    if rq.POST:
        form = FormTambahCust(rq.POST)
        if form.is_valid():
            form.save()
            return redirect('/kasir/customer')
        #print(form.errors)
    return render(rq, 'customer/addcus.html',{
        'form': form,
    })
    
def hapuscus(rq, id):
    Customer.objects.filter(id=id).delete()
    return redirect('/kasir/customer')

# <--- Data Transaksi --->
def tr_screen(rq):
    transk = Transaksi.objects.all()
    return render(rq, 'transaksi/trans.html',{
        'datumtran' : transk,
    })

def tambahtrans(rq):
    form = FormTambahTrans
    return render(rq, 'transaksi/trans.html', {
        'form' : form,
    })

def simpantrans(rq):
    if rq.POST:
        form = FormTambahTrans()
        if form.is_valid():
            form.save()
            return redirect('/transaksi')
        #print(form.erros)
    return redirect('/transaksi/trans')

def hapustrans(rq, id):
    Transaksi.objects.filter(id=id).delete()
    return redirect('/transaksi')