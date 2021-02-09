from django.db import models

class Barang(models.Model):
    kode = models.ChartField(max_length=255)
    kategori = models.ChartField(max_length=255)
    kode_barang = models.ChartField(max_length=255)
    nama_barang = models.ChartField(max_length=255)
    harga_beli = models.DecimalField()
    stok = models.DecimalField()
    lokasi = models.ChartField
    
