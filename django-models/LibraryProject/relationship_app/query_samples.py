from relationship_app.models import Author, Book, Library, Librarian

# --- CREATE SAMPLE DATA ---

# 1. Create an Author
author1, created = Author.objects.get_or_create(name="Jane Austen")

# 2. Create Books for that author
book1, created = Book.objects.get_or_create(title="Pride and Prejudice", author=author1)
book2, created = Book.objects.get_or_create(title="Emma", author=author1)

# 3. Create a Library
library1, created = Library.objects.get_or_create(name="Central Library")

# 4. Add books to the library
library1.books.add(book1, book2)

# 5. Create a Librarian for that library
librarian1, created = Librarian.objects.get_or_create(name="Mr. John Doe", library=library1)

# --- RUN SAMPLE QUERIES ---

# Query all books by Jane Austen
books_by_author = Book.objects.filter(author=author1)
print("Books by Jane Austen:")
for book in books_by_author:
    print("-", book.title)

# List all books in Central Library
books_in_library = library1.books.all()
print("\nBooks in Central Library:")
for book in books_in_library:
    print("-", book.title)

# Retrieve the librarian for Central Library
librarian = Librarian.objects.get(library=library1)
print("\nLibrarian for Central Library:", librarian.name)
