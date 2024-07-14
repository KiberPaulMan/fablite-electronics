from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import Form
from django import forms


class SignupForm(UserCreationForm):
    """ Форма регистрации нового пользователя"""
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    def clean(self):
        """ Проверка уникальнисти email"""
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            self.add_error('email', 'Such email already exists')
        return self.cleaned_data


class AuthUserForm(Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)
