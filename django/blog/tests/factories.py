import factory
import datetime
from factory.django import DjangoModelFactory, DjangoOptions
from shop.models import Product, Purchase
from django.contrib.auth.models import User


class ProductFactory(DjangoModelFactory):
    class Meta:
        model = Product

    title = factory.Sequence(lambda n: f"product-{n}")
    cost = factory.Sequence(lambda n: 35 * n)
    description = "Product description"
    status = "IN_STOCK"


class UserFactory(DjangoModelFactory):
    def __init__(self, password):
        self.password = password

    class Meta:
        model = User
        django_get_or_create = ('username', 'email', 'password',)

    username = 'apterek-test'
    email = 'apterek-test@mail.ru'
    password = '12345678'


class PurchaseFactory(DjangoModelFactory):
    class Meta:
        model = Purchase

    user = factory.SubFactory(UserFactory)
    product = factory.SubFactory(ProductFactory)
    count = factory.Sequence(lambda n: 2 * n)
    created_at = datetime.datetime.now()
