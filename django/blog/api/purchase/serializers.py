from rest_framework import serializers
from django.contrib.auth.models import User
from shop.models import Purchase, Product


class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = ["user", "product", "count", "created_at"]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "user_purchases"]
