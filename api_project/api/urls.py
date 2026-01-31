from django.urls import path
from . import views
from rest_framework import routers
from .views import BookViewSet
from django.urls import include


router = routers.DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    path('books/', views.BookList.as_view(), name='book-list'),
    path('', include(router.urls)),


]