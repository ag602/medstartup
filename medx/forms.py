from .models import *
from django import forms

class Contact(forms.ModelForm):
    class Meta:
        model = contact
        fields = ['fname', 'lname', 'email', 'message']