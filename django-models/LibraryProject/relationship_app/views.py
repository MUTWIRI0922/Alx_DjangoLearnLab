from django.shortcuts import render
from django.views.generic import DetailView
from django.http import HttpResponse
from .models import Author, Book, Librarian
from .models import Library

# Create your views here.
def index(request): 
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, 'relationship_app/list_books.html', context)


class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['librarian'] = self.object.librarian
        context['books'] = self.object.books.all()
        return context