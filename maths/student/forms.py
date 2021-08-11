from django import forms

class reg(forms.Form):
    name=forms.CharField(max_length=140)
    password=forms.CharField(max_length=120)