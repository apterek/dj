import logging
import requests
from django.db.models import F
from django_rq import job
import datetime
from shop.models import Product

logger = logging.getLogger(__name__)
CURRCOV_API_KEY = "37f1f0ad28d970fb8fd3"


@job
def run_products_update():
    Product.objects.filter(cost=0).update(status="OUT_OF_STOCK")
    logger.info(f"Products updated successfully: {datetime.datetime.now()}")


@job
def run_update_exchange_rate():
    url = f"https://free.currconv.com/api/v7/convert?q=USD_BYN&compact=ultra&apiKey={CURRCOV_API_KEY}"
    response = requests.get(url)
    if response.status_code != 200:
        logger.error("Something gone wrong, try again")

    exchange_rate = response.json().get("USD_BYN")
    Product.objects.update(price_byn=F("cost") * exchange_rate)
    logger.info(f"Exchange rate updated successfully: {datetime.datetime.now()}")
