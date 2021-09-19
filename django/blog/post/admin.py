from django.contrib import admin

from post.models import Post, Tag


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "created_at", 'author',)
    fields = ("title", "image", "slug", "created_at", "author", )
    readonly_fields = ("created_at", )
    search_fields = ("author", "title", "slug", )


@admin.register(Tag)
class TagsAdmin(admin.ModelAdmin):
    list_display = ("title", )
    fields = ("title", "posts",)
    search_fields = ("title", )

