from django.core.management.base import BaseCommand
from shop.spiders import OmaSpider
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from shop.models import Spider


class Command(BaseCommand):
    help = "Crawl oma.by"

    def add_arguments(self, parser):
        parser.add_argument("--clear", type=str)

    def handle(self, *args, **options):
        if options["clear"]:
            Spider.objects.all().delete()
        process = CrawlerProcess(get_project_settings())
        process.crawl(OmaSpider)
        process.start()



