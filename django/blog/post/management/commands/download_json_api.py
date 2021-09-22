from django.core.management.base import BaseCommand
import csv
from rest_framework import status
import requests


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("--ip", type=str)
        parser.add_argument("--port", type=str)
        parser.add_argument("--file_out", type=str)
        parser.add_argument("--api", type=str)

    def handle(self, *args, **options):

        req = f"http://{options['ip']}:{options['port']}/api/{options['api']}"
        response = requests.get(req)

        if response.status_code == status.HTTP_200_OK:
            answer = response.json()["results"]
        else:
            return Exception('Something going wrong, Error: \n{}'.format(response.text))

        with open(options["file_out"], "w") as file:
            writer = csv.writer(file)
            for ans in answer:
                writer.writerow([ans["title"], ans["slug"],
                                 ans["created_at"]])


