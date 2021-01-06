from django.shortcuts import render, redirect

# Create your views here.

from .forms import FormAddRegist
from .models import Register

def home_screen(req):
    regist = Register.objects.all()
    return render(req, 'registrasi/index.html', {
        'datum' : regist,
    })

def detail(req, id):
    register = Register.objects.filter(id=id).first()
    return render(req, 'registrasi/detail.html',{
        'register': register,
    })

def hapus(req, id):
    Register.objects.filter(id=id).delete()
    return redirect('/registrasi')
    
def tambah(req):
    form = FormAddRegist()
    return render(req, 'registrasi/tambah.html',{
        'form': form,
    })

def simpanbaru(req):
    if req.POST:
        form = FormAddRegist(req.POST)

        if form.is_valid():
            form.save()
            return redirect('/registrasi')

        print(form.errors)
    return redirect('/registrasi/tambah')

def profilscr(req):
    return render(req, 'registrasi/profile.html')