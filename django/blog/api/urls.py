from django.urls import include, path
from rest_framework import routers
from api.posts.views import PostViewSet
from api.products.views import ProductsViewSet
from api.users.views import RegisterViewSet, LoginView, LogoutView
from api.purchase.views import PurchaseViewSet, PurchaseUserViewSet


app_name = "api"

router = routers.DefaultRouter()
router.register(r"posts", PostViewSet, "posts")
router.register(r"products", ProductsViewSet, "products")
router.register(r"register", RegisterViewSet, "register")
router.register(r"login", LoginView, "login")
router.register(r"logout", LogoutView, "logout")
router.register(r"purchase", PurchaseViewSet, "purchases")
router.register(r"user", PurchaseUserViewSet, "user")


urlpatterns = [
    path("", include(router.urls)),
    path("api-auth/", include(
        "rest_framework.urls",
        namespace="rest_framework"
    )),

]
