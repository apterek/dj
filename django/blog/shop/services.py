from django.db.models import Sum, F, QuerySet


def product_filter(products: QuerySet, price__gt: int = None, price__lt: int = None,) -> QuerySet:
    if price__gt:
        products = products.filter(price__gt=price__gt)
    if price__lt:
        products = products.filter(price__lt=price__lt)
    return products
