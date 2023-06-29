from rest_framework import serializers
from djoser.serializers import UserCreateSerializer, UserDeleteSerializer
from .models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    # logo = serializers.ImageField(read_only=True)

    class Meta:
        model = CustomUser
        fields = (
            'first_name',
            'last_name',
            'middle_name',
            'avatar',
            'salary',
            'age',
            'department'
        )


class RegisterCustomUserSerializer(UserCreateSerializer):

    class Meta:
        model = CustomUser
        fields = (
            'first_name',
            'last_name',
            'middle_name',
            'avatar',
            'salary',
            'age',
            'username',
            'password',
            'department'
        )
        extra_kwargs = {
            'username': {'required': True},
            'password': {'required': True},
            'first_name': {'required': True},
            'last_name': {'required': True},
            'middle_name': {'required': True},
            'salary': {'required': True},
        }

