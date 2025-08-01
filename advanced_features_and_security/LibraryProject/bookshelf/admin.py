# relationship_app/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin 
from .models import Author, Book, Library, Librarian, CustomUser, CustomUserAdmin # UPDATED: Import CustomUser
from django.contrib.auth.models import Group # Import Group model to unregister it if needed

# Register your existing models
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Library)
admin.site.register(Librarian)
admin.site.register(CustomUser, CustomUserAdmin)


# --- UPDATED: Extend Django's default UserAdmin to work with CustomUser ---
# Define a custom UserAdmin to display CustomUser fields
@admin.register(CustomUser)
class CustomUserAdmin(BaseUserAdmin):
    # These are the fields from AbstractUser that you want to display
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'role')
    
    # These are the fields that will be editable on the user's admin page
    fieldsets = BaseUserAdmin.fieldsets + (
        ('Custom Fields', {'fields': ('date_of_birth', 'profile_photo', 'role')}),
    )