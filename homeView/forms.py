from django import forms
from .models import Scripts

class ScriptForm(forms.Model):
    class Meta:
        model = Scripts
        fields = ['scriptName','scriptDescription']