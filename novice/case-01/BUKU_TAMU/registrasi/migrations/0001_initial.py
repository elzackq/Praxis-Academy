# Generated by Django 2.2 on 2021-01-05 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=255)),
                ('alamat', models.CharField(max_length=255)),
                ('tlp', models.CharField(max_length=20)),
                ('keperluan', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
