from relationship_app.models import Author, Book, Library, Librarian

# --- CREATE SAMPLE DATA ---

# Create author
author_name = "Jane Austen"
author, created = Author.objects.get_or_create(name=author_name)

# Create books for the author
book1, created = Book.objects.get_or_create(title="Pride and Prejudice", author=author)
book2, created = Book.objects.get_or_create(title="Emma", author=author)

# Create a library
library_name = "Central Library"
library, created = Library.objects.get_or_create(name=library_name)

# Add books to the library
library.books.add(book1, book2)

# Create a librarian for that library
librarian, created = Librarian.objects.get_or_create(name="Mr. John Doe", library=library)

# --- RUN SAMPLE QUERIES ---

# 1. Query all books by a specific author
author = Author.objects.get(name=author_name)
books_by_author = Book.objects.filter(author=author)
print("Books by", author_name)
for book in books_by_author:
    print("-", book.title)

# 2. List all books in a library
library = Library.objects.get(name=library_name)
books_in_library = library.books.all()
print("\nBooks in library:", library_name)
for book in books_in_library:
    print("-", book.title)

# 3. Retrieve the librarian for a library
librarian = Librarian.objects.get(library=library)
print("\nLibrarian for library:", librarian.name)
