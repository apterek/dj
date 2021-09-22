from django.core.management.base import BaseCommand
from post.models import Post
import csv


class Command(BaseCommand):

    def handle(self, *args, **options):
        print(args)
        with open("file_with_all_post.csv", "a") as file:
            writer = csv.writer(file)
            for post in Post.objects.all():
                writer.writerow([post.title, post.slug, post.created_at])
                print(post.title, post.slug, post.created_at)
