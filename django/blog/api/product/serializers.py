from rest_framework import serializers
from post.models import Product


class ProductSerializer(serializers.Serializer):
    product_name = serializers.CharField()
    product_cost = serializers.FloatField()
    vendor_code = serializers.IntegerField(read_only=True)
    serial_number = serializers.CharField(read_only=True)


