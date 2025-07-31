from rest_framework_nested.routers import DefaultRouter, NestedDefaultRouter
from .views import (
    CartItemViewSet,
    CartViewSet,
    CourseViewSet,
    OrderViewSet,
    ReportViewSet,
)

router = DefaultRouter()
router.register("cart", CartViewSet, basename="cart")
router.register(r"courses", CourseViewSet, basename="courses")
router.register("orders", OrderViewSet, basename="orders")


report_router = NestedDefaultRouter(router, r"courses", lookup="course")
report_router.register(r"reports", ReportViewSet, basename="course-reports")

cart_router = NestedDefaultRouter(router, "cart", lookup="cart")
cart_router.register("items", CartItemViewSet, basename="cart-items")

urlpatterns = router.urls + report_router.urls + cart_router.urls
