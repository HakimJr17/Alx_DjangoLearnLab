# relationship_app/views.py
from django.shortcuts import render
from django.views.generic import DetailView # Import DetailView for the class-based view
from .models import Book, Library # Import your Book and Library models

def book_list(request):
    """
    Function-based view to list all books.
    This view will render a simple text list of book titles and their authors.
    It passes a 'books' queryset to the template.
    """
    books = Book.objects.all() # Retrieve all Book objects from the database
    context = {
        'books': books # Pass the queryset as 'books' to the template
    }
    # Renders the 'list_books.html' template located in 'relationship_app/templates/relationship_app/'
    return render(request, 'relationship_app/list_books.html', context)

class LibraryDetailView(DetailView):
    """
    Class-based view to display details for a specific library,
    listing all books available in that library.
    Utilizes Django’s DetailView.
    """
    model = Library # Specifies that this view operates on the Library model
    template_name = 'relationship_app/library_detail.html' # Defines the template to be used for rendering
    context_object_name = 'library' # Sets the name of the context variable used in the template (e.g., {{ library.name }})

    # DetailView automatically fetches a single object based on the URL's primary key (pk) or slug.
    # The related books can then be accessed directly in the template using library.books.all()