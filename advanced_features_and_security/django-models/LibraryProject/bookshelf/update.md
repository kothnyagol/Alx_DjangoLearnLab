# Update Operation

Command:
```python
from bookshelf.models import Book

# Retrieve the book we created
book = Book.objects.get(title="1984")

# Update the title
book.title = "Nineteen Eighty-Four"
book.save()

# Check the updated book
updated_book = Book.objects.get(id=book.id)
print(updated_book.title, updated_book.author, updated_book.publication_year)
