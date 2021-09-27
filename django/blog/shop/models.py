from django.conf import settings
from django.db import models


class Product(models.Model):
    product_name = models.CharField()
    vendor = models.CharField(max_length=40)
    cost = models.FloatField()
    quantity = models.IntegerField()
    photo = models.ImageField(
        upload_to='images/%Y/%m/%d/')  # /%Y/%m/%d/ - creating dir for each day, when download image

    class Meta:
        verbouse_name = "Product"
        verbouse_name_plural = "Products"

    def __str__(self):
        return self.product_name


class Purchase(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey("User", on_delete=models.CASCADE)
    purchases = models.IntegerField()

    class Meta:
        verbouse_name = "Purchase"
        verbouse_name_plural = "Purchases"


class User(models.Model):
    user_name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True,
                                  blank=True)
    email = models.EmailField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        verbouse_name = "User"
        verbouse_name_plural = "Users"

    def __str__(self):
        return self.user_name
