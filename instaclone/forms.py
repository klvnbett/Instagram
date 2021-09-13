from .models import *
from django import forms

class FormDetails(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

class FormImage(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['profile','date','like']
