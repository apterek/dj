from rest_framework.test import APIClient
from rest_framework import status
import pytest
from django.urls import reverse


@pytest.mark.django_db
class TestRegisterApi:
    def setup_method(self):
        self.client = APIClient()

    def test_user_api(self):
        response = self.client.post(reverse("api:login-list"),
                                    {
                                        "username": "test_api",
                                        "password": "api123api123"
                                    })
        assert response.status_code == status.HTTP_404_NOT_FOUND

        response = self.client.post(reverse("api:register-list"),
                                    {
                                        "username": "test_api",
                                        "email": "test_api@api.ap",
                                        "password": "api123api123"
                                    })
        assert response.status_code == status.HTTP_201_CREATED

        response = self.client.post(reverse("api:login-list"),
                                    {
                                        "username": "test_api",
                                        "password": "api123api123"
                                    })
        assert response.status_code == status.HTTP_200_OK

        response = self.client.post(reverse("api:logout-list"),
                                    {
                                        "username": "test_api",
                                        "password": "api123api123"
                                    })
        assert response.status_code == status.HTTP_200_OK

