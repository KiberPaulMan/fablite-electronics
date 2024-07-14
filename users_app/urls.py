from drf_spectacular.utils import extend_schema
from rest_framework.routers import DefaultRouter
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from . import views


@extend_schema(tags=["Tokens"])
class CustomTokenObtainPairView(TokenObtainPairView):
    pass


@extend_schema(tags=["Tokens"])
class CustomTokenRefreshView(TokenRefreshView):
    pass


router = DefaultRouter()
router.register(r'api/v1/users', views.UserModelViewSet)

urlpatterns = [
    # Регистрация пользователя
    path('register/', views.register_page, name='register'),
    # Успешной регистрация
    path('success/', views.successful_registration, name='success_register'),
    # Аутентификация пользователя
    path('auth/', views.auth_user, name='auth_user'),

    # Получние access токена и обновление через refresh токен
    path('api/v1/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns += router.urls
