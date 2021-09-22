from django.core.management.base import BaseCommand
from post.models import Post
import csv
import requests


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("--file_out", type=str)

    def handle(self, *args, **options):
        CSV_URL = 'http://localhost:8000/media/example.csv'
        with requests.get(CSV_URL, stream=True) as r, open(options["file_out"], "w") as file:
            lines = (line.decode('utf-8') for line in r.iter_lines())
            writer = csv.writer(file)
            for row in csv.reader(lines):
                writer.writerow(row)
                Post.objects.create(title=row[0], slug=row[1], created_at=row[2])
