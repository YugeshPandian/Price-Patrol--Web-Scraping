from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.contrib.auth.models import AbstractUser
from django.db import models

from django import forms

from django.contrib.auth.models import User

class CustomUserForm(UserCreationForm):
    phone = forms.CharField(max_length=10)
    
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter User Name'}))
    email=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Valid Mail Id'}))
    phone=forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter Phone Number'}))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Password'}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Confirm Password '}))
   
    class Meta:
        model = User
        fields = ['username', 'email', 'phone', 'password1', 'password2']
