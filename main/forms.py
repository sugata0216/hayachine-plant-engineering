from django import forms

from .models import *

class InquiryForm(forms.ModelForm):
    
    class Meta:
        model = Contact
        fields = (
            'genre',
            'last_name',
            'first_name',
            'postal_code',
            'address',
            'image',
            'phone_number',
            'mail',
            'content',
        )