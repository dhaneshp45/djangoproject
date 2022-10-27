from django import forms
from . models import Table1,Image
class RegisterForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput,max_length=8,min_length=2)
    cpassword=forms.CharField(widget=forms.PasswordInput,max_length=8,min_length=2)
    class Meta():
        model=Table1
        fields='__all__'

class LoginForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput,max_length=8,min_length=2)
    class Meta():
        model=Table1
        fields=('email','password')

class UpdateForm(forms.ModelForm):
    class Meta():
        model=Table1
        fields=('name','age','place','email')


class ChangePasswordForm(forms.Form):
    oldpassword=forms.CharField(widget=forms.PasswordInput,max_length=8,min_length=2)
    newpassword=forms.CharField(widget=forms.PasswordInput,max_length=8,min_length=2)
    cpassword=forms.CharField(widget=forms.PasswordInput,max_length=8,min_length=2)

class ImageForm(forms.ModelForm):
    Password=forms.CharField(widget=forms.PasswordInput,max_length=8,min_length=2)
    Cpassword=forms.CharField(widget=forms.PasswordInput,max_length=8,min_length=2)
    class Meta():
        model=Image
        fields='__all__'