from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


# User Models SingUp
class SingUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
