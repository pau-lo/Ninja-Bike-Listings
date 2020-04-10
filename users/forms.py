from django import forms
from django.contrib.auth.forms import UserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email', 'street', 'city',
                  'state', 'zip_code', 'phone', 'age')


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = CustomUser
        fields = ('username', 'email', 'street', 'city',
                  'state', 'zip_code', 'phone', 'age')
