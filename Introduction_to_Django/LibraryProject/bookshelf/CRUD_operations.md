### Create Operation

**Python Command:**
```python
from bookshelf.models import Book
book1 = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
print(book1)


### Retrieve Operation

**Python Command:**
from bookshelf.models import Book
retrieved_book = Book.objects.get(title="1984") # Assuming you created '1984' in the previous step
print(f"Title: {retrieved_book.title}")
print(f"Author: {retrieved_book.author}")
print(f"Publication Year: {retrieved_book.publication_year}")


### Update Operation

**Python Command:**
from bookshelf.models import Book
book = Book.objects.get(title="1984") # Retrieve the book by its *original* title
book.title = "Nineteen Eighty-Four"
book.save()
print(book.title)


### Delete Operation

**Python Command:**
from bookshelf.models import Book
book_ = Book.objects.get(title="Nineteen Eighty-Four") # Retrieve the book by its updated title
book.delete()
print(Book.objects.all()) # Confirm deletion