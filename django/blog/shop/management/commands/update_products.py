from django.core.management.base import BaseCommand
from shop.task import run_products_update


class Command(BaseCommand):
    help = "Update products in status in stock  with cost = 0 to out of stock"

    def handle(self, *args, **options):
        run_products_update.delay()
        print("OK")
