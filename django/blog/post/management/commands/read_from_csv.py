from django.core.management.base import BaseCommand
from post.models import Post
import csv


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument("--filename")

    def handle(self, *args, **options):
        with open(options["filename"], "a+") as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
