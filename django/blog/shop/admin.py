from django.contrib import admin
from shop.models import Product, Purchase


@admin.register(Product)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "cost", "photo", "status", )
    fields = ("title", "cost", "photo", "status", )
    search_fields = ("title",)


@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ("user", "product", "count", )
    fields = ("user", "product", "count", )
