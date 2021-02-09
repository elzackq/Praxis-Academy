from django.db import models

class Barang(models.Model):
    kode_barang = models.CharField(max_length=20)
    nama_barang = models.CharField(max_length=255)
    harga_beli = models.()
    harga_

    def __init__(self):
        pass
        