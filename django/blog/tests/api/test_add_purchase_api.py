from rest_framework.test import APIClient
from rest_framework import status
import pytest
from django.urls import reverse
from shop.models import Product
from tests.factories import UserFactory, ProductFactory
import factory


@pytest.mark.django_db
class TestRegisterApi:
    def setup_method(self):
        self.client = APIClient()

    def test_add_purchase(self):
        # test with fake user
        response = self.client.post(reverse("api:add_purchase-list"),
                                    {
                                        "user": "fake_user",
                                        "product": "test_product",
                                        "count": 3802
                                    })
        assert response.status_code == status.HTTP_404_NOT_FOUND
        # test with fake product
        response = self.client.post(reverse("api:add_purchase-list"),
                                    {
                                        "user": "apterek",
                                        "product": "fake_product",
                                        "count": 3802
                                    })
        assert response.status_code == status.HTTP_404_NOT_FOUND
        # test if "count" it isn't a digit
        response = self.client.post(reverse("api:add_purchase-list"),
                                    {
                                        "user": "apterek",
                                        "product": "test_product",
                                        "count": "aaaaaa"
                                    })
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        # test right request
        response = self.client.post(reverse("api:add_purchase-list"),
                                    {
                                        "user": "apterek",
                                        "product": "product_1",
                                        "count": 3802
                                    })
        assert response.status_code == status.HTTP_201_CREATED




