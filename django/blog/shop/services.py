from django.db.models import Sum, F, QuerySet


def product_filter(products: QuerySet, cost__gt: int = None, cost__lt: int = None, status: str = None,
                   order_by: str = None,) -> QuerySet:
    if status == "IN_STOCK":
        products = products.filter(status=status)
    if status == "OUT_OF_STOCK":
        products = products.filter(status=status)
    if cost__gt:
        products = products.filter(cost__gt=cost__gt)
    if cost__lt:
        products = products.filter(cost__lt=cost__lt)
    if order_by:
        order_by = order_by
        if order_by == "max_count":
            products = products.annotate(
                total_count=Sum("purchases__count")
            ).order_by("-total_count")
        if order_by == "max_cost":
            products = products.annotate(
                total_cost=Sum("purchases__count") * F("cost")).order_by("-total_cost")
    return products
