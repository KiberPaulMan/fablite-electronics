from django.shortcuts import redirect, render
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated
from .forms import SignupForm, AuthUserForm


def register_page(request):
    """ Регистрация нового пользователя"""
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_register')
    else:
        form = SignupForm()
    return render(request, 'users_app/register.html', {'form': form})


def successful_registration(request):
    """ Страница после успешной регистрации"""
    return render(request, 'users_app/success_register_user.html')


def auth_user(request):
    """Аутентификация пользователя"""
    if request.method == 'POST':
        form = AuthUserForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)

            context = {'is_form': False}

            if user is not None:
                context['message'] = f'Пользователь {username} аутентифицирован!'
            else:
                context['message'] = 'Нет такого пользователя с таким паролем!'

            return render(request, 'users_app/auth_user.html', context)
    else:
        form = AuthUserForm()
        return render(request, 'users_app/auth_user.html', {'form': form, 'is_form': True})


# Описание API документации
@extend_schema(tags=["Users"])
@extend_schema_view(
    list=extend_schema(
            summary='Получить список пользователей',
        ),
    retrieve=extend_schema(
        summary='Получить пользователя по id',
    ),
    update=extend_schema(
        summary='Изменение существующего пользователя по id',
    ),
    partial_update=extend_schema(
        summary='Частичное обновление существующего пользователя по id',
    ),
    create=extend_schema(
            summary="Создание нового пользователя",
        ),
    destroy=extend_schema(
        summary="Удалить пользователя по id",
    ),
)
class UserModelViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
