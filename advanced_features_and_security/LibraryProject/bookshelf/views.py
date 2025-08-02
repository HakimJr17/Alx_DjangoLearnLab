# bookshelf/views.py
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic.detail import DetailView
from .forms import CustomUserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required, user_passes_test, permission_required
from .models import Book, Library, CustomUser


def book_list(request):
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, 'bookshelf/list_books.html', context)


class LibraryDetailView(DetailView):
    model = Library
    template_name = 'bookshelf/library_detail.html'
    context_object_name = 'library'


# --- UPDATED: Registration View to use a Custom Form ---
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST) # UPDATED: Use CustomUserCreationForm
        if form.is_valid():
            user = form.save()
            # Redirect to login page after successful registration
            return redirect('bookshelf:login')
    else:
        form = CustomUserCreationForm() # UPDATED: Use CustomUserCreationForm
    return render(request, 'bookshelf/register.html', {'form': form})


# --- UPDATED: Helper functions for role checks ---
def is_admin(user):
    # UPDATED: No need to check for hasattr(user, 'userprofile') anymore
    return user.is_authenticated and user.role == 'ADMIN'

def is_librarian(user):
    # UPDATED: No need to check for hasattr(user, 'userprofile') anymore
    return user.is_authenticated and user.role == 'LIBRARIAN'

def is_member(user):
    # UPDATED: No need to check for hasattr(user, 'userprofile') anymore
    return user.is_authenticated and user.role == 'MEMBER'


# --- Role-based views (no changes here as they use the updated helper functions) ---
@login_required
@user_passes_test(is_admin, login_url='/relationship/accounts/login/', redirect_field_name=None)
def admin_view(request):
    return render(request, 'bookshelf/admin_view.html', {'role': 'Admin'})


@login_required
@user_passes_test(is_librarian, login_url='/relationship/accounts/login/', redirect_field_name=None)
def librarian_view(request):
    return render(request, 'bookshelf/librarian_view.html', {'role': 'Librarian'})


@login_required
@user_passes_test(is_member, login_url='/relationship/accounts/login/', redirect_field_name=None)
def member_view(request):
    return render(request, 'bookshelf/member_view.html', {'role': 'Member'})


# --- UPDATED: Dashboard Redirect View ---
@login_required
def dashboard_redirect(request):
    # UPDATED: Check request.user.role directly
    if request.user.role == 'ADMIN':
        return redirect(reverse('bookshelf:admin_dashboard'))
    elif request.user.role == 'LIBRARIAN':
        return redirect(reverse('bookshelf:librarian_dashboard'))
    elif request.user.role == 'MEMBER':
        return redirect(reverse('bookshelf:member_dashboard'))
    # Fallback if no role or unknown role
    return redirect(reverse('bookshelf:book_list'))


@login_required
@permission_required('bookshelf.can_add_book', login_url='/relationship/accounts/login/', raise_exception=True)
def add_book_view(request):
    return render(request, 'bookshelf/add_book.html', {'message': 'You have permission to add books.'})


@login_required
@permission_required('bookshelf.can_change_book', login_url='/relationship/accounts/login/', raise_exception=True)
def change_book_view(request, book_id):
    return render(request, 'bookshelf/edit_book.html', {'message': f'You have permission to edit book ID: {book_id}.'})

@login_required
@permission_required('bookshelf.can_delete_book', login_url='/relationship/accounts/login/', raise_exception=True)
def delete_book_view(request, book_id):
    return render(request, 'bookshelf/delete_book.html', {'message': f'You have permission to delete book ID: {book_id}.'})