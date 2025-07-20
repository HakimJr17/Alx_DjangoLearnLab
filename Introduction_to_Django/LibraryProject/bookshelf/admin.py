from django.contrib import admin
from .models import Book # Import your Book model

# Register your models here.

# Option 1: Basic Registration (no customization yet)
# admin.site.register(Book)

# Option 2: Registration with Customization (as per the next step)
# We'll use this for the next part of the task
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year') # Display these fields in the list view
    list_filter = ('publication_year', 'author') # Add filters for these fields
    search_fields = ('title', 'author') # Add search capability for these fields

admin.site.register(Book, BookAdmin)