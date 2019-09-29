
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django.contrib.auth import authenticate
from django import forms


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = "__all__"


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = "__all__"
