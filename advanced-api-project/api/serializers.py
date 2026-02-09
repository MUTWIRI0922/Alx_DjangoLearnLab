from rest_framework import serializers
from django.shortcuts import render
from datetime import date
from .models import Book, Author

# Create your views here.
    # BookSerializer is a serializer for the Book model, converting model instances to JSON and vice versa.
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    def validate_publication_year(self,value):
        current_year = date.today().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

    
    # AuthorSerializer is a serializer for the Author model, converting model instances to JSON and vice versa.
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']