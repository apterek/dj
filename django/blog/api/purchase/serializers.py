from rest_framework import serializers
from django.contrib.auth.models import User
from shop.models import Purchase, Product
from api.products.serializers import ProductsSerializer


class PurchaseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Purchase
        fields = ["product", "count", "created_at"]


class UserSerializer(serializers.ModelSerializer):
    user_purchases = PurchaseSerializer(many=True)

    class Meta:
        model = User
        fields = ["username", "user_purchases"]


class PurchaseViewSerializer(serializers.ModelSerializer):
    product = serializers.SerializerMethodField()

    def get_product(self, obj):
        return obj.product.title

    class Meta:
        model = Purchase
        fields = ["user", "product", "count", "created_at"]


class AddPurchasesSerialezer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = ["user", "product", "count", "created_at"]
