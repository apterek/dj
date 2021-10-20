import pytest
from tests.factories import ProductFactory
from django.test import Client


@pytest.mark.django_db
class TestFilters:

    def setup_method(self):
        self.client = Client()
        self.url = "http://localhost:8000/api/products/"
        ProductFactory.create_batch(7)

    def test_api_products(self):
        test_filters = (
            "",
            "status=IN_STOCK",
            "status=OUT_OF_STOCK",
            "cost__gt=100",
            "cost__lt=100",
            "cost__gt=10&cost__lt=100",
            "status=IN_STOCK&cost__gt=10&cost__lt=100",
        )
        for query in test_filters:
            response = self.client.get(f"{self.url}?{query}")
            assert response.status_code == 200

