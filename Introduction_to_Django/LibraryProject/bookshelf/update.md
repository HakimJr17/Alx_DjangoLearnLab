### Update Operation

**Python Command:**
```python
from bookshelf.models import Book
book = Book.objects.get(title="1984") # Retrieve the book by its *original* title
book.title = "Nineteen Eighty-Four"
book.save()
print(book.title)