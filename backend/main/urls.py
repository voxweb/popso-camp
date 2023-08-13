from django.contrib import admin
from django.conf.urls import url
from django.urls import include, path, re_path
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


app_name = "main"

schema_view = get_schema_view(
    openapi.Info(
        title="Backend API", default_version="v1", description="API endpoints described here", terms_of_service=""
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    re_path(
        r"^api-docs/swagger(?P<format>\.json|\.yaml)$", schema_view.without_ui(cache_timeout=0), name="schema-json"
    ),
    re_path(r"^api-docs/swagger$", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    re_path(r"^api-docs/redoc$", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    path("api/v1/products/", include("products.urls")),
    path("admin/", admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
