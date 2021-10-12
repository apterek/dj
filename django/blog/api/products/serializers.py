from rest_framework import serializers
from shop.models import STATUS_CHOICES
from shop.models import Product


class ProductsSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=200)
    cost = serializers.IntegerField()
    photo = serializers.ImageField()
    description = serializers.CharField()
    status = serializers.ChoiceField(choices=STATUS_CHOICES)


    def validate_status(self, value):
        if Product.objects.filter(status="IN_STOCK"):
            raise serializers.ValidationError("ONLY IN STOCK")
        return value

