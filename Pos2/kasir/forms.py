from django import forms
from django.forms import ModelForm
from .models import Barang, Suplier, Customer, Transaksi

# untuk form Barang

class FormTambahBarang(forms.ModelForm):
    class Meta:
        exclude = []
        model = Barang

# untuk form Suplier

class FormTambahSuplier(forms.ModelForm):
    class Meta:
        exclude = []
        model = Barang

# untuk form Customer

class FormTambahCust(forms.ModelForm):
    class Meta:
        exclude = []
        model = Barang

# untuk form Transaksi

class FormTambahTrans(forms.ModelForm):
    class Meta:
        exclude = []
        model = Barang
