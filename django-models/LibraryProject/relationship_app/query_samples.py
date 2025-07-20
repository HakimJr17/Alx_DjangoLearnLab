# relationship_app/query_samples.py

import os
import sys
import django

# Get the base directory of the Django project (the 'LibraryProject' directory)
# This assumes query_samples.py is in relationship_app/
# and relationship_app is a direct child of the LibraryProject where manage.py is
# So, two os.path.dirname calls to go up from query_samples.py to relationship_app/ to LibraryProject/
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

# Configure Django settings (important for running standalone scripts)
# 'LibraryProject.settings' refers to the settings.py file inside the inner LibraryProject folder
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

# Now you can import your models from your relationship_app
from relationship_app.models import Author, Book, Library, Librarian

def run_queries():
    print("\n--- Performing Sample Queries ---")

    # Clean up existing data to ensure fresh start for demonstration
    print("--- Cleaning up existing data ---")
    Librarian.objects.all().delete()
    Library.objects.all().delete()
    Book.objects.all().delete()
    Author.objects.all().delete()
    print("Existing data cleared.\n")

    # --- Data Setup for demonstration purposes ---
    print("--- Setting up sample data ---")
    author1 = Author.objects.create(name="George Orwell")
    author2 = Author.objects.create(name="Jane Austen")
    author3 = Author.objects.create(name="Harper Lee")

    book1 = Book.objects.create(title="1984", author=author1)
    book2 = Book.objects.create(title="Animal Farm", author=author1)
    book3 = Book.objects.create(title="Pride and Prejudice", author=author2)
    book4 = Book.objects.create(title="To Kill a Mockingbird", author=author3)

    library1 = Library.objects.create(name="City Central Library")
    library1.books.add(book1, book2, book3) # Adding multiple books to a library
    library2 = Library.objects.create(name="Riverside Branch")
    library2.books.add(book4)

    librarian1 = Librarian.objects.create(name="Alice Smith", library=library1)
    librarian2 = Librarian.objects.create(name="Bob Johnson", library=library2)
    print("Sample data created.\n")

    # --- Query 1: Query all books by a specific author. ---
    print("--- Query 1: All books by George Orwell ---")
    george_orwell_books = Book.objects.filter(author__name="George Orwell")
    for book in george_orwell_books:
        print(f"- {book.title} (Author: {book.author.name})")
    print()

    # --- Query 2: List all books in a library. ---
    print("--- Query 2: All books in City Central Library ---")
    city_library = Library.objects.get(name="City Central Library")
    for book in city_library.books.all():
        print(f"- {book.title} (Author: {book.author.name})")
    print()

    # --- Query 3: Retrieve the librarian for a library. ---
    print("--- Query 3: Librarian for City Central Library ---")
    city_library_librarian = Librarian.objects.get(library__name="City Central Library")
    print(f"Librarian for City Central Library: {city_library_librarian.name}")
    print("\n--- Queries Complete ---\n")

if __name__ == "__main__":
    run_queries()