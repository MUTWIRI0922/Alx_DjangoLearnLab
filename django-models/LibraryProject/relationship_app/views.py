from django.shortcuts import render
from django.http import HttpResponse
from .models import Author, Book, Librarian
from .models import Library
from django.views.generic.detail import DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponse("Signup successful!")
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponse("Login successful!")
        else:
            return HttpResponse("Invalid login credentials.")
    return render(request, 'login.html')
def logout(request):
    pass



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