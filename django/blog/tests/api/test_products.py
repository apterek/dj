"""import pytest
from rest_framework import status
from rest_framework.test import APIClient

from post.models import Post, Product


@pytest.mark.django_db
class TestPostsApi:
    def setup_method(self):
        self.client = APIClient()

    def test_product(self):
        product = Product.objects.create(product_name='touchpad', product_cost=10,
                                         description='asdasdfsa', vendor_code=12124,
                                         serial_number='SN1412ASD2')
        response = self.client.get("/api/product/")
        assert response.status_code == status.HTTP_200_OK
        assert response.data["results"][0]["product_name"] == product.product_name
"""