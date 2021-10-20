from rest_framework import viewsets, status
from rest_framework.response import Response
from api.purchase.serializers import PurchaseSerializer, UserSerializer
from shop.models import Purchase
from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView
import datetime


class PurchaseUserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PurchaseViewSet(viewsets.ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer

