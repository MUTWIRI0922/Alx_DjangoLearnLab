from django.shortcuts import render
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Book
from .serializers import BookSerializer
from rest_framework import viewsets

# Create your views here.
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    # TokenAuthentication is used to authenticate API requests.
    # Users must include a valid token in the Authorization header.
    # Permissions ensure only authenticated users can access endpoints.
 
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    

    queryset = Book.objects.all()
    serializer_class = BookSerializer