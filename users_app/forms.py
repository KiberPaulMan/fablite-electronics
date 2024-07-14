from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


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
