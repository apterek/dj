import pytest
from rest_framework import status
import requests


@pytest.mark.django_db
class TestHomePage:

    def test_home_page(self):
        # previously run a server
        response = requests.get("http://127.0.0.1:8000/", verify=False)
        assert response.status_code == status.HTTP_200_OK
