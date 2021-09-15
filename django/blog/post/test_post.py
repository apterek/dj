from django.test import TestCase, RequestFactory
from post.models import Post, Tag, Product
import pytest
from rest_framework import status
from rest_framework.test import APIClient


class TestPost(TestCase):
    def test(self):
        responce = self.client.get("/api/posts/")
        self.assertEqual(responce.status_code, 200)


@pytest.mark.django_db
class TestPostsApi:
    def setup_method(self):
        self.client = APIClient()

#    def test_posts_api(self):
#        post = Post.objects.create(title='testing', slug='test', text='text_testing')
#        response = self.client.get("/api/posts/")
#        assert response.status_code == status.HTTP_200_OK
#        assert response.data["results"][0]["title"] == post.title

    def test_product(self):
        product = Product.objects.create(product_name='touchpad', product_cost=10,
                                         description='asdasdfsa', vendor_code=12124,
                                         serial_number='SN1412ASD2')
        response = self.client.get("/api/product/")
        assert response.status_code == status.HTTP_200_OK
        assert response.data["results"][0]["product_name"] == product.product_name
