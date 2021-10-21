from rest_framework import viewsets, status
from rest_framework.generics import CreateAPIView
import datetime
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.purchase.serializers import PurchaseViewSerializer, UserSerializer, AddPurchasesSerialezer
from shop.models import Purchase, Product
from django.contrib.auth.models import User


class PurchaseUserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PurchaseViewSet(viewsets.ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseViewSerializer
    permission_classes = []


class AddPurchaseViewSet(CreateAPIView, viewsets.GenericViewSet):
    serializer_class = AddPurchasesSerialezer
    permission_classes = []

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        purchase = None
        user = serializer.validated_data["user"]
        product = serializer.validated_data["product"]
        try:
            count = int(serializer.validated_data["count"])
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        if user in [user_list for user_list in User.objects.all()] \
                and product in [product_list for product_list in Product.objects.all()]:
            purchase = Purchase.objects.create(
                user=user,
                product=product,
                count=count,
                created_at=datetime.datetime.now()
            )
        if purchase:
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
