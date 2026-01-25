from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import User
from django.shortcuts import redirect
from .forms import UserCreationForm, UserChangeForm
from .models import Book
from django.db.models import Q
# Create your views here.

def book_list(request):
    query = request.GET.get('q')

    if query:
        # Safe ORM filtering (prevents SQL injection)
        books = Book.objects.filter(
            Q(title__icontains=query) |
            Q(author__icontains=query)
        )
    else:
        books = Book.objects.all()

    return render(request, 'bookshelf/book_list.html', {'books': books})


@permission_required('bookshelf.can_view', raise_exception=True)
def view_users(request):
    users = User.objects.all()
    return render(request, 'bookshelf/view_users.html')

@permission_required('bookshelf.can_create', raise_exception=True)
def add_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():

            form.save()
            return redirect('view_users')
    else:
        form = UserCreationForm()
    return render(request, 'bookshelf/add_user.html', {'form': form})
@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_user(request, user_id):
    user = User.objects.get(id=user_id)
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('view_users')
    else:
        form = UserChangeForm(instance=user)
    return render(request, 'bookshelf/edit_user.html', {'form': form, 'user': user})
@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_user(request, user_id):
    user = User.objects.get(id=user_id)
    user.delete()
    return redirect('view_users')
