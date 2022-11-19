from rest_framework.routers import SimpleRouter
from .views import PostViewSet, CategoryViewSet

router = SimpleRouter()

router.register('categories_list', CategoryViewSet, basename='category')
router.register('posts_list', PostViewSet, basename='post')

urlpatterns = []

urlpatterns += router.urls
