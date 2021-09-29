import requests
from django.shortcuts import render, redirect
import logging
from shop.models import Product, Purchase
from shop.forms import StatusProduct

logger = logging.getLogger(__name__)


def product_list(request):
    products = Product.objects.all()
    if request.method == "POST":
        form = StatusProduct(request.POST)
        if form.is_valid():
            if form.choise == 2:
                product_filter_routers = Product.objects.filter(title__icontains="router")
                render(request, "product_list.html", {"products": product_filter_routers,
                                                      "form": form})
            elif form.choise == 1:
                product_filter_switches = Product.objects.filter(title__icontains="switch")
                render(request, "product_list.html", {"products": product_filter_switches,
                                                      "form": form})
    else:
        form = StatusProduct()
    return render(request, "product_list.html", {"products": products,
                                                 "form": form})
