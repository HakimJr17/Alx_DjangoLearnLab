### Create Operation

**Python Command:**
```python
from bookshelf.models import Book
book1 = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
print(book1)