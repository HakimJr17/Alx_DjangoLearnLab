# relationship_app/urls.py
from django.urls import path
from . import views # Import views from the current app
from relationship_app.views import LibraryDetailView # Import the class-based view explicitly
from .views import list_books

app_name = 'relationship_app' # Namespace for URLs (good practice)

urlpatterns = [
    # URL pattern for the function-based view (lists all books)
    # Accessible at /relationship/books/
    path('books/', views.book_list, name='book_list'),

    # URL pattern for the class-based view (details for a specific library)
    # Accessible at /relationship/library/<pk>/ (e.g., /relationship/library/1/)
    # The <pk> part captures the primary key from the URL
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]