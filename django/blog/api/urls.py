from django.urls import include, path
from rest_framework import routers
from api.posts.views import PostViewSet2
from api.product.views import PostViewSet

app_name = "api"

router = routers.DefaultRouter()
router.register(r"posts", PostViewSet2)
router.register(r"product", PostViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path("api-auth/", include(
        "rest_framework.urls",
        namespace="rest_framework"
    )),
]
