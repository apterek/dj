from django.contrib import messages
from django.http import Http404
from django.shortcuts import render
import logging
from shop.models import Product, Purchase
from shop.forms import FormStatus, FilterDate
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
        elif request.user.is_authenticated and request.POST["action"] == "remove":
            product.favorites.remove(request.user)
            messages.info(request, "Product removed from favorites")
        elif request.user.is_authenticated and request.POST["action"] == "buy":
            Purchase.objects.create(user=request.user, product=product, count=int(request.POST["quantity"]))
            messages.info(request, "Product purchased")
    return render(request, "product/product_item.html", {"product": product,
                                                         "favorite_products": request.user in product.favorites.all()})


class PurchaseView(TemplateView):
    template_name = "product/product_purchases.html"

    def get_context_data(self, **kwargs):
        filter_form = FilterDate(self.request.GET)

        if self.request.user.is_authenticated:
            purchase = Purchase.objects.filter(user=self.request.user)
            if filter_form.is_valid():
                if filter_form.cleaned_data["filter_by_date"] == "NEW_FIRST":
                    purchase = Purchase.objects.filter(user=self.request.user).order_by("-created_at")
            return {"purchases": purchase, "form": filter_form}
        else:
            raise Http404


def view_resume(request):
    return render(request, "resume.html")
