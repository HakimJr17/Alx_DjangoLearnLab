# LibraryProject/LibraryProject/urls.py
"""
URL configuration for LibraryProject project.
... (Django comments) ...
"""
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect 

# Helper function to redirect root to book list
def redirect_to_book_list(request):
    return redirect('relationship_app:book_list') # Redirects to the namespaced URL


urlpatterns = [
    path('admin/', admin.site.urls),
    # --- NEW: This handles the root URL ('/') ---
    path('', redirect_to_book_list, name='home'),
]