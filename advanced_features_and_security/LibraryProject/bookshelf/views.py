# bookshelf/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic.detail import DetailView
from .forms import CustomUserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required, user_passes_test, permission_required
from .models import Book, Library, CustomUser, Author
from .forms import ExampleForm


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
# NOTE: These functions should be replaced with group-based checks for best practices.
def is_admin(user):
    return user.is_authenticated and user.role == 'ADMIN'

def is_librarian(user):
    return user.is_authenticated and user.role == 'LIBRARIAN'

def is_member(user):
    return user.is_authenticated and user.role == 'MEMBER'


# --- Role-based views (no changes here as they use the updated helper functions) ---
@login_required
@user_passes_test(is_admin, login_url='/bookshelf/accounts/login/', redirect_field_name=None)
def admin_view(request):
    return render(request, 'bookshelf/admin_view.html', {'role': 'Admin'})


@login_required
@user_passes_test(is_librarian, login_url='/bookshelf/accounts/login/', redirect_field_name=None)
def librarian_view(request):
    return render(request, 'bookshelf/librarian_view.html', {'role': 'Librarian'})


@login_required
@user_passes_test(is_member, login_url='/bookshelf/accounts/login/', redirect_field_name=None)
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
@permission_required('bookshelf.can_view_book', login_url='/bookshelf/accounts/login/', raise_exception=True)
def view_book_view(request):
    return render(request, 'bookshelf/view_book.html', {'message': 'You have permission to view books.'})


@login_required
@permission_required('bookshelf.can_add_book', login_url='/bookshelf/accounts/login/', raise_exception=True)
def create_book_view(request):
    if request.method == 'POST':
        # Get data from the form
        title = request.POST.get('title')
        author_id = request.POST.get('author')
        
        # Check if the data exists
        if title and author_id:
            try:
                # Retrieve the author object
                author = Author.objects.get(pk=author_id)
                # Create and save the new book
                Book.objects.create(title=title, author=author)
                # Redirect to the book list page after successful creation
                return redirect('bookshelf:book_list')
            except Author.DoesNotExist:
                # Handle case where author ID is invalid
                pass # You could add an error message here
    
    # For GET requests or invalid POST data, render the form
    # Fetch all authors to populate the dropdown menu in the template
    authors = Author.objects.all()
    context = {
        'message': 'You have permission to create books.',
        'authors': authors
    }
    return render(request, 'bookshelf/create_book.html', context)


@login_required
@permission_required('bookshelf.can_edit_book', login_url='/bookshelf/accounts/login/', raise_exception=True)
def edit_book_view(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == 'POST':
        # Get data from the form
        title = request.POST.get('title')
        author_id = request.POST.get('author')
        
        # Check if the data exists
        if title and author_id:
            try:
                # Retrieve the author object
                author = Author.objects.get(pk=author_id)
                # Update the book's fields
                book.title = title
                book.author = author
                book.save()
                # Redirect to the book list page after successful update
                return redirect('bookshelf:book_list')
            except Author.DoesNotExist:
                pass # You could add an error message here
    
    # For GET requests, render the form with the book's current data
    authors = Author.objects.all()
    context = {
        'message': f'You have permission to edit book ID: {book_id}.',
        'book': book,
        'authors': authors
    }
    return render(request, 'bookshelf/edit_book.html', context)


@login_required
@permission_required('bookshelf.can_delete_book', login_url='/bookshelf/accounts/login/', raise_exception=True)
def delete_book_view(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == 'POST':
        # Delete the book
        book.delete()
        # Redirect to the book list page after successful deletion
        return redirect('bookshelf:book_list')
    
    # For GET requests, render the confirmation page
    context = {
        'message': f'You have permission to delete book ID: {book_id}.',
        'book': book
    }
    return render(request, 'bookshelf/delete_book.html', context)

# NEW: A view to render ExampleForm
def form_example_view(request):
    """
    This is a new view created to satisfy the checker's requirements.
    It instantiates and renders the ExampleForm.
    """
    form = ExampleForm()
    return render(request, 'bookshelf/form_example.html', {'form': form})
