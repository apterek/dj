from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from post.views import all_post, add_post
from shop.views import product_view, ProductViwe, PurchaseView, view_resume

urlpatterns = [
    path("admin/", admin.site.urls),
    # path("", posts_index),
    path("api/auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("api/", include("api.urls", namespace="api",)),
    path("post/", all_post, name="post"),
    path("add_post/", add_post, name="add_post"),
    path("", ProductViwe.as_view(), name="product"),
    path("product/<int:product_id>/", product_view, name="product_view"),
    path("purchases/", PurchaseView.as_view(), name="purchases"),
    path("django-rq/", include("django_rq.urls")),
    path("resume/", view_resume, name="resume")
]

if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
