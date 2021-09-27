from django.conf import settings
from django.db import models


class Post(models.Model):
    objects = None
    title = models.CharField(max_length=200)
    image = models.ImageField(blank=True, null=True)
    slug = models.SlugField()
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True,
                               blank=True)
    tag = models.ForeignKey("Tag", on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=100)
    posts = models.ManyToManyField(Post, related_name="tags")

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"

    def __str__(self):
        return self.title


class User(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=32)
    age = models.IntegerField()

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.first_name, self.last_name


class Product(models.Model):
    product_name = models.CharField(max_length=25)
    product_cost = models.FloatField(max_length=10)
    description = models.TextField(max_length=200)
    vendor_code = models.IntegerField()
    serial_number = models.CharField(max_length=16)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return self.product_name


class Files(models.Model):
    title = models.CharField(max_length=200)
    file = models.FileField()

    class Meta:
        verbose_name = "File"
        verbose_name_plural = "Files"
        
    def __str__(self):
        return self.title
