from rest_framework import viewsets

from api.product.serializers import ProductSerializer
from post.models import Product


class Product1ViewSet(viewsets.ModelViewSet):
    """
   API endpoint that allows posts to be viewed.
   """

    queryset = Product.objects.all().order_by("serial_number")
    serializer_class = ProductSerializer
    permission_classes = []
