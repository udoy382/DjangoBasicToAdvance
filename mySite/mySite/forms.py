from django import forms
from django.forms.forms import Form

class usersForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    phone = forms.CharField()
