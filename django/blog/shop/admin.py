from django.contrib import admin
from shop.models import Product


@admin.register(Product)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "cost", "photo", "choise", )
    fields = ("title", "cost", "photo", "choise", )
    search_fields = ("title",)
