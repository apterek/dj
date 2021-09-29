from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from post.views import all_post, add_post
from shop.views import product_list


urlpatterns = [
    path("admin/", admin.site.urls),
    # path("", posts_index),
    path("api/", include(
        "api.urls", namespace="api"
    )),
    path("", all_post),
    path("add_post/", add_post, name="add_post"),
    path("shop/", product_list, name="product")
]

if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
