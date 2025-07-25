from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "Mulhim Admin Panel"
admin.site.index_title = "CME Course & E-commerce Management"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/admin/", include("administrator.urls")),
    path("api/", include("core.urls")),
    # Djoser for JWT token management
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.jwt")),
]
