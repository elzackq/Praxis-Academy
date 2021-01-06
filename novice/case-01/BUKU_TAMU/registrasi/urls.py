from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_screen),
    path('tambah', views.tambah),
    path('simpanbaru', views.simpanbaru),

    path('<int:id>', views.detail),
    path('<int:id>/hapus', views.hapus),

    path('profile', views.profilscr),
]