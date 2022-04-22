from django import forms
from .models import ContactModel


class ContactForm(forms.ModelForm):
    class Meta:
        model  = ContactModel
        fields = ("first_name","last_name","email","city","state","phone","message","car_slug","car_title","customer_need")
