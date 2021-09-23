import pytest
from django import urls
from post.models import Post


@pytest.mark.django_db
class TestForm:

    @pytest.fixture
    def form_data(self):
        return {"title": "test_title", "slug": "slug_test"}

    def test_form(self, client, form_data):
        form_url = urls.reverse("add_post")
        response = client.post(form_url, form_data)
        assert response.status_code == 302
        # 302 code because we create redirect, after making a POST,
        # redirect client on the same URL (create GET request) with clean form,
        # line 37 in the views.py
        assert Post.objects.all().last().title == "test_title"
        # Check created post in database after POST request
