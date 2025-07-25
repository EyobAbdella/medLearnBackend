from django.urls import path, include
from rest_framework_nested import routers
from .views import UserManagementViewSet

router = routers.SimpleRouter()
router.register(r"users", UserManagementViewSet, basename="users")

users_router = routers.NestedSimpleRouter(router, r"users", lookup="user")
users_router.register(r"details", UserManagementViewSet, basename="user-details")

urlpatterns = router.urls + users_router.urls
