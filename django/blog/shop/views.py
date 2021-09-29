import requests
from django.shortcuts import render, redirect
import logging
from shop.models import Product, Purchase
from shop.forms import FormStatus

logger = logging.getLogger(__name__)


def product_list(request):
    products = Product.objects.all()
    form = FormStatus(request.GET)
    if form.is_valid():
        if form.cleaned_data["status"]:
            if form.cleaned_data["status"]:
                products = products.filter(status="IN_STOCK")
            if form.cleaned_data["cost__gt"]:
                products = products.filter(price__gt=form.cleaned_data["cost__gt"])
            if form.cleaned_data["cost__lt"]:
                products = products.filter(price__lt=form.cleaned_data["cost__lt"])
    else:
        form = FormStatus()
    return render(request, "product_list.html", {"products": products,
                                                 "form": form})
