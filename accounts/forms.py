from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from accounts.models import ProfileUser


class ProfileForm(forms.ModelForm):
    class Meta:
        model = ProfileUser
        fields = ('company',)


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username',)


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
