import factory

from factory.django import DjangoModelFactory

from shop.models import Product


class ProductFactory(DjangoModelFactory):
    class Meta:
        model = Product

    title = factory.Sequence(lambda n: f"product-{n}")
    cost = factory.Sequence(lambda n: 35 * n)
    description = "Product description"
    status = "IN_STOCK"
