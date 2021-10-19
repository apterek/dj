from rest_framework import serializers
from shop.models import STATUS_CHOICES, ORDER_BY_CHOICES
from shop.models import Product


class ProductsSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=200)
    cost = serializers.IntegerField()
    photo = serializers.ImageField()
    description = serializers.CharField()
    status = serializers.ChoiceField(choices=STATUS_CHOICES)


class ProductFiltersSerializer(serializers.Serializer):
    status = serializers.ChoiceField(
        choices=STATUS_CHOICES,
        required=False
    )
    cost__gt = serializers.IntegerField(
        min_value=0,
        required=False,
    )
    cost__lt = serializers.IntegerField(
        min_value=0,
        required=False,
    )
    order_by = serializers.ChoiceField(
        choices=ORDER_BY_CHOICES,
        required=False,
    )

    def validate(self, attrs):
        attrs = super().validate(attrs)
        cost__gt = attrs.get("cost__gt")
        cost__lt = attrs.get("cost__lt")
        if cost__gt and cost__lt and cost__gt > cost__lt:
            raise serializers.ValidationError(
                "Min price can't be greater than Max price"
            )
        return attrs


