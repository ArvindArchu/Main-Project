from django import forms
from django.forms import fields
from .models import *

class productForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['productname','price','description','image']