from django.conf import settings
from django.db import models


class Post(models.Model):

    test = models.CharField(max_length=200, blank=True, null=True)
    title = models.CharField(max_length=200)
    image = models.ImageField(blank=True, null=True)
    slug = models.SlugField()
    text = models.TextField()
    created_at = models.DateTimeField(
        auto_now_add=True, db_index=True
    )


class Tag(models.Model):
    title = models.CharField(max_length=100)
    posts = models.ManyToManyField(Post, related_name="tags")

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"


class User(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=32)
    age = models.IntegerField()
