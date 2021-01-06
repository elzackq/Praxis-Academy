from django import forms

from .models import Register

class FormAddRegist(forms.ModelForm):
    class Meta:
        exclude = []
        model = Register