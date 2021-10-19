from rest_framework import viewsets

from api.products.serializers import ProductsSerializer, ProductFiltersSerializer
from shop.models import Product
from shop.services import product_filter


class ProductsViewSet(viewsets.ModelViewSet):
    """
   API endpoint that allows posts to be viewed.
   """

    queryset = Product.objects.all().order_by("cost")
    serializer_class = ProductsSerializer
    permission_classes = []

    def filter_queryset(self, queryset):
        filter_serializer = ProductFiltersSerializer(data=self.request.query_params)
        filter_serializer.is_valid(raise_exception=True)
        return product_filter(queryset, **filter_serializer.validated_data)
