from django.contrib.auth.hashers import check_password
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User


class UserSerializer(ModelSerializer):
    password = serializers.CharField(max_length=255, write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'password']

    def create(self, validated_data):
        """Создание пользователя с проверкой уникальнисти email"""
        user_email = validated_data.get('email', None)
        if user_email and User.objects.filter(email=user_email).exists():
            raise serializers.ValidationError('A user with this email already exists')
        return User.objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        """Хеширование пароля при обновлении данных пользователя"""
        user_password = validated_data.pop('password', None)
        if user_password:
            if not check_password(user_password, instance.password):
                instance.set_password(user_password)
        return super().update(instance, validated_data)
