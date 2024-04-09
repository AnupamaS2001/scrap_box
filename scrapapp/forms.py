from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from scrapapp.models import UserProfile,Scrap

class Register_form(UserCreationForm):
    class Meta:
        model=User
        fields=["username","email","password1","password2"]

class Signin_form(forms.Form):
    username=forms.CharField()
    password=forms.CharField()

class Profile_form(forms.ModelForm):
    class Meta:
        model=UserProfile
        exclude=("user",)

class Scrap_form(forms.ModelForm):
    class Meta:
        model=Scrap
        exclude=('user','status',)