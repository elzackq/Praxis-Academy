from django.shortcuts import render, redirect

from .forms import FormTambahBarang
from .models import Barang, Suplier, Customer, Transaksi
from . import forms


# <--- Data Barang --->
def h_screen(rq):
    barangs = Barang.objects.all()
    return render(rq, 'dbarang/barang.html',{
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
            return redirect('/dbarang')
        #print(form.errors)
    return render(rq,'dbarang/barang.html',{
        'form': form,
    })

def hapusbarang(rq, id):
    Barang.objects.filter(id=id).delete()
    return redirect('/dbarang')

# <--- Data Suplier --->
def sup_creen(rq):
    supliers = Suplier.objects.all()
    return render(rq, 'suplier/suplier.html',{
        'datumsup' : supliers,
    })

def tambahsuplier(rq):
    form = FormTambahSuplier
    return render(rq, 'suplier/addsup.html', {
        'form' : form,
    })

def simpansuplier(rq):
    if rq.POST:
        form = FormTambahSuplier()
        if form.is_valid():
            form.save()
            return redirect('/suplier')
        #(form.errors)
    return redirect('/suplier/addsup')

def hapussup(rq, id):
    Suplier.objects.filter(id=id).delete()
    return ('/suplier')


# <--- Data Customer --->
def cus_screen(rq):
    customrs = Customer.objects.all()
    return render(rq, 'dcustomer/customer.html',{
        'datumcus' : customrs,
    })

def tambahcus(rq):
    form = FormTambahCust
    return render(rq, 'dcustomer/customer.html', {
        'form' : form,
    })

def simpancus(rq):
    if rq.POST:
        form = FormTambahCust()
        if form.is_valid():
            form.save()
            return redirect('/dcustomer')
        #print(form.errors)
    return redirect('/dcustomer/customer')
    
def hapuscus(rq, id):
    Customer.objects.filter(id=id).delete()
    return redirect('/dcustomer')

# <--- Data Transaksi --->
def tr_screen(rq):
    transk = Transaksi.objects.all()
    return render(rq, 'dtransaksi/trans.html',{
        'datumtran' : transk,
    })

def tambahcuplier(rq):
    form = FormTambahTrans
    return render(rq, 'dtransaksi/trans.html', {
        'form' : form,
    })

def simpantrans(rq):
    if rq.POST:
        form = FormTambahTrans()
        if form.is_valid():
            form.save()
            return redirect('/dtransaksi')
        #print(form.erros)
    return redirect('/dtransaksi/trans')

def hapustrans(rq, id):
    Transaksi.objects.filter(id=id).delete()
    return redirect('/dtransaksi')