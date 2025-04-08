from . import views
from rest_framework.routers import DefaultRouter

app_name = "api-v1"

# Generating urls via DefaultRouter
router = DefaultRouter()
router.register("post", views.PostModelViewSet, basename="post")
router.register("category", views.CategoryModelViewSet, basename="category")
urlpatterns = router.urls
