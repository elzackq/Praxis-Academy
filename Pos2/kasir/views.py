from django.shortcuts import render, redirect

from .models import Barang, Suplier, Customer, Transaksi


# <--- Data Barang --->
def h_screen(rq):
    barangs = Barang.objects.all()
    return render(rq, 'dbarang/barang.html',{
        'datum': barangs,
    })

def tambahbarang(rq):
    form = FormTambahBarang
    return render(rq, 'dbarang/addbarang.html', {
        'form' : form,
    })

def simpanbarang(rq):
    if rq.POST:
        form = FormTambahBarang()
        if form.is_valid():
            form.save()
            return redirect('/dbarang')
        #print(form.errors)
    return redirect('/dbarang/addbarang')

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

def tambahcuplier(rq):
    form = FormTambahCust
    return render(rq, 'dcustomer/customer.html', {
        'form' : form,
    })


# <--- Data Transaksi --->
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
    