from django import forms
from django.forms import ModelForm, fields
from core.models import Celular
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 


class CelularForm(ModelForm):

    class Meta:
        model = Celular
        fields = ['marca','modelo','precio','cliente']
        

class CustomUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','email','username','password1','password2']
    
