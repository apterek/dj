from rest_framework import serializers
from django.conf import settings


class RegisterUserSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=100)
    password = serializers.CharField(max_length=100, min_length=8)
