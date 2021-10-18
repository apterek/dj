from django.core.management.base import BaseCommand
from shop.spiders import OmaSpider
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from shop.models import Spider


class Command(BaseCommand):
    help = "Crawl oma.by"
    Spider.objects.all().delete()

    def handle(self, *args, **options):

        process = CrawlerProcess(get_project_settings())
        process.crawl(OmaSpider)
        process.start()



