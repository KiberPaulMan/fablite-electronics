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
    # Страница регистрации пользователя
    path('register/', views.register_page, name='register'),
    # Страница после успешной регистрации
    path('success/', views.successful_registration, name='success_register'),
    # Получние access токена и обновление через refresh токен
    path('api/v1/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns += router.urls
