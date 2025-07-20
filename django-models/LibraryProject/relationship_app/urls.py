# relationship_app/urls.py
from django.urls import path, include # Make sure to import 'include'
from . import views # Import views from the current app
from relationship_app.views import LibraryDetailView # Import the class-based view explicitly
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy # NEW: Import reverse_lazy for LogoutView redirect



app_name = 'relationship_app' # Namespace for URLs (good practice)

urlpatterns = [
    # Existing URL patterns
    path('books/', views.book_list, name='book_list'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),

    # --- NEW: Authentication URL patterns ---
    # Login URL
    path('accounts/login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),

    # Logout URL
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page=reverse_lazy('relationship_app:login')), name='logout'), # Use reverse_lazy for next_page

    # Registration URL (using our custom view)
    path('accounts/register/', views.register, name='register'),
]