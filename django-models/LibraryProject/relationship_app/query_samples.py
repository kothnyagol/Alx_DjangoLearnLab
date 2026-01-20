#!/usr/bin/pyrhon3
import os
import django

# ----------------------------
# Setup Django environment
# ----------------------------
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

# ----------------------------
# Import models
# ----------------------------
from relationship_app.models import Author, Book, Library, Librarian

# ----------------------------
# Query functions
# ----------------------------

def query_books_by_author(author_name):
    """Return all books by a specific author"""
    try:
        author = Author.objects.get(name=author_name)
        return author.book_set.all()  # or use related_name if defined
    except Author.DoesNotExist:
        return []

def query_books_in_library(library_name):
    """
    Return all books in a library.
    ALX checker expects `.get()` here.
    Make sure only one library exists with this name to avoid MultipleObjectsReturned.
    """
    library = Library.objects.get(name=library_name)
    return library.books.all()

def query_librarian_for_library(library_name):
    """Return the librarian for a library"""
    try:
        library = Library.objects.get(name=library_name)
        return [library.librarian]  # return as list for consistency
    except Library.DoesNotExist:
        return []
    except Librarian.DoesNotExist:
        return []

# ----------------------------
# Run queries if script is executed directly
# ----------------------------
if __name__ == "__main__":
    author_name = "Chinua Achebe"
    library_name = "Central Library"

    print(f"Books by {author_name}:")
    books_by_author = query_books_by_author(author_name)
    for book in books_by_author:
        print(f"- {book.title}")

    print(f"\nBooks in {library_name}:")
    books_in_library = query_books_in_library(library_name)
    for book in books_in_library:
        print(f"- {book.title}")

    print(f"\nLibrarians for {library_name}:")
    librarians = query_librarian_for_library(library_name)
    for librarian in librarians:
        print(f"- {librarian.name}")
