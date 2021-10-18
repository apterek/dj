import requests
from django.db.models import Sum, F
from django.shortcuts import render, redirect
import logging
from shop.models import Product, Purchase
from shop.forms import FormStatus
from shop.spiders import OmaSpider

logger = logging.getLogger(__name__)


def product_list(request):
    products = Product.objects.all()
    form = FormStatus(request.GET)
    if form.is_valid():
        if form.cleaned_data["status"] == "IN_STOCK":
            products = products.filter(status="IN_STOCK")
        if form.cleaned_data["status"] == "OUT_OF_STOCK":
            products = products.filter(status="OUT_OF_STOCK")
        if form.cleaned_data["cost__gt"]:
            products = products.filter(cost__gt=form.cleaned_data["cost__gt"])
        if form.cleaned_data["cost__lt"]:
            products = products.filter(cost__lt=form.cleaned_data["cost__lt"])
        if form.cleaned_data["order_by"]:
            order_by = form.cleaned_data["order_by"]
            if order_by == "max_count":
                products = products.annotate(
                    total_count=Sum("purchases__count")
                ).order_by("-total_count")
            if order_by == "max_cost":
                products = products.annotate(
                    total_cost=Sum("purchases__count") * F("cost")).order_by("-total_cost")

    else:
        form = FormStatus()

    return render(request, "product_list.html", {"products": products,
                                                 "form": form})


def product_view(request, **kwargs):
    product = Product.objects.get(id=kwargs["product_id"])
    if request.method == "POST":
        if request.user.is_authenticated and request.POST["action"] == "add":
            product.favorites.add(request.user)
        else:
            product.favorites.remove(request.user)
    return render(request, "product_item.html", {"product": product,
                                                 "favorite_products": request.user in product.favorites.all()})

