from rest_framework.test import APIClient
from rest_framework import status
import pytest
from django.urls import reverse
from tests.factories import PurchaseFactory
from django.contrib.auth.models import User


@pytest.mark.django_db
class TestRegisterApi:
    def setup_method(self):
        self.client = APIClient()
        PurchaseFactory.create_batch(5)

    def test_api_purchase(self):
        response = self.client.get(reverse("api:user-list"))
        assert response.status_code == status.HTTP_200_OK
        assert response.data["count"] == User.objects.count()
        assert response.data["results"][0]["username"] == "apterek-test"
