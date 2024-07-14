from django.shortcuts import redirect, render
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated
from .forms import SignupForm


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
