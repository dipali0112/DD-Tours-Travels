# In trvels/forms.py
from django import forms
from .models import Contact,Location, Inquiry

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']

class InquiryForm(forms.ModelForm):
    class Meta:
        model = Inquiry
        fields = ['name', 'email', 'contact_number', 'place', 'number_of_persons', 'departure_date', 'return_date', 'transportation_method']