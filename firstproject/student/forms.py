from django import forms

class studRegister(forms.Form):
    name=forms.CharField(max_length=120)
    email=forms.EmailField()
    course=forms.CharField(max_length=120)
    phone=forms.CharField(max_length=23)
    username=forms.CharField(max_length=120)
    password=forms.CharField(max_length=30)
