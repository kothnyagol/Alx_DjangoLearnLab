# Delete Operation

Command:
```python
from bookshelf.models import Book

# Retrieve the book we want to delete
book = Book.objects.get(title="Nineteen Eighty-Four")

# Delete the book
book.delete()

# Check all books to confirm deletion
all_books = Book.objects.all()
print(all_books)
