from django.core.management.base import BaseCommand
from post.models import Post
import csv


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('filename', type=str)

    def handle(self, *args, **options):
        all_post = Post.objects.all()
        with open(options["filename"], "r") as file:
            reader = csv.reader(file)
            for row in reader:
                coincidence = False
                for post in all_post:
                    if post.title == row[0]:
                        coincidence = True
                if not coincidence:
                    Post.objects.create(title=row[0], slug=row[1])
