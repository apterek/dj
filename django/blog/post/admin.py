from django.contrib import admin

from post.models import Post, Tag


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "created_at")
    fields = ("title", "image", "slug", "text", "created_at", "author", "test")
    readonly_fields = ("created_at",)
    search_fields = ("title", "slug", "text")


@admin.register(Tag)
class TagsAdmin(admin.ModelAdmin):
    list_display = ("title", )
    fields = ("title", )
    search_fields = ("title", )

