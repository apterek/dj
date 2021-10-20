from django.conf import settings
from django.db import models


STATUS_CHOICES = (("IN_STOCK", "In Stock"), ("OUT_OF_STOCK", "Out Of Stock"), ("ALL_PRODUCT", "All products"))

ORDER_BY_CHOICES = (
    ("max_cost", "Max Cost"),
    ("max_count", "Max Count"),
)


class Product(models.Model):
    title = models.CharField(max_length=200, default=True)
    cost = models.IntegerField(null=True)
    photo = models.ImageField(
        upload_to='images/%Y/%m/%d/', null=True)  # /%Y/%m/%d/ - creating dir for each day, when download image
    description = models.TextField(default="")
    status = models.CharField(
        max_length=100, choices=STATUS_CHOICES, default="IN_STOCK"
    )
    favorites = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="favorite_products"
    )

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return f"{self.title}"


class Purchase(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name="purchases", on_delete=models.CASCADE, blank=True, null=True
    )
    product = models.ForeignKey(
        Product, related_name="purchases", on_delete=models.CASCADE, default=True, blank=True, null=True
    )
    count = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True, blank=True, null=True)

    class Meta:
        verbose_name = "Purchase"
        verbose_name_plural = "Purchases"

    def __str__(self):
        return f"{self.product}"


class Spider(models.Model):
    title = models.CharField(max_length=100)
    price = models.CharField(max_length=15)
    link = models.CharField(max_length=200)
    image_name = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        verbose_name = "Spider"
        verbose_name_plural = "Spiders"

    def __str__(self):
        return f"{self.title}"
