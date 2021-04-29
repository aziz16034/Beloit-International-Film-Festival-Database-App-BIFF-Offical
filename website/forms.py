from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Post



class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class LoginForm(forms.Form):
    email = forms.EmailField(label='Courriel')
    password = forms.CharField(label='Mot de passe',
                        widget = forms.PasswordInput)




