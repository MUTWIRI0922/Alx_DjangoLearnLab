from django.shortcuts import render
from rest_framework import serializers, permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters
from datetime import date
from .models import Book, Author
from .serializers import BookSerializer

# Create your views here.

class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = BookSerializer
    # Enable filtering, searching, and ordering
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    # Fields allowed for filtering
    filterset_fields = {
        'title': ['exact', 'icontains'],
        'publication_year': ['exact', 'gte', 'lte'],
        'author__name': ['icontains'],
    }

    # Fields allowed for searching
    search_fields = [
        'title',
        'author__name',
    ]

    # Fields allowed for ordering
    ordering_fields = [
        'title',
        'publication_year',
    ]

    # Default ordering
    ordering = ['title']

class BookDetailView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookCreateView(generics.CreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookUpdateView(generics.UpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDeleteView(generics.DestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Book.objects.all()
    serializer_class = BookSerializer