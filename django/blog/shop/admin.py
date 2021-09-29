from django.contrib import admin
from shop.models import Product


@admin.register(Product)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "cost", "photo", "status", )
    fields = ("title", "cost", "photo", "status", )
    search_fields = ("title",)
