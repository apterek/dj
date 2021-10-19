import scrapy
import logging
from shop.models import Spider
from blog.settings import MEDIA_ROOT

logger = logging.getLogger(__name__)


class OmaSpider(scrapy.Spider):
    name = "oma.by"
    allowed_domains = ["https://www.oma.by"]
    start_urls = ["https://www.oma.by/elektroinstrument-c"]
    ITEM_PIPELINES = {
        'scrapy.pipelines.images.ImagesPipeline': 1
    }
    IMAGES_STORE = '/home/danila/django/dj/django/blog/media/'

    def parse(self, response, **kwargs):

        for product in response.css(".catalog-grid .product-item"):
            data = {
                "title": product.css(".product-title-and-rate-block .wrapper::text").get().strip(),
                "price": product.css(".product-price-block .price__normal::text").get().strip(),
                "link": f"{self.allowed_domains[0]}{product.css('a.area-link::attr(href)').get()}",
                "image_urls": f'https://www.oma.by/{product.css("img.catlg_list_img::attr(data-src)").get().strip()}',
            }
            clean_image_urls = [data["image_urls"]]

            if data:
                Spider.objects.create(title=data["title"], price=data["price"], link=data["link"])

            yield data, clean_image_urls

            NEXT_PAGE_SELECTOR = 'a.btn.btn__light.btn__bigger.btn__page-nav.btn__nav-right.js_scroll_top::attr(href)'
            next_page = response.css(NEXT_PAGE_SELECTOR).extract_first()
            if next_page:
                yield scrapy.Request(
                    response.urljoin(next_page),
                    callback=self.parse)
