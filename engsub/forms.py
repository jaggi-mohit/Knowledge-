from django.db.models import fields
from .models import Computer, show
from django import forms

class editor(forms.ModelForm):
    class Meta:
        model=Computer
        fields= ['code']


class edit(forms.ModelForm):
    class Meta:
        model = Computer
        fields =['desc']

class shw(forms.ModelForm):
    class Meta:
        model = show
        fields =['shws']