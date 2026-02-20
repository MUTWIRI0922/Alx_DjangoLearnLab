from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, user_feed

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'comments', CommentViewSet, basename='comment')

urlpatterns = router.urls + [
    path('feed/', user_feed, name='user_feed'),
]