# Generated by Django 2.2 on 2020-11-26 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toko', '0006_auto_20201112_0818'),
    ]

    operations = [
        migrations.AddField(
            model_name='toko',
            name='nama_bank',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='toko',
            name='nomor_rek',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='toko',
            name='pemilik_bank',
            field=models.TextField(default='', max_length=255),
        ),
    ]
