from django.urls import include, path
from rest_framework import routers
from api.posts.views import PostViewSet
from api.product.views import ProductViewSet
from api.products.views import ProductsViewSet
from api.users.views import RegisterViewSet


app_name = "api"

router = routers.DefaultRouter()
router.register(r"posts", PostViewSet)
router.register(r"product", ProductViewSet)  # old lesson, from blog app
router.register(r"products", ProductsViewSet)
#router.register(r"users", RegisterViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path("api-auth/", include(
        "rest_framework.urls",
        namespace="rest_framework"
    )),

]
