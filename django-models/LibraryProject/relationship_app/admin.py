# relationship_app/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin # NEW: For customizing User admin
from django.contrib.auth.models import User # NEW: Import User model
from .models import Author, Book, Library, UserProfile, Librarian # NEW: Import UserProfile

# Register your existing models
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Library)
admin.site.register(UserProfile)
admin.site.register(Librarian)

# --- NEW: Inline for UserProfile to be editable directly from the User admin page ---
class UserProfileInline(admin.StackedInline): # Use StackedInline for a block layout, TabularInline for a table
    model = UserProfile
    can_delete = False # Prevents accidental deletion of profile when deleting user
    verbose_name_plural = 'user profile' # How it appears in the admin

# --- NEW: Extend Django's default UserAdmin ---
class UserAdmin(BaseUserAdmin):
    inlines = (UserProfileInline,) # Add our UserProfileInline to the User admin

# --- NEW: Unregister the default User admin and register our customized one ---
admin.site.unregister(User) # Unregister the original User admin
admin.site.register(User, UserAdmin) # Register our custom UserAdmin