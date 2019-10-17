from django import forms
from django.db import models
from .models import Product, Catalog, Category, Charact, Delivery, Property
CHOICES = [('home', 'Домой'), ('storage', 'Со склада')]
class CheckoutForm(forms.Form):
    email = forms.EmailField(label="Почта")
    firstName = forms.CharField(label="Имя")
    phone = forms.CharField(label="Телефон")

    
    deliveryType = forms.ChoiceField(label="",
                                initial='home',
                                widget=forms.RadioSelect, 
                                choices=CHOICES,
                                required=True,
                                )
    address = forms.CharField(label="Адрес", required=False)
    delivery = forms.ModelChoiceField(label="", queryset=Delivery.objects.all(), required=False )
