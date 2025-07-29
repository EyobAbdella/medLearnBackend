from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions


admin.site.site_header = "Mulhim Admin Panel"
admin.site.index_title = "CME Course & E-commerce Management"


schema_view = get_schema_view(
    openapi.Info(
        title="Med Learn API",
        default_version="v1",
        description="API documentation with Swagger UI",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/admin/", include("administrator.urls")),
    path("api/", include("course.urls")),
    path("api/", include("core.urls")),
    # Djoser for JWT token management
    # path("auth/", include("djoser.urls")),
    # path("auth/", include("djoser.urls.jwt")),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=300),
        name="schema-swagger-ui",
    ),
    path(
        "redoc/", schema_view.with_ui("redoc", cache_timeout=300), name="schema-redoc"
    ),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
