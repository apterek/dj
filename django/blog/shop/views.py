import requests
from django.contrib import messages
from django.db.models import Sum, F
from django.shortcuts import render, redirect
import logging
from shop.models import Product, Purchase
from shop.forms import FormStatus
from shop.spiders import OmaSpider
from django.views.generic import TemplateView
from shop.services import product_filter

logger = logging.getLogger(__name__)


class ProductViwe(TemplateView):
    template_name = "product/product_list.html"

    def get_context_data(self, **kwargs):
        products = Product.objects.all()
        form = FormStatus(self.request.GET)
        if form.is_valid():
            products = product_filter(products, **form.cleaned_data)
        else:
            form = FormStatus()
        return {"products": products, "form": form}


def product_view(request, **kwargs):
    product = Product.objects.get(id=kwargs["product_id"])
    if request.method == "POST":
        if request.user.is_authenticated and request.POST["action"] == "add":
            product.favorites.add(request.user)
            messages.info(request, "Product added to favorites")
        else:
            product.favorites.remove(request.user)
            messages.info(request, "Product removed from favorites")
    return render(request, "product/product_item.html", {"product": product,
                                                 "favorite_products": request.user in product.favorites.all()})
