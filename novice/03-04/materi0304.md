## Aplikasi yang perlu di install bikin aplikasi web python+django dev

1. [Python](https://www.python.org/downloads/)
2. [pip](https://pip.pypa.io/en/stable/installing/)
3. [Django](https://www.djangoproject.com/download/)

## Membuat projectnya

1. Buka terminal emulator dan jalankan perintah berikut:
```
    django-admin startproject <nama_projek>
```
eg.
```
    django-admin startproject buku_catatan
```

2. Masuk ke direktori project, jalankan perintah berikut
```
    python3 manage.py runserver
```

## Membuat Aplikasi
1. Pada terminal emulator yang sudah berada di direktori projek, jalankan perintah berikut:
```
    python manage.py startapp <nama_applikasi>
```
Contoh:
```
    python manage.py startapp kegiatan
```
Pada proses ini, Django akan membuat direktori baru yang memiliki nama sesuai dengan nama aplikasi yang dibuat.
2. Kemudian, agar dapat digunakan, aplikasi harus didaftarkan terlebih dahulu. Mendaftar aplikasi dapat dilakukan dengan:

membuka file ```settings.py``` yang berada pada direktori yang memiliki nama sama dengan nama projek (misal ```buku_catatan```).

pada bagian ```INSTALLED_APPS```, tambahkan nama aplikasi yang ingin didaftarkan.

Contoh:
```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'kegiatan',
]
```

## Mengaktifkan server
1.
