from django.shortcuts import render
from django.http import HttpResponse
from .models import Author, Book, Librarian
from .models import Library
from django.views.generic.detail import DetailView
from django.contrib.auth import login
from django.contrib.auth.decorators import permission_required, user_passes_test
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def is_admin(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def is_librarian(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def is_member(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

@user_passes_test(is_admin)
def Admin(request):
    return render(request, 'admin_view.html')

@user_passes_test(is_librarian)
def Librarian(request):
    return render(request, 'librarian_view.html')

@user_passes_test(is_member)
def Member(request):
    return render(request, 'member_view.html')

@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        published_date = request.POST.get('published_date')

        Book.objects.create(
            title=title,
            author=author,
            published_date=published_date
        )
        return redirect('book_list')

    return render(request, 'add_book.html')
@permission_required('relationship_app.can_change_book', raise_exception=True)
def change_book(request, book_id):
    book = Book.objects.get(id=book_id)
    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        book.published_date = request.POST.get('published_date')
        book.save()
        return redirect('book_list')

    return render(request, 'change_book.html', {'book': book})

@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, book_id):
    book = Book.objects.get(id=book_id)
    book.delete()
    return HttpResponse("Delete Book View")

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponse("Signup successful!")
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

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