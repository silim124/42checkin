from django.contrib import admin
from django.urls import path, include

from core.root_views import api_doc_view
from cadet import urls as cadet_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path("doc", api_doc_view.with_ui("redoc", cache_timeout=0), name="api_doc"),
    path("cadet/", include(cadet_urls, namespace="cadet")),
]
