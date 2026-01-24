#!/usr/bin/python3
from relationship_app.models import Author, Book, Library, Librarian

# 1️⃣ Query all books by a specific author
author = Author.objects.get(name="John Doe")  # Replace with actual author if needed
books_by_author = Book.objects.filter(author=author)

# 2️⃣ List all books in a library
library = Library.objects.get(name="Central Library")  # Replace with actual library name
library_books = library.books.all()  # <-- THIS MUST EXIST for ALX

# 3️⃣ Retrieve the librarian for a library
librarian = Librarian.objects.get(library=library)
