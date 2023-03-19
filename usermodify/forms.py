from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from phone_field import PhoneField
from django.contrib.auth.models import User

from django import forms

#generating a registration form and login to add to the template
class RegisterUserForm(UserCreationForm):
	username = forms.CharField(label='login', widget=forms.TextInput(attrs={'class': 'form-control'}))
	email = forms.EmailField(label='email', widget=forms.EmailInput(attrs={'class': 'form-control'}))
	password1 = forms.CharField(label='password1', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
	password2 = forms.CharField(label='password2', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
	class Meta:
		model = User
		fields = {'username','email','password1','password2'}
		

class LoginUserForm(AuthenticationForm):
	username = forms.CharField(label='login', widget=forms.TextInput(attrs={'class': 'form-control'}))
	password = forms.CharField(label='password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))