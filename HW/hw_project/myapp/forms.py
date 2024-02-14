import datetime
from django import forms
from .models import User


class ProductFormWidget(forms.Form):
    """This class is a first type to create form for model"""
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите название продукта'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Введите описание продукта'}))
    price = forms.DecimalField(max_digits=8, decimal_places=2, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    count = forms.IntegerField(min_value=0, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Введите количество товара'}))
    image = forms.ImageField()


class NewUser(forms.ModelForm):
    """This class is a second type to create form for model"""

    class Meta:
        model = User
        fields = ['name', 'email', 'phone', 'adress']
