import pytest
from django.urls import reverse

from tests.factories import ProductFactory
from django.test import Client


@pytest.mark.django_db
class TestFilters:
    def setup_method(self):
        self.client = Client()
        self.url = reverse("products_view")
        ProductFactory.create_batch(10)

    def test_product_list(self):
        test_filters = (
            "",
            "order_by=price__gt",
            "order_by=price__lt",
            "order_by=max_count",
            "order_by=max_cost",
            "status=IN_STOCK",
            "status=OUT_OF_STOCK",
            "cost__gt=100",
            "cost__lt=100",
            "cost__gt=10&cost__lt=100",
            "status=IN_STOCK&cost__gt=10&cost__lt=100",
            "order_by=max_count&status=IN_STOCK&cost__gt=10&cost__lt=100",
            "order_by=max_cost&cost__gt=10",
        )

        for query in test_filters:
            response = self.client.get(f"{self.url}?{query}")
            assert response.status_code == 200

    def test_product_filters_validation(self, client):
        response = self.client.get(f"{self.url}?price__gt=10&price__lt=100")
        assert response.status_code == 200
        assert not response.context["filters_form"].errors

        response = self.client.get(f"{self.url}?cost__gt=100&cost__lt=10")
        assert response.status_code == 200
        assert response.context["filters_form"].errors
