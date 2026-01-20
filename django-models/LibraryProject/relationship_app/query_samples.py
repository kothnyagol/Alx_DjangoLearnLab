#!/usr/bin/python3
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
        return author.books.all()
    except Author.DoesNotExist:
        return []

def query_books_in_library(library_name):
    """Return all books in a library (handles multiple libraries with same name)"""
    libraries = Library.objects.filter(name=library_name)
    books = []
    for lib in libraries:
        books.extend(lib.books.all())
    return books

def query_librarian_for_library(library_name):
    """Return librarians for a library (handles multiple libraries with same name)"""
    libraries = Library.objects.filter(name=library_name)
    librarians = []
    for lib in libraries:
        try:
            librarians.append(lib.librarian)
        except Librarian.DoesNotExist:
            pass
    return librarians

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
