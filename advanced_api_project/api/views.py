from django.shortcuts import render
from rest_framework import serializers, permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from datetime import date
from .models import Book, Author
from .serializers import BookSerializer

# Create your views here.

class BookListView(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = BookSerializer
    ordering_fields = ['publication_year']
    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Book.objects.filter(author=user)
        return Book.objects.all()

class BookDetailView(generics.RetrieveAPIView):
    permission_classes = [permissions.AllowAny]

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