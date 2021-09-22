from django.core.management.base import BaseCommand
from post.models import Post
import csv


class Command(BaseCommand):

    def handle(self, *args, **options):
        with open("file_with_all_post.csv", "w") as file:
            writer = csv.writer(file)
            writer.writerow(["title", "image", "slug", "created_at", "author", "tag"])
            for post in Post.objects.all():
                writer.writerow([post.title, post.image, post.slug,
                                 post.created_at, post.tag])

