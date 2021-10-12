from rest_framework import viewsets

from api.products.serializers import ProductsSerializer
from shop.models import Product


class ProductsViewSet(viewsets.ModelViewSet):
    """
   API endpoint that allows posts to be viewed.
   """

    queryset = Product.objects.all().order_by("cost")
    serializer_class = ProductsSerializer
    permission_classes = []
