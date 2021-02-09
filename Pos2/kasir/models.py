from django.db import models

# Data Barang

class Barang(models.Model):
    kode = models.CharField(max_length=255)
    kategori = models.CharField(max_length=255)
    kode_barang = models.CharField(max_length=255)
    nama_barang = models.CharField(max_length=255)
    harga_beli = models.DecimalField(max_digits=12, decimal_places=2)
    harga_jual = models.DecimalField(max_digits=12, decimal_places=2)
    stok = models.DecimalField(max_digits=4, decimal_places=0)
    lokasi = models.CharField
    
# Data Stok

# Data Supplier

