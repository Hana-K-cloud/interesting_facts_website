from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2')


# add fact form
class AddFact(forms.ModelForm):
    class Meta:
        model= Fact
        fields = ('topic', 'fact')
