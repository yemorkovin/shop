from django import forms

class Reg(forms.Form):
    login = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
    phone = forms.CharField()
    email = forms.EmailField()

class Auth(forms.Form):
    login = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())