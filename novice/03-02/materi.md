# Django Prostgres
model --> migration
#step 1 : bikin models.py
#step 2 : python manage.py makemigrations
#step 3 : python manage.py migrate

namaclass.objects.filter --> data spesifik
ex: namaclass.objects.filter(id=3).update(keterangan = 'makanlah ajah')

# conection dbcd
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "buku_catatan",
        "USER": "elzackq",
        "PASSWORD": "124313",
        "HOST": "localhost",
        "PORT": "",
    }
}