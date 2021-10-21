import pytest
from django.urls import reverse

from tests.factories import PurchaseFactory
from django.test import Client


@pytest.mark.django_db
class TestFilters:
    def setup_method(self):
        self.client = Client()
        self.url = reverse("purchases")
        PurchaseFactory.create_batch(5)

    def test_purchase_view(self):
        response = self.client.get(f"{self.url}")
        assert response.status_code == 200

    def test_filter_by_date(self):
        test_filter_by_date = (
            "",
            "filter_by_date=NEW_FIRST"
            "filter_by_date=OLD_AT_FIRST"
        )
        for query in test_filter_by_date:
            response = self.client.get(f"{self.url}?{query}")
            assert response.status_code == 200
