from django.forms import ModelForm
from django import forms
from customer.models import Orders,Reviews
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegistrationForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta():
        model=User
        fields=[
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2"
        ]
        widgets={
            "username":forms.TextInput(attrs={"class":'form-control'}),
            "first_name": forms.TextInput(attrs={"class": 'form-control'}),
            "last_name": forms.TextInput(attrs={"class": 'form-control'}),
            "email": forms.EmailInput(attrs={"class": 'form-control'}),
        }

class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class PasswordResetForm(forms.Form):
    oldpassword=forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    newpassword=forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    confirmpassword=forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def clean(self):
        cleaned_data=super().clean()
        newpassword=cleaned_data.get('newpassword')
        confirmpassword=cleaned_data.get('confrimpassword')
        if newpassword!=confirmpassword:
            msg='password mismatch'
            self.add_error("newpassword",msg)

class OrderForm(forms.ModelForm):
    class Meta():
        model=Orders
        fields=[
            "address"
        ]
        widgets={
            "address":forms.Textarea(attrs={"class":"form-cntrol"})
        }

class ReviewForm(forms.ModelForm):
    class Meta():
        model=Reviews
        fields=[
            "comment","rating"
        ]
        widgets={"comment":forms.Textarea(attrs={"class":"form-control"}),
                 "rating":forms.Select(attrs={"class":"form-select"})}