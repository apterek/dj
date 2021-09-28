from django.conf import settings
from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=200, default=True)
    cost = models.IntegerField(null=True)
    photo = models.ImageField(
        upload_to='images/%Y/%m/%d/', null=True)  # /%Y/%m/%d/ - creating dir for each day, when download image

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return self.title


class Purchase(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name="purchases", on_delete=models.CASCADE, blank=True, null=True
    )
    product = models.ForeignKey(
        Product, related_name="purchases", on_delete=models.CASCADE, default=True
    )
    count = models.IntegerField(null=True)

    class Meta:
        verbose_name = "Purchase"
        verbose_name_plural = "Purchases"
