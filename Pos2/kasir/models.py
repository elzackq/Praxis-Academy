from django.db import models

# Data Barang

class Barang(models.Model):
    kode = models.CharField(max_length=255)
    kategori = models.CharField(max_length=255)
    kode_barang = models.CharField(max_length=255)
    nama_barang = models.CharField(max_length=255)
    harga_beli = models.DecimalField(max_digits=15, decimal_places=2)
    harga_jual = models.DecimalField(max_digits=15, decimal_places=2)
    diskon = models.DecimalField(max_digits=15, decimal_places=0)
    stok = models.DecimalField(max_digits=5, decimal_places=0)
    lokasi = models.CharField

# Data Suplier

class Suplier(models.Model):
    id_suplier = models.CharField(max_length=255)
    nama_suplier = models.CharField(max_length=255)
    alamat = models.CharField(max_length=255)
    no_tlp = models.CharField(max_length=255)
    rek_bank = models.CharField(max_length=255)
    pemilik_rek = models.CharField(max_length=255)

# Data Customer

class customer(models.Model):
    id_cus = models.CharField(max_length=255)
    nama_cus = models.CharField(max_length=255)
    alamat = models.CharField(max_length=255)
    no_tlp = models.CharField(max_length=255)
    kota = models.CharField(max_length)

# Data Transaksi

class Transaksi(models.Model):
    no_nota = models.CharField(max_length=255)
    date = models.TimeField()
    qty = models.DecimalField(max_digits=5, decimal_places=0)
    total = models.DecimalField(max_digits=5, decimal_places=0)
    dp = models.DecimalField(max_digits=15, decimal_places=2)
    sisa = models.DecimalField(max_digits=15, decimal_places=2)