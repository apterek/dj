import factory
import datetime
from factory.django import DjangoModelFactory
from shop.models import Product, Purchase
from django.conf import settings
from django.test import Client


class ProductFactory(DjangoModelFactory):
    class Meta:
        model = Product

    title = factory.Sequence(lambda n: f"product-{n}")
    cost = factory.Sequence(lambda n: 35 * n)
    description = "Product description"
    status = "IN_STOCK"


class PurchaseFactory(DjangoModelFactory):
    class Meta:
        model = Purchase
    user = Client()
    
    count = factory.Sequence(lambda n: 2 * n)
    created_at = datetime.datetime.now()
