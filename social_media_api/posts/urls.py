from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, user_feed
from django.urls import path, include

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'comments', CommentViewSet, basename='comment')

urlpatterns = router.urls + [
    path('feed/', user_feed, name='user_feed'),
    path('posts/<int:pk>/like/', PostViewSet.as_view({'post': 'like'}), name='post-like'),
    path('posts/<int:pk>/unlike/', PostViewSet.as_view({'post': 'unlike'}), name='post-unlike'),

]