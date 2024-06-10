from django import forms
from .models import Product, ProfileImage
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class ProfilePictureForm(forms.ModelForm):
	class Meta:
		model = ProfileImage
		fields = ['profile_picture','userId']


class ProductForm(forms.ModelForm):
	class Meta:
		model = Product
		fields = ['name', 'description', 'image','userId']


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    pass