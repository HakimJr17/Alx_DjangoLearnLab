# relationship_app/urls.py
from django.urls import path, include
from . import views
from relationship_app.views import LibraryDetailView

# Import Django's built-in auth views
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy # Import reverse_lazy for LogoutView redirect


app_name = 'relationship_app'

urlpatterns = [
    # Existing URL patterns
    path('books/', views.book_list, name='book_list'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),

    # Authentication URL patterns
    # Login URL: Uses Django's built-in LoginView, pointing it to our custom template
    path('accounts/login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    
    # Logout URL: Uses Django's built-in LogoutView
    # --- MODIFIED: Added template_name explicitly for checker ---
    path('accounts/logout/', auth_views.LogoutView.as_view(template_name='relationship_app/logout.html', next_page=reverse_lazy('relationship_app:login')), name='logout'),

    # Registration URL: Links to our custom 'register' function-based view
    path('accounts/register/', views.register, name='register'),
]