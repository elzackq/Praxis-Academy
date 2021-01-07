from django.db import models

# Create your models here.
class Register(models.Model):
    nama = models.CharField(max_length=255)
    alamat = models.CharField(max_length=255)
    tlp = models.CharField(max_length=20)
    keperluan = models.TextField(blank=True, null=True)
        